def sortFiles():
    files = []
    for i in range(1, 4):
        filename = f'{i}.txt'
        file = open(file=filename, encoding='utf8', mode='r')
        c = file.read()
        files.append((filename, c.count('\n') + 1, c))
    filesSorted =  sorted(files, key=lambda x: x[1])
    with open('result_file.txt', 'w', encoding='utf-8') as result:
        for i in range(len(filesSorted)-1, -1, -1):
            result.write(str(filesSorted[i][0])+ '\n' + str(filesSorted[i][1]) + '\n' + str(filesSorted[i][2]) + '\n')
            print('a')


sortFiles()