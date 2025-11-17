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
main_count = {}
for i in l:
    main_count[i] = main_count.get(i, 0) + 1
for i, j in sorted(main_count.items(), key = lambda x: -x[1])[:3]:
    print(i)
