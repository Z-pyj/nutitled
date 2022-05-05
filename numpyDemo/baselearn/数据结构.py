# 列表推导式
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# Python 会忽略代码里 []、{} 和 () 中的换行，因此如果你的代码里
# 有多行的列表、列表推导、生成器表达式、字典这一类的，可以省
# 略不太好看的续行符 \

# filter和map
symbols = '$¢£¥€¤'
beyond = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# 列表推导的作用只有一个：生成列表
tshirts = [(x, y) for x in colors for y in sizes]
print(tshirts)

