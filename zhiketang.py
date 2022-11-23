import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 生成 UA
ua = UserAgent()

#  全局cookie
cookie = dict()


def login(username, password):
    global cookie
    login_url = 'http://cas.hnqczy.com:8002/cas/login'
    studen_url = 'http://218.75.206.107:8008/study/web/study'
    headers = {
        "user-agent": ua.chrome
    }
    r = req.get(url=login_url, headers=headers)
    cookie = dict(r.cookies)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = {
        'authType': '0',
        'username': username,
        'password': password,
        'lt': 'LT-681-dwTwQm6DoGH1ddlOwGY4LqNyO4XXfT-cas1',
        'lt': 'LT-695-cASalFvofRyxNZWbFkndu19suQqqRU-cas1',
        'execution': 'aa145c76-9db2-45ae-8fd4-00e0e4af6a89_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuTUdGcU1UQkVUMlZGZFZaNGFsWnVVamxrYUc5bmIwOVhTM2Q1VDBsbEt6Y3ZWbnBXYjNnd09HMVpWRXBuVUZKaVUySmtNMVV6SzBRcldrOVVVMjFRVkRnM2FEazVVRXB4VTJkUmRFc3lSMk5oT0ZKSlpXTnFkRzV4Yld4d09IVnhTbXBxV1ZoVGJUWTFNMHROYlhoM1ZVVTJURXhSU2pVMVFUbFBiV1ZzUjFsdmIwOUpWM1IzVTFSbVZVNDBkVTQ1WmxkdlducHRaa1ZRT1ZkWWFYWjJURXRYWW5oR1EydGlWV2xZY1RaMFowRjNhMjFCUVVOWk1XSjJUbTVFWWpSSFNsQnhkRE5qZUVaV1ZqRTFUWEExWVVKblUwNWtTa1J3YXpKdFRUTklXRUYxVkhGaU1UTlpUSGhSUlRSWVozbFNhbVo1ZFdndk9HbFNVM2t2TjBwRE1uSllPVlZNVVRkNlF6Vm1SR1JZZGtnd1MzZ3pPVXczWTNVd2NsSkpjM1JVVDJwSVdISkdiRXhSWm5vNFJEZEhRV1kyTUdWNlFVbE5PVEJ3VEhWdVFXRklhbFJCUzJaaWFITllkWGREZFZZNFRuWnpkemd6YmtGbGNUSkRWMU01Y21WYVFXbHZSRzVtY1RCcWVXbFZVemRVWldsa2RraFhNMFZGWWtSRVJra3phVWt3Y201TWJHWk5kbFptTVhaVmRWUTRlSFJJUVRNNWRrMVVXVVFyWm5obFZXWnVhRGsyVHpNdmMwWnNaRnBYY0hWV2VVUnBhRXhTVVZJMVRrcGtkMnR2Y2s1R1VUYzJVbGgwU0ZwMFNHZzJSVEY1WWxCM04wUnhlRkJYVW5oUlRuVnFkWFZNZGt4c1ZETlZWV1JOV25WMlpGSnBWa3RNWjJRd2JucHhVVlk1U0V4MU1IbEhVRVpKU214RlRuUk5RbXR6TTFWRE0zY3hSMFJZV0hwWEsxb3ZSa3BvYWtWUVV6aDFWa0ZEY2pseFQwNWFka3B1TXpFNGFsTm5USGQ2V1ZRclpuTnRjbXBhY2xrNFZUWm1OamhEY1d4Qk1EUlBlakp6VlZOMk1HWXdlWE5STmtaeVpGRlRVa3BLTTJGelZsRTRjSEpsYVRObVUwNVNTVUowUTFKaWFWaERPVEZFVFhnM1IwUXlOR1JLVkdsUFJqTk1UazVyV1VKVFlraFRhRFFyV0hCRlVrb3ZOMlpQU0dKd2FFeERhMHBQVEZjNVVGTTJjbWhCZDJ4UFRHNXdiSFJSVGtsQk1FWlJNbUlyUkRSeVUzUk9Za0pCVmpGYVlrbFJZa3hFY1U1MkwwNVVPR3R4TURoWGNYZHphVms0YjNGMlluWlhkWFV2VWpKd1RtNUlaVWcyUXl0bGNqSlNTVEJCYW1aRU9XRm5ORzFuTm5odkwwVXlURFJRTWpWcE1GcExaR2RJVkVWSVpXSXdWV1JMZVdOaVdFMTZlVWxLYWk5WmFFMTFNbUZOT0ZWVmVUY3lUa2hqVFRoQmQxTlZhM0VyTkRGbFlsSk9XWFJOYm5sMlpUVTJhVEIzV2xoMmJXb3haSEV3VEhvemRqUTJiWFJhTlhGMFJsVmFURlF5UmtKcVpFUlBXV1l4UW05a1EzWTJNbTlyUW5KWmVqaGljRVIyTkZVcmJYTnVibTkzT1d0M1NsWkVaM2RzUzFkcmQza3ZkbXhtYmpRclJtMVNhbmt4WW1wdU5IcFJhMEU1WkRKaWIybDZlV2tyTVdkVVVXaEpiVUpZTHpoc2JtWjBTazh4ZDJOMlVrTmpZV0Z6UVRCNk5FczFaMDFaWkdWcGNXTnRRak5TTkhaQ2JHOVJlVmM0Y0cxb2JHZFVOMG94ZDBGRlRVVXZlblpEZVhadGVWa3diRTlhTDJFNWFrNTFlVVJ3TUVSWFNGSktaRUZFVFRGclFsTnNNa2R5VUVKTFkzRnBaMncxV0hCNGNscGlLemRJWVVOTFoxaDBOMmh3ZWpKVE0wRnlVV05NYTJoRGJFMW1jWEVyTkhOaVdIRlliV2RrYjJWSFVYbEdibmROUlZwWVFsWnNTaXN3TWpKbVRIVXlWak5CTUdwYWQwbExSbXhaTkRKbE1WSjVWamg1U0haVFVtMU9jMUowVlVVMFFVMW9UMmhwZWxSRFJtVTVZVTFzTW1GaFVtYzRRelEyY1dWemQzbDJRamRsYnpZeVlUWkRjbFZsY2xNemVtb3JaV1IwWTI1NVNHdEhPVkZ3V0ZaUWJUSmpOa2xUTkZwWEwzZEZXVnByVFRZMUx5czVPV3Q2YkVsSU5sZHBOSEJwV1RkUFNsRmtiVFo1WjNJMWMwUXdOQzlLUjBSWmVqaERRMFp2Yld0T2FWcGlXRXBYYTNwbFRVVlFaRWxYVkdoNE5ubFFRVTVwY3pkU2JXNTNTRWRzTDBOaWEyOVdVR3hRYVhsa1dHb3lWRFJWYjNWWFNsSkVWbWh4Y1RkeWNGZGlTWEpNWjFWcU9XeERRelJPZUdWU1pERnJSVFV4Vms4MlJuVjFkV1Z0Wkd0NFRVWm1lRlJvYVhWNFRTODBLMGRuTUZJeWJYTnBXV1kxUkZsc2J5dEphVmhDU1c0d2EwUlFha05MUlhwRWRXMU1jMUozWkhremJGQmxaMjUxY1U1aE9VeDZVVEpNUzBsWlMweFhiVFU0VlU5M05sWnlNVkl2YzJOWlZtMTRTRWxFTmxwb1JEbDVRbmRGZHl0Q1JIUTNkMU16U1d0QmJ6bFFiM0J4T0VZMVZWcERLMngwZUdGcFEwdDJjMUp2WVZwdlMwVkJURlY2V0hKNWIzUXpURlYwZVdZNWNWWldOMjl2WldkMWVXcEhOVm93ZGxZMk1qRXJVbmxtT1ZacFRIVmpZbUZOVm5sTUwxazVWa2swYzIxMWEyMXNZV1ZxYVVSUVpEQTNaSFoyVjI4eFRHMXVLMUYxWVZBMFJIaEJWaTk0UjI1M1luZExkMGQ2Y0VSYVkwZzBjbmxOUm1sYVpVTjJNV2xKVFVOdUwydDRkVW96WVVobE5rdFFkM0J3YURSVU0weHRhbm8yTTBSR2FFYzJNbUYwYlRCUU1sRjNPV0Z3V1V0cVRqWlVTUzlUYUdaQ2IyNVVLMVVyU1RGQ2RVOTFTRWx2VDB0UlUxbGlVRzlEUXl0WU1GVlpiMWt3TlhjMGRIaEphSEkxU2xsdk5VaGpUQ3N3WWtacVRVVjJZU3Q1VlRkMWFrcHZaakp4VlRKYVEzTldlV013TTIxMWRsQlZOamN3WjNodFNucFBiWFZwWjFkT09ISm1LMUkwWlN0V1lrTnRTMGRKTm1GUFEwMWtLMGRWWml0WVV6TTFUVk4yVkVrMGNYUnpaazFXZW1aeWJFNTRZbkZUUldoNGVsRlJja1kwVkZkcWNVaFpiVzlyZFhwMGRHOTRPVzlXZEVkaFFscFRLMnREY0hwWmVsaENkMlJHYUZkbFJITjRibXhqY0ZjeFJqVjJaRzVOVGpkQ2VVZzFiSGx5V1RCRE0ydHpOVmxIZVhGRE5EUnZSMlJTTWpJeFltbEZNV2xLTjFaUVVHODFPR3A1TkhaNVlXVnpVVFJCVVZkQmFHa3Jlbk5LTDJoNVJTczVVRWROWW5wdlNuQldTbnBZVWt4YVdVczBkbkIwUVdneVZrcFRiMGt4TmtoS04wUnJORlpQTURaSVEwVjZaRWxzVEVkVlVERXdZa2hZVkRseU1ETnhUMnhWVkZOcEsyZHJTM0UxZEhVMmNtTmlRVzlsT1UxRlJDOTVSa296WVd3eGVGcFVia3RwY0RSbU4yeGtiMHgyTTFjelpHaHdTbkUzY0hWUVVVSjBlV0ZhTlVOcVpXUlJObmxWTW00clpsZEJXVmhVV1hsS1FuTkZUVTFGZUdwS04yTmFTM1ZVZGpOVGFIQlJORXBKTkZRNFVXbFZUR1p4VkU1b05tRk1ibmxOVUhCbk9XeG1kRkpzUWpjd01FUnBkbTFFVmxKRmQxWk5kVkZpYmpWV1JsSlNNeTk0ZEhjemJWYzRkREJ0Y1hCWWVscEJkR0p6T0VkTlpEY3pWekJWYm1zdldVSXZWWGxSYTBsSVpWWlVjV3d5T1VvNWJEWTFjRXh2YjJoa01rb3hZMDU0ZEZOQmJsTkVVR3RtTVZsSlJDOTRVMlUzUmpseGNISkJTRGd5TkhKbFQzaHlUMnMyYXpkQmFWVkRTRTVWYm5kUlUyRkZjVTlQUzNCYU4xaElkMjEyYVVsbFdtUnBjMFpsY0dwWk5sb3JNbXh2YVRkblJHcE1Na05rY2tGTkszSkpRa1pQUzNkRU1IVmtVV1JGVTNsUlpDdHBSME5TTTFsaFkzRkpjMGRZUjBGU2NYRXdkMHBpZEdSdmJFWnpOVFpYZDNnNE4wUTNOWEV5YW5sWk16TmtVMlpVTjNSYU4ycEhhRlJPVGsxRlUzTkROVEJQUkc0MVdWQTFNMk50YWxwVVVWVnlXUzlDVlVkb1EwdDBjbWRxVVVaeFRrOTJSV2s0WWpkeWJtTnZOM3BtU0ZOdE5teDVhSE5vY1d3elp6ZHhabVY1Y205WlVsTm5MM1o1Tmtvck1XNXVNbmhoVTFJM2RrUmlWbm94ZWpOdFEzUk1lbEIzTmtkQ1pGaHVhblpRWVZJeU9VWk1OVmxQUzBkeGNFaDVOMWxtUjJwSE9WTTRRbGxWY0NzeVUzcFdMMDUwV1hkTFdGSTVWRll3VGtoWk9FeE1OMlJVVUVKWFpVOWhTMnhvTDJsRlFqbG9hVzlGYjBFeVdtUnlkVFJvVm1oeFdEaEpTbnBOTlZRd2FGaEdaVEEzYzA1NWQxUTJOelJMVHpCSlVWQTNaRTA1YW5OUVkwZDRWalZMYmxsNVVXUlBNaTh3WkRNNGVXWkdUbFJoZFZOM0sxUnVURU5EUXpRNFozQkdXR0pTTVN0cmExUXliVGhRWjBsQ1VrNTZRbkU1UlVzNGNtbDRkemwxZFdKYUwwcGpaM3ByZEZKclMyZGFaMlV4U21OQk1uQllSMDlCSzBKcFJtVmxRVVI2YzNKblBUMC5SdTdWRENHS09TT19WY0RXOWlnT1ZNMnEteHo0LVRuaEJzSjFGNnB0VkdzS2g1U2dkQ2ZxNnN3V2dNVUp6Z01mUjRYXzAtMmVkZC1qaW55eU5OalBMZw==',
        '_eventId': 'submit',
        'randomStr': ''
    }
    for i in soup.find_all(attrs={'type': 'hidden'}):
        data[i.attrs['name']] = i.attrs['value']
    login_api = f'http://cas.hnqczy.com:8002/cas/login;jsessionid={cookie["JSESSIONID"]}?service=http://218.75.206.107:8008/study/shiro-cas'
    r = req.post(url=login_api, headers=headers, cookies=cookie, data=data)
    if '登录成功' not in r.text:
        print('登录失败')
    else:
        print('登录成功')
    return r.cookies


