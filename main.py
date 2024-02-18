import re

f = open("strona.html", encoding="utf8")

text = f.read()


ceny = re.findall(r"\bprice=\"([1-9][0-9]\...?)\"", text)
tytuly = re.findall(r'aria-hidden="true">(.+?)</a>', text)

ksiazki = list(zip(tytuly, ceny))

for tytul, cena in ksiazki:
    print("Tytuł:", tytul)
    print("Cena:", cena)
    print()

f.close()

