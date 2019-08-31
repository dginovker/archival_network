import re
from datetime import datetime

"""
Calculates the time difference in ms between logs (created _delta files)
"""

with open("TOKYO_sync_192GB_32CPU.csv") as file:
    content = file.readlines()


def milliseconds(content):
    return datetime.strptime(re.match(r"(.*),.*", content + "000").group(1), "%Y-%m-%d %H:%M:%S.%f").timestamp()*1000


for i in range(1, len(content)):
    diff = milliseconds(content[i]) - milliseconds(content[i-1])
    print(content[i].split("\n")[0] + ", " + str(diff))
