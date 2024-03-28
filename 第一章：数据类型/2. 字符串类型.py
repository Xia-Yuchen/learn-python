''' python 的字符串类型 string '''

'''
1. 如何定义字符串
'''
# 定义字符串案例
name_1 = 'jack' # 单引号定义
name_2 = "jack" # 双引号定义
name_3 = '''jack''' # 三个单引号定义
name_4 = """jack""" # 三个双引号定义


'''
2. python 中字符串常用和的方法
    .lstrip()   去除左边空格
    .rsplit()   去除右边空格
    .split()    去除两边的空格
    .startswith()   判断字符串是否以某字符串开头
    .endswith()     判断字符串是否以某字符串结尾
    .split()    分割字符串
'''
## 1. 去除首位空格
msg_1 = "    Python编程时光    "
msg_1.lstrip()  # 去除左边空格  >>>  'Python编程时光    '
msg_1.rstrip()  # 去除右边空格  >>>  '    Python编程时光'
msg_1.strip()   # 去除两边空格  >>>  'Python编程时光'
## 2. 判断字符串是否以某字符串开头
msg_2 = "Hello, Python"
msg_2.startswith("Hello")   # >>>  true
msg_2.startswith("hello")   # >>>  false
## 3. 判断字符串是否以某字符串结尾
msg_3 = "Hello, Python"
msg_3.endswith("Python")    # >>> true
msg_3.endswith("python")    # >>> false
## 4. 格式化字符串
msg_name = '小黑子'
msg_4 = f"你好我是{msg_name}"   #  >>> "你好我是小黑子"
## 5. 字符串分割
languages = "Python,Java,Golang"
languages.split(",")    #  >>> ['Python', 'Java', 'Golang']
