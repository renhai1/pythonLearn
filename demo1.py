# print("hello,world!")
# str = '123456789'
'''
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# 输出所有的保留字
多行注释
多行注释
多行注释
'''

'''
import keyword
print(keyword.kwlist)
'''
'''
python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。
'''
# if True:
#     print("True")
# else:
#     print("False")

# if True:
#     print("Answer")
#     print("True")
# else:
#     print("Answer")
# # 缩进不一致，会导致运行错误
# print("False")
# item_one = 'sss';
# item_two = 'aa'
# item_three = 'ccc'
# total = item_one + \
#         item_two + \
#         item_three
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)
