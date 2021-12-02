file = open('input', 'r')
sonardata = []
for i in file:
    sonardata.append(int(i))

n = 0
count = 0
sum = 0
while n < len(sonardata) and n != 1998:
    previous = sum
    sum = 0
    a = [sonardata[n], sonardata[n + 1], sonardata[n + 2]]
    for i in a:
        sum = sum + i
    if previous < sum and previous != 0:
        count += 1
    n += 1

print("count:", count)
