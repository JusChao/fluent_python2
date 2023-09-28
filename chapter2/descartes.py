# 推导式
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']

mix = [[color, size] for color in colors for size in sizes]
print(type(mix))

# 生成式
mix = ([color, size] for color in colors for size in sizes)
print(type(mix))
