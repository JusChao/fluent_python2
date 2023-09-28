# 元组不仅仅是不可变的列表
# 除了用作不可变的列表，它还可以用于没有字段名的记录。
#

# 元组记录
lax_coordinates = (120.08071, 30.482262)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    # 报错
    # print('{}/{}'.format(passport))
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# 列表拆包测试
lista = [1, 2, 3]
a, b, c = lista
print(a)

# 拆包
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

# * 处理不确定元素, 可以在任意位置
a, b, *rest = range(5)
print(a)
a, *rest, b = range(2)
print(b)
