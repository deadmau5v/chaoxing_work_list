import requests as req
from bs4 import BeautifulSoup
import time
from sys import argv


class Course(object):
    def __init__(self):
        self.clazzid = None
        self.courseid = None
        self.personid = None
        self.url = None
        self.img = None
        self.coures_name = None
        self.coures_teacher = None

    def info(self):
        print(self.clazzid)
        print(self.courseid)
        print(self.personid)
        print(self.url)
        print(self.img)
        print(self.coures_teacher)


class Wrok(object):
    def __init__(self):
        # 作业地址
        self.url = None
        # 作业名称
        self.work_name = None
        # 作业完成状态
        self.status = None
        # 作业剩余时间
        self.time = None
        # 课程名称
        self.clazz = None

    def info(self):
        if self.time is None:
            print(f"\033[1;32m[{self.clazz}]\033[0m {self.work_name} \033[1;32m[状态:{self.status}]\033[0m")
        else:
            time = str(self.time).replace('\t', '').replace('\n', '').replace('\r', '')
            print(
                f"\033[1;32m[{self.clazz}]\033[0m {self.work_name} \033[1;33m[状态:{self.status}]\033[0m {'[剩余时间:' + time + ']' if time != '未限时' else time if self.status in ['超时', '未交'] else ''}")


def login(username, password):
    url = 'http://passport2.chaoxing.com/fanyalogin'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42',
        'Referer': 'http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http://i.chaoxing.com'
    }
    data = {
        'fid': '-1',
        'uname': username,
        'password': password,
        'refer': 'http%3A%2F%2Fi.chaoxing.com',
        't': 'true',
        'forbidotherlogin': '0',
        'validate': '',
        'doubleFactorLogin': '0',
        'independentId': '0'
    }

    # 先访问登录页面 拿到 SSID cookies
    r = req.get(url='http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http://i.chaoxing.com',
                headers=header)
    # 用拿到的SSID 访问登录API 传入数据
    r = req.post(url='http://passport2.chaoxing.com/fanyalogin', cookies=dict(r.cookies), data=data)
    if r.json()["status"]:
        print('学习通登录成功...')
    else:
        print('学习通登录失败 密码错误或者账号错误')
    return dict(r.cookies)


def course_list_data():
    """获取课程列表"""
    url = 'http://mooc1-1.chaoxing.com/visit/courselistdata'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
    }
    data = {
        'courseType': '1',
        'courseFolderId': '0',
        'baseEducation': '0',
        'superstarClass': '',
        'courseFolderSize': '0'
    }
    global cookie
    r = req.post(url, cookies=cookie, headers=header, data=data)
    try:
        soup = BeautifulSoup(r.text, 'html.parser')
        soup = soup.find(id='courseList')
        soup = soup.find_all('li')
    except:
        print(r.text)

    couress = []
    for i in soup:
        if len(i) < 2:
            continue
        course = Course()
        course.clazzid = i.attrs['courseid']
        course.courseid = i.attrs['clazzid']
        course.personid = i.attrs['personid']

        # 获取课程老师
        course.coures_teacher = i.find_all('p')[1].attrs['title']
        course.coures_name = i.find(name='span', attrs={'class': 'course-name overHidden2'}).text

        # 获取链接
        course.url = i.a.attrs['href']
        course.img = i.find('img').attrs['src']
        couress.append(course)
    global cookie2
    cookie2 = dict(r.cookies)
    return couress


def get_homework(course_list):
    # url = f'https://mooc1-1.chaoxing.com/visit/stucoursemiddle?courseid={course_list[0].clazzid}&clazzid={course_list[0].courseid}&vc=1&cpi={course_list[0].personid}&ismooc2=1&v=2'
    # url = f'https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=222678166&clazzid=67643081&cpi=281472339&enc=31c61833fd8957b72f4a39527304924b&t=1668852859139&pageHeader=0&v=2'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
    }
    global cookie
    global cookie2
    # r = req.get(url=url, headers=header, cookies=cookie)
    works = []
    for i in course_list:
        r = req.get(url=i.url, headers=header, cookies=cookie)
        soup = BeautifulSoup(r.text, 'html.parser')
        enc = soup.find(id='workEnc').attrs['value']
        url = f'https://mooc1.chaoxing.com/mooc2/work/list?courseId={i.clazzid}&classId={i.courseid}&cpi={i.personid}&ut=s&enc={enc}'
        r = req.get(url=url, cookies=dict(cookie, **cookie2), headers=header)
        soup = BeautifulSoup(r.text, 'html.parser')
        if '暂无作业' in soup.text:
            continue
        try:
            soup = soup.find(name='div', attrs={'aria-label': '作业列表'})
            soup = soup.find_all(name='li', attrs={'onclick': 'goTask(this);'})
        except AttributeError:
            print(soup)
            for i1 in works:
                i1.info()
            exit()
        for s in soup:
            work = Wrok()
            work.url = s.attrs['data']
            work.work_name = s.attrs['aria-label']
            work.status = s.find(name='p', attrs={'class': 'status fl'}).text
            work.clazz = i.coures_name
            if work.status in ['超时', '未交']:
                try:
                    work.time = str(
                        str(s.find(name='div', attrs={'class': 'time notOver'}).text).replace('\n', '')).replace(' ',
                                                                                                                 '')
                except AttributeError:
                    work.time = '未限时'
            works.append(work)
    return works


if __name__ == "__main__":
    cookie2 = None
    cookie = login(input('输入用户名'), input('输入密码'))
    course_list = course_list_data()
    works = get_homework(course_list)
    print('\033[1;32m' + '完成的作业'.center(80, '=') + '\033[0m')
    for i in works:
        if i.status in ['已完成']:
            i.info()
    print('\033[1;32m' + '完成的作业'.center(80, '=') + '\033[0m')
    print('\033[1;33m' + '未完成的作业'.center(80, '=') + '\033[0m')
    for i in works:
        if i.status in ['未交', '超时']:
            i.info()
    print('\033[1;33m' + '未完成的作业'.center(80, '=') + '\033[0m')