cookie = login('202253210250', 'ZvZ/CI2r3FUO5t7H+ghypg==')
print(list(cookie)[0])
import requests as req
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree
from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad

# 全局变量
header = {
    'User-Agent': UserAgent().random
}
cookie = dict()


class Studen_info():
    def __init__(self):
        self.sid = None
        self.uid = None
        self.time = None


class Course_info():
    def __init__(self):
        self.courseId = None
        self.courseName = None
        self.indexUrl = None
        self.teacherName = None


# 作业类
class Work(object):
    def __init__(self):
        # 课程名称
        self.courseName = None
        # 截止时间
        self.endTime = None
        # 作业标题
        self.title = None
        # 提交状态
        self.submitStatus = None

    def print_obj(self):
        if self.submitStatus:
            print(f"\033[1;32m[{self.courseName}]\033[0m {self.title} \033[1;32m[状态:已完成]\033[0m")
        else:
            print(
                f"\033[1;32m[{self.courseName}]\033[0m {self.title} \033[1;33m[状态:未交]\033[0m [截至时间:{self.endTime}]")


def enc(key, data):
    #  ========================加密密码=========================  #
    key = key.encode()
    data = pad(data.encode(), 16)
    enc = AES.new(key=key, mode=AES.MODE_ECB)
    data = enc.encrypt(data)
    enced = base64.b64encode(data)
    return enced
    #  =======================================================  #


