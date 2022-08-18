#!/usr/bin/env python3

# Author: Jesus Cuenca

# JSON DBs are based on records distributed on JSON files
# Each file has this structure (to simplify parsing with different tools):
# dict -> register -> dict
# So, to access name field...
# row[0].name 

# Basic operations of interest are...
# - select columns (fields) - create column filters with select_fields(),
#   then apply the filter with map()
# - select rows (by field value)

from json import JSONDecoder
import sys
# with open
# json.load

# !!!! get fields from command line
fields=["name", "vm"]

def filterDict(d,keys):
    return {k:v  for k,v in d.items() if k in keys}

def select_fields(fields):
    def filter(d):
        return filterDict(d,fields)
    return filter

def toMDRow(list):
    return " | ".join([" "] + list + [" "])

def toList(dict):
    return [str(dict[k]) for k in dict]

input = []
stdin = sys.stdin.read().lstrip()
decoder = JSONDecoder()

while len(stdin) > 0:
    obj, bytes_read = decoder.raw_decode(stdin)
    stdin = stdin[bytes_read:].lstrip()
    input.append(obj)

rows=list((map(lambda x: list(x.values())[0],input)))

col_filter=select_fields(fields)

print(toMDRow(fields))
for r in (map(col_filter,rows)):
    print(toMDRow(toList(r)))


