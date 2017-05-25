#!/anaconda/bin/python
import math

with open("HeatmapSCNdata.csv") as infile, open("HeatmapSCNlogdata.csv", 'w') as outfile:
    lines = []
    for line in infile:
        if line.startswith("Gene"):
            outfile.write(line)
        else:
            for x in line:
                try int(x):
                    lines.append(log(float(x)))
                else:
                    continue
    print(lines)
