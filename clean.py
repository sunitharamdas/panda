import csv

filename = "file0.txt"
text = open(filename, 'r')
lines = text.readlines()
Newlines = []
temp = None
a = len(lines)
for i in lines:
        temp = str(i)
        temp1 = temp.replace('||', '|')
        Newlines.append(temp1)
for row in Newlines:
        print(row,end="")














