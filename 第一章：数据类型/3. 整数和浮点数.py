'''
python 的数字类型 Number
    python 支持的数字类型又三种：整数 ，浮点数 ，复数
'''

# 整数 Int
## 通常被称为整型，是正或负整数，不带小数点。例如：1，100，-8080，0，等等。
print(type(100))    #  >>> <class 'int'>
print(type(-100))   #  >>> <class 'int'>


# 浮点数 Float
## 浮点数也就是小数，如1.23，3.14，-9.01，等等。
print(type(1.23))   #  >>> <class 'float'>


# 复数 Complex
## 复数由实数部分和虚数部分构成，可以用a + bj，或者 complex(a,b) 表示，复数的实部a和虚部b都是浮点型。
print(type(10 + 0.2j))  #  >>>  <class 'complex'>
print(type(complex(10, 0.2)))  #  >>>  <class 'complex'>



'''
数字类型的常用方法：
    +   加法
    -   减法
    *   乘法
    /   除法
    //  取模
    %   取余
    abs()   计算绝对值
    int()   数值直接取整
    round() 数值四舍五入
'''
# 加法 +
print( 10 + 20 )    #  >>>  30
# 减法 -
print( 20 - 10 )    #  >>>  10
# 乘法 *
print( 10 * 20 )    #  >>>  200
# 除法 /
print( 20 / 10 )    #  >>>  2.0
# 取模 //
print( 10 // 3 )    #  >>>  3
# 取余 %
print( 10 % 3 )    #  >>>  1
# 计算绝对值 abs()
print(abs(-10))    #  >>>  10
# 数值直接取整 int()
print(int(3.14))    #  >>>  3
# 数值四舍五入 round()
print(round(3.14))    #  >>>  3
print(round(3.74))    #  >>>  4