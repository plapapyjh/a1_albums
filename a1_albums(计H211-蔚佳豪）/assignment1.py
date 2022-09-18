"""
Replace the contents of this module docstring with your own details
Name: 蔚佳豪
Date started: 2022.9.18
GitHub URL: git@github.com:plapapyjh/a1_albums.git
"""

"""
Album stored as (Title, Artist, Year, Required)
"""
REQUIRED = 'r'
COMPLETED = 'c'
MENU = """Menu:
L - List all albums
A - Add new album
M - Mark an album as completed
Q - Quit
>>> """

TIP = "Albums 1.0 - by 蔚佳豪"

POSITIVE = 'Number must be > 0'

BLANK = 'Input can not be blank'

INVALID = 'Invalid menu choice'

ALBUM_0 = 'No albums left to listen to. Why not add a new album?'

def menu():
    print(MENU, end='')
    choice = input().lower().strip()
    while len(choice) >=2 or choice not in 'mqla':
        print(INVALID)
        print(MENU, end='')
        choice = input().lower().strip()
    return choice

def integer(string):
    if string.startswith('-'):
        string = string[1:]
    for i in range(len(string)):
        flag=1
        for j in range(10):
            if(string[i]==str(j)):
                flag=0
        if flag == 1:
            return None
    return int(string[i])

def getpositiveint(string='>>> '):
    print(string, end='')
    while True:
        token = input()
        if integer(token) is None:
            print('Invalid input; enter a valid number')
        else:
            tok = int(token)
            if tok <=0:
                print(POSITIVE)
            else:
                return int(token)
        print(string, end='')

def getblankinput(string):
    print(string,end='')
    while True:
        token = input()
        if(token != ''):
            break
        print(BLANK)
        print(string,end='')
    return token

def getcount(album):
    sum=0
    for music in album:
        if music[3] == REQUIRED:
            sum+=1;
    return sum

def printls(album):

    ls1 = [len(music[0]) for music in album]
    ls2 = [len(music[1]) for music in album]
    max_title = max(ls1)
    max_artist = max(ls2)
    cnt = 1
    for title, artist, year, required in album:
        test = (required == REQUIRED)
        if test:
            print("*",end="")
        else:
            print(" ",end="")
        print(cnt, '. ', title.ljust(max_title), ' by ', artist.ljust(max_artist), ' (', year, ')', sep='')
        cnt += 1

def listalbum(album):
    printls(album)
    count = getcount(album)
    test = (count == 0)
    if test:
        print(ALBUM_0)
    else:
        print('You need to listen to', end=' ')
        print(count, end=' ')
        print('albums.')

def checkandlist(album):
    num = getcount(album)
    test = (num == 0)
    if  test:
        print('No required albums')
        return
    listalbum(album)
    print('Enter the number of an album to mark as completed')

def markalbum(album):
    checkandlist(album)
    choice = getpositiveint()
    u = album[choice - 1][3]
    test = (u == REQUIRED)
    if test:
        album[choice - 1][3] = COMPLETED
        print('You listened to', album[choice - 1][0], 'by', album[choice-1][1])
    else:
        print('You have already listened to', album[choice - 1][0])

def sortalbum(album,title,artist,year):
    album.append([title, artist, year, REQUIRED])
    album.sort(key=lambda x: (x[1], x[0]))

def getinput():
    title = getblankinput('Title: ')
    artist = getblankinput('Artist: ')
    year = getpositiveint('Year: ')
    return (title,artist,year)
def addalbum(album):
    (title,artist,year) = getinput()
    sortalbum(album,title,artist,year)
    print(title, ' by ', artist, ' (', year, ') added to Albums', sep='')

def readfile(filename):
    result = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            row = row.strip()
            if len(row) < 1:
                continue
            items = row.split(',')
            if len(items) == 4 and \
                len(items[0]) >= 1 and \
                    len(items[1]) >=1 and \
                        integer(items[2]) is not None and \
                            int(items[2]) > 0 and \
                                (items[3] == REQUIRED or items[3] == COMPLETED):
                result.append([items[0], items[1], int(items[2]), items[3]])
    print(len(result), 'albums loaded')
    result.sort(key=lambda x: (x[1], x[0]))
    return result

def writefile(filename, album):
    cnt = 0
    with open(filename, 'w') as f:
        for i in range(len(album)):
            if i != 0:
                f.write('\n')
            f.write(album[i][0]+','+album[i][1]+','+str(album[i][2])+','+album[i][3])
            cnt += 1
    print(cnt, 'albums saved to', filename)

def main():
    print(TIP)
    album = readfile('albums.csv')
    while True:
        user_input = menu()
        if user_input == 'a':
            addalbum(album)
        elif user_input == 'm':
            markalbum(album)
        elif user_input == 'l':
            listalbum(album)
        else:
            writefile('albums.csv', album)
            exit(0)

if __name__ == '__main__':
    main()