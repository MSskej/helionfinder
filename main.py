import re

f = open("strona.html", encoding="utf8")


x = re.findall(r"\bprice=\"[1-9][0-9]\...?\"", f.read())

print(x)

f.close()