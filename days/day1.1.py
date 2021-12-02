sonardata = open('../inputs/input1', 'r')
n = 0
count = 0
for line in sonardata:
    lineint = int(line)
    if n < lineint and n != 0:
        count += 1
    n = lineint

print(count)
