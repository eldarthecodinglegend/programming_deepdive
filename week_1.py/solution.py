import sys
input = sys.argv[1]
list = list(input)
sum = 0
for i in list:
    sum += int(i)
print(sum)
