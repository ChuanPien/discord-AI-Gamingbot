# -*- coding: utf-8 -*-
import json, os
from time import sleep

def line_to_dict(split_Line):
    # Assumes that the first ':' in a line
    # is always the key:value separator

    print(split_Line)

    
    line_dict = {}
    key, value = split_Line.split("=", maxsplit=1)

    print(key, value)

    line_dict[key] = value

    return line_dict

def convert2(filename) :
    f = open(f"{filename}", "r",encoding='utf8')
    content = f.read()
    splitcontent = content.splitlines()

    for ch in splitcontent:
        if '' in splitcontent:
            splitcontent.remove('')

    # Split each line by pipe
    lines = [line.split(' = ') for line in splitcontent]

    #for del_nonestr in splitcontent:

    # Convert each line to dict
    lines = [line_to_dict(l) for l in splitcontent]

    # Output JSON 
    with open(f"{filename[:-4]}.json", 'w',encoding='utf8') as fout:
        json.dump(lines, fout, indent=4,ensure_ascii=False)


for filename in os.listdir("./"):
    if filename.endswith('.txt'):
        print(filename)
        convert2(filename)
        sleep(1)