class MusicData:
    def __init__(self, raw):
        data = raw.split(";")
        self.rank = int(data[0])
        self.name = data[1]
        self.title = data[2]
        self.yturl = data[3].strip()