''' python 的布尔类型 True / False '''

'''
    True:   真值
    False:  假值
'''

'''
布尔运算
    and     与运算  所有都是True结果为True
    or      或运算  只要有一个是True结果为Tue
    not     非运算  把True变成False, False变成True
'''
# and 与运算
print(True and True)    # >>> True
print(True and False)   # >>> False
print(False and False)  # >>> False
print(5 > 3 and 3 > 1)  # >>> True
# or 或运算
print(True or True)    # >>> True
print(True or False)   # >>> True
print(False or False)  # >>> False
print(5 > 3 or 1 > 3)  # >>> True
# not 非运算
print(not True)     # >>> False
print(not False)    # >>> True
print(not 1 > 2)    # >>> True


'''
空值: None
    None也不是布尔类型,而是NoneType。
'''
print(bool(None))   # >>>  False
print(type(None))   # >>>  <class 'NoneType'>