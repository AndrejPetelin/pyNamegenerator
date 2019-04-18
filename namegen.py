import random
import sys


def reader(filename):
    ret = []
    with open(filename) as f:
        for line in f:
            ret.append(line.rstrip())
    return ret


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python nameGen.py <dictionary file>")
    else:
        dic = reader(str(sys.argv[1]))
        print(random.choice(dic) + ' ' + random.choice(dic))




        