def find_cookie(html, cookie_name):
    cookie_str = html.xpath('/html/body/script[3]')[0].text
    start = cookie_str.find(cookie_name)
    end = cookie_str.find("\n", start)
    cookie_data = cookie_str[start: end]
    cookie_data = str(cookie_data).replace(' ', '').replace(cookie_name, '').replace('=', '').replace("'", '').replace(
        ';', '').replace('\r', '')
    return cookie_data


def login(username, password):
    global header, cookie

    login_url = 'http://cas.hnqczy.com:8002/cas/login?service=http://218.75.206.107:8008/study/shiro-cas'
    r = req.get(url=login_url)
    # 访问登录页面 拿到cookie
    cookie = dict(r.cookies)
    #  ============= 制作 POST 的 login_data ==============  #
    # 加密密码 用enc()函数👆
    password = enc("c6dda3852e2d4be2", password)
    login_data = {
        'authType': '0',
        'username': username,
        'password': str(password).replace("b'", '').replace("'", '')
    }
    # 解析登陆页面html 提取出隐藏在html里的密钥
    soup = BeautifulSoup(r.text, 'lxml')
    soup = soup.find_all(attrs={"type": "hidden"})
    # 将html里的密钥添加到login_data里
    for tag in soup:
        login_data[tag.attrs['name']] = tag.attrs['value']
    login_api = 'http://cas.hnqczy.com:8002/cas/login?service=http://218.75.206.107:8008/study/shiro-cas'
    r = req.post(url=login_api, headers=header, data=login_data, cookies=cookie)
    #  ================== 得到HTML页面中的 cookie ================== #
    html = etree.HTML(r.text)
    studen_info = Studen_info()
    studen_info.sid = find_cookie(html, '_jsessionid')  # 这个函数看上面👆 它可以从主页解析出隐藏的cookie
    studen_info.time = find_cookie(html, '_currentTimestamp')  # 这个函数看上面👆 它可以从主页解析出隐藏的cookie
    studen_info.uid = find_cookie(html, '_userId')  # 这个函数看上面👆 它可以从主页解析出隐藏的cookie
    cookie = dict()
    cookie['sid'] = studen_info.sid
    r = req.get(r.url, headers=header, cookies=cookie)
    return studen_info


def classlist(studen_info):
    global header, cookie
    class_list_api = f'http://218.75.206.107:8008/study/web/study/queryUserCourseList?_time={studen_info.time}&courseCategory=1&courseMode=&courseName=&courseTypeId=&pageNumber=1&pageSize=12&term=2022%E5%B9%B4%E7%A7%8B'
    r = req.get(url=class_list_api, headers=header, cookies=cookie)
    courselist = []
    for i in r.json()['list']:
        cores = Course_info()
        cores.courseId = i['courseId']
        cores.courseName = i['courseName']
        cores.teacherName = i['teacherName']
        cores.indexUrl = i['indexUrl']
        courselist.append(cores)
    return courselist


def work_list(studen_info):
    url = f'http://218.75.206.107:8008/study/web/study/homework/selectMyHomeworkList?_time={studen_info.time}&courseId=&pageNumber=1&pageSize=64&status=&title='
    r = req.get(url=url, cookies=cookie)
    works = []
    for i in r.json()['list']:
        work = Work()
        work.courseName = i["courseName"]
        work.title = i["title"]
        work.endTime = i["endTime"]
        work.submitStatus = i["submitStatus"]
        works.append(work)
    return works
