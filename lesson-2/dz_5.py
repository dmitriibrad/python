a = [57.8, 46.51, 97, 13.99, 2.56, 46.30, 80, 19, 10, 7.12]
a = sorted(a)

print(id(a))
b = []

for i in a:
    if type(a[a.index(i)]) == float:
        meaning = str(a[a.index(i)])
        r, kk = meaning.split('.')
        r = int(r)
        kk = int(kk)
        if r <= 9:
            if kk <= 9:
                b.append(f'«0{r} руб 0{kk} коп»')
            else:
                b.append(f'«0{r} руб {kk} коп»')
        else:
            if kk <= 9:
                b.append(f'«{r} руб 0{kk} коп»')
            else:
                b.append(f'«{r} руб {kk} коп»')
    elif type(a[a.index(i)]) == int:
        r = a[a.index(i)]
        kk = 00
        if r <= 9:
            b.append(f'«0{r} руб 0{kk} коп»')
        else:
            b.append(f'«{r} руб 0{kk} коп»')

b = sorted(b)
print(b)
c = sorted(b, reverse=True)
print(c)
b = b[5:]
print(b)
