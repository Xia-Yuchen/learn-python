'''
1. 变量不需要声明类型
    pyhone 中的变量和常量不需要事先声明类型
'''
# 变量声明案例如下
myName = "小爬虫"
myAge = 18


'''
2. 赋值与比较
    python 中用 = 号来给变量赋值，比如 age 变量的值为18     >>> age = 18
    python 中用 == 来比较两个值是否相等，结果返回 true / false      >>> age === 18 // true
'''
# 赋值与比较案例如下：
newAge = 18
newAge == 18 # print(newAge == 18) 结果：true
newAge == 15 # print(newAge == 15) 结果：false


'''
3. 变脸需要先创建再使用
    每个变量在使用前必须赋值，变量赋值后才会被创建。
    新的变量通过赋值的动作，创建并开辟内存空间，保存值。
    *注：* 如果没有赋值而直接使用，会抛出变量未定义的异常
'''
# 没赋值的异常抛出案例：
# errAge # Traceback (most recent call last):


'''
4. 赋值的方法
    (1) 单个直接赋值    age = 18
    (2) 多个批量赋值    a = b = c = 1
    (3) 先计算再赋值    age = 18 + 2
    (4) 分别赋值        a, b, c = 1, 2, 3
'''


'''
5. 简单介绍常量
    常量就是不变的变量，在 python 中，通常全部大写的变量表示常量
'''
# 常量的案例
PI = 3.1415926