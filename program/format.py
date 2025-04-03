import program.data
def format_to_class(list):
    class_data = []
    for i in range(len(list)):
        class_data.append(program.data.MusicData(list[i]))
    return class_data