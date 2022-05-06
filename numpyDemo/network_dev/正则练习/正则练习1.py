import re

#
# # compile()模式对象
# r = re.compile(r'[a-z]+\d{4}')
#
# # 反斜杠不以任何特殊的方式处理前缀为 'r' 的字符串字面
# # r.match()确定正则是否从字符串的开头匹配
# m = r.match('abcd1234')
#
# # group()返回匹配的字符串
# # group() 返回正则匹配的子字符串。
# # start() 和 end() 返回匹配的起始和结束索引。
# # span() 在单个元组中返回开始和结束索引。
# # 由于 match() 方法只检查正则是否在字符串的开头匹配，所以 start() 将始终为零
# s = m.group()
# print(s)
# m.start()
# m.end()
# m.span()
#
# sr = "one12twothree34four"
# r1 = re.compile('\d{2}')
# s1 = r1.search(sr)
# if s:
#     print('search find:', s1.group())
# else:
#     print('search not find')
#
# s2 = r1.findall(sr)
# print(s2)
#
# # 模块级函数
# # 你不必创建模式对象并调用其方法
# s3 = re.match(r'From\s+', 'from abcd',re.S)
# print(s3)
#
# # 编译标志

# 分组
p = re.compile('(a(b)c)d')
s4 = p.match('abcd')
# groups() 方法返回一个元组，其中包含所有子组的字符串，从1到最后一个子组
print(s4.groups())

# 子组从左到右编号，从 1 向上编号。 组可以嵌套；要确定编号，只需计算从左到右的左括号字符
print(s4.group(0))
print(s4.group(1))
print(s4.group(2))

# group() 可以一次传递多个组号，在这种情况下，它将返回一个包含这些组的相应值的元组
print(s4.group(1, 2, 1))

# \b字边界。 这是一个零宽度断言
p = re.compile(r'\bclass\b')
# 仅当它是一个完整的单词时匹配 class
print(p.search('no class at all'))

# 模式的 split() 方法在正则匹配的任何地方拆分字符串，返回一个片段列表
p = re.compile(r'\W+')
s5 = p.split('This is a test, short and sweet, of split().')
print(s5)

# 搜索和替换
# sub(replacement, string[, count=0])
p = re.compile('(blue|white|red)')
s6 = p.sub('colour', 'blue socks and red shoes')
print(s6)

s7 = p.sub('colour', 'blue socks and red shoes', count=1)
print(s7)
