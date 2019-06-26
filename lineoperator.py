def add_music(author, track, username):
    file = []
    with open('musicline.txt', 'r') as f:
        num = int(f.readline().strip())
    if num > 10:
        num = 10
        file = []
        with open('musicline.txt', 'r') as f:
            file = f.readlines()
        with open('musicline.txt', 'w') as f:
            f.write('10')
            for i in file[1:]:
                f.write(i)
        with open('musicline.txt', 'a') as f:
            f.write('@'+username + ': ' + str(num) + '. ' + author + ' - ' + track + '\n')
            num += 1
    else:
        with open('musicline.txt', 'a') as f:
            f.write('@'+username + ': ' + str(num) + '. ' + author + ' - ' + track + '\n')
            num += 1
        file = []
        with open('musicline.txt', 'r') as f:
            file = f.readlines()
        with open('musicline.txt', 'w') as f:
            f.write(str(num) + '\n')
            for i in file[1:]:
                f.write(i)
