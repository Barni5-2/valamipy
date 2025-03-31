def refresh_file():
    f = open("data/data.txt", "r", encoding="UTF8")
    l = []
    for i in f:
        l.append(i)
    f.close()
    return l