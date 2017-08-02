arr = { 'Москва':'Питер', 'Алматы':'Саратов', 'Балашиха':'Красногорск', 'Питер':'Алматы', 'Саратов':'Сызрань', 'Сызрань':'Балашиха'}

def path(d):
    first = ''
    res = []

    for city in d:
        if city not in d.values():
            first = city
    res.append(first)

    current = first
    for i in range(len(d)):
        current = d[current]
        res.append(current)

    return res

path(arr)
