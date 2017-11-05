# Python2

import codecs

f = open("unvalidatedList.txt", "r")
o = open("outlist", "w+")

while True:
    line = f.readline()
    if not line: break
    line = line.decode('utf-8')
    line = line[0].upper() + line[1:-1]
    line = line.encode('utf-8')
    for i in range(0, 10):
        o.write(line + str(i) + '\n')
        for j in range(0, 10):
            o.write(line + str(i) + str(j) + '\n')
            for k in range(0, 10):
                o.write(line + str(i) + str(j) + str(k) + '\n')
                for l in range(0, 10):
                    o.write(line + str(i) + str(j) + str(k) + str(l) + '\n')
                    # print(line)

f.close()
o.close()