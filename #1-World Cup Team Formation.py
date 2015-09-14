# pay attention on: how to read the input file from the standardized format!

x = []
for n in range(10):
    x.append(int(raw_input().strip()))
y = 0
for n in range(3):
    large = max(x)
    x.remove(large)
    second_large = max(x)
    x.remove(second_large)
    y += large
print(y)