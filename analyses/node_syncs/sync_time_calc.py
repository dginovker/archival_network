import re

with open("SNG_128GB_24CPU_delta.csv") as file:
    content = file.readlines()

def parseblock(line):
    return int(re.match(r".*:\d\d.\d\d\d, (.*),", line).group(1))

def parsetimedt(line):
    return int(float(re.match(r".*, (.*)", line).group(1)))


blocks_per_datapt = 10000
block_over = blocks_per_datapt
timesum = 0

for i in range(0, len(content)):
    timesum += parsetimedt(content[i])
    if parseblock(content[i]) > block_over:
        print(str(parseblock(content[i])) + ", " + str(parsetimedt(content[i])))
        block_over += blocks_per_datapt
        timesum = 0
