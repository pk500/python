import re
my_data=open("data.txt").read()
print sum(list(map(int,re.findall("[0-9]+",my_data))))

