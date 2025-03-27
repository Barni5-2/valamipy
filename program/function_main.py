import class_main

def read_file(path):
    f = open(path, "r", encoding="UTF8")
    a = []
    for i in f:
        a.append(i)
    return a

def format_file(path):
    f = open(path, "r", encoding="UTF8")
    a = []
    for i in f:
        a.append(class_main.MusicData(i))
    return a
