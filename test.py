import re

def find_url(file):
    i = 1
    url = "-"
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            print(line)
            if 'https:' in line:
                url=i
            i+=1
    print(url)

find_url('test.txt')