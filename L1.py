from collections import *
import requests
r = requests.get("https://dfedorov.spb.ru/python3/sport.txt")
text = r.content.decode('cp1251')
l = []
for i in text.split('\n'):
    counter = 0;
    for j in i.split('\t'):
        if counter % 7 == 3:
            for word in j.split(','):
                if word != '':
                    l.append((word.lower()).strip())
        counter += 1;
l = l[1:]
c = Counter(l)
for i in c.most_common(3):
    print(i[0])
