#import interface.main
import program.refresh

main_file = program.refresh.refresh_file()

for i in range(len(main_file)):
    print(main_file[i])