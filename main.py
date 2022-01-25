# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import datetime
# import re
# import pickle
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# others = {'city': 'beijing', 'hobby': 'programming'}
#
#
# def per_info(name, number, **kw):
#     print(f'name:{name}, number:{number}, others: {kw}')
#
#
# per_info('forest', '12', city=others['city'], hobby=others['hobby'])
# per_info('forest', '12', **others)
#
#
# total_val = 0
#
#
# def sum_num(arg1, arg2):
#     global total_val
#     total_val = arg1 + arg2
#     print(f'function internal var: {total_val}')
#     return total_val
#
#
# print(f'function result: {sum_num(10, 20)}')
# print(total_val)
#
# print(f'today is: {datetime.datetime.today()}')
# print(f'today is: {datetime.datetime.now()}')
# print(f'today is: {datetime.datetime.utcnow()}')
# dt = datetime.datetime.now()
# print(f"strptime is: {dt.strptime('2021-12-23 09:53', '%Y-%m-%d %H:%M')}")
# line = 'Cats are smarter than dogs'
#
# matchObj = re.match(r'dogs', line, re.M | re.I)
# if matchObj:
#     print(f'use match, the match string is: {matchObj.group()}')
# else:
#     print("No match string!!")
#
# path = './test.txt'
#
# f_name = open(path)
# print(f_name.read())
#
# # try:
# #     d = dict(name='xiao zhi', num=1002)
# #     f_name = open('dump.txt', 'wb')
# #     pickle.dump(d, f_name)
# # finally:
# #     f_name.close()
# try:
#     f_name = open('dump.txt', 'rb')
#     dic = pickle.load(f_name)
#     print(dic['name'])
#     print(dic['num'])
# finally:
#     f_name.close()
#
#
import os
import time


def batch_rename(path):
    global img_num
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False

    if os.path.isfile(path):
        file_path = os.path.split(path)
        lists = file_path[1].split('.')

        file_ext = lists[-1]
        img_ext = ['bmp', 'jpeg', 'gif', 'psd', 'png', 'jpg']
        if file_ext in img_ext:
            os.rename(path, file_path[0] + '/' + lists[0] + '_cn.' + file_ext)
            img_num += 1
    elif os.path.isdir(path):
        for item in os.listdir(path):
            batch_rename(os.path.join(path, item))


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s %s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s %s/>' % (name, attr_str)


if __name__ == "__main__":
    img_dir = 'c:\\Screenshots\\vpn'
    start = time.time()
    img_num = 0
    batch_rename(img_dir)
    print('deal with %s pictures, time consuming: %0.2f.' % (img_num, time.time() - start))
    print(factorial.__doc__)
    print(factorial(3))
    print(type(factorial))
    print(map(factorial, range(11)))
    print(list(map(factorial, range(11))))
    print(tag('br'))
    print(tag('br', 'hello', 'world'))
    print(tag(content='testing', name='img'))
    print(tag('br', 'hello', id=33))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    # my_tag = {'name': 'img', 'cls': 'framed'}
    print(tag(**my_tag))
    str = "this is really a string example...wow!!!"
    substr = "is"

    print(str.rfind(substr))







