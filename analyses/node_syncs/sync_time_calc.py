import re

with open("CA_16GB_6CPU_delta.csv") as file:
    content = file.readlines()

def parseblock(line):
    return int(re.match(r".*:\d\d.\d\d\d, (.*),", line).group(1))

def parsetimedt(line):
    return int(float(re.match(r".*, (.*)", line).group(1)))


block_index = 1000
block_over = block_index
timesum = 0

for i in range(0, len(content)):
    timesum += parsetimedt(content[i])
    if parseblock(content[i]) > block_over:
        print(str(parseblock(content[i])) + ", " + str(parsetimedt(content[i])))
        block_over += block_index
        timesum = 0