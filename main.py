file = open('input', 'r')
sonardata = []
for i in file:
    sonardata.append(int(i))

n = 0
count = 0
evaluation = 0
while n < len(sonardata) - 2:
    previous = evaluation
    evaluation = sonardata[n] + sonardata[n + 1] + sonardata[n + 2]
    if previous < evaluation and previous != 0:
        count += 1
    n += 1
print("count:", count)
