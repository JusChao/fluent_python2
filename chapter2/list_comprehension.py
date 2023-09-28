# listcomps
# 列表推导式

symbols = 'ABCDEFG'

# 推导式中忽略换行
codes = [ord(symbol) for symbol
         in symbols]
print(codes)

# python3 推导式中都是内部变量
x = 'abcd'

codes = [ord(x) for x in x]
print(codes)