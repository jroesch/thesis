#!/usr/bin/env python3

import json
import sys

def json2tex(macroname, inf, outf):
    outf.write("\\def\\{}#1{{%\n".format(macroname))
    count = 0
    for key, value in sorted(json.load(inf).items()):
        count += 1
        outf.write("\\ifstrequal{{#1}}{{{}}}{{{}}}{{".format(
            key, value
        ))
    outf.write("\\errmessage{{unknown key for {}: #1}}".format(macroname))
    outf.write("}" * count + "}\n")

if __name__ == '__main__':
    json2tex(sys.argv[1], sys.stdin, sys.stdout)
