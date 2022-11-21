import time
import chaoxing
import zhiketang

subisfalse = 0  # 作业未提交数量

chaoxing.cookie2 = None
chaoxing.cookie = chaoxing.login('your_tel', 'your_password')  # 学习通  把参数改为你的账号和密码 例如:login('1777436', '123456')
course_list = chaoxing.course_list_data()
works2 = chaoxing.get_homework(course_list)
studen_info = zhiketang.login('yor_student_id', 'your_id_back6') # 把参数改为你的学号 和你的身份证后六位 login('20225321****', '2****3')
print('智课堂登录成功...')
works1 = zhiketang.work_list(studen_info)
print('\033[1;32m' + '完成的作业'.center(80, '=') + '\033[0m')
for i in works1:
    if i.submitStatus:
        i.print_obj()
for i in works2:
    if i.status in ['已完成']:
        i.info()
print('\033[1;32m' + '完成的作业'.center(80, '=') + '\033[0m')
print('\033[1;33m' + '\033[1;32m智课堂未完成的作业\033[0m\033[1;33m'.center(92, '=') + '\033[0m')
for i in works1:
    if not i.submitStatus:
        i.print_obj()
        subisfalse += 1
print('\033[1;33m' + ''.center(80, '=') + '\033[0m')

print('\033[1;33m' + '\033[1;32m学习通未完成的作业\033[0m\033[1;33m'.center(92, '=') + '\033[0m')
for i in works2:
    if i.status in ['未交', '超时']:
        i.info()
        subisfalse += 1
print('\033[1;33m' + ''.center(80, '=') + '\033[0m')
print(f"\033[1;31m [ 还有{subisfalse}个作业没做 ]\033[0m".center(85))
time.sleep(1000)
