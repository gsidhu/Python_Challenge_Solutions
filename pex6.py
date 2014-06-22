## Python Challenge Solutions
## MIT License, 2014 Gurjot S. Sidhu

def pex6():
    '''
    Change URL to channel.zip and readme.txt
    Apparently textfiles inside zipfiles have comments you can extract

    answer: hockey -> oxygen
    '''

    import string
    import zipfile
    bob = []
    f = zipfile.ZipFile('channel.zip')
    filename = "90052.txt"
    while True:
        file = open(filename)
        txt = file.read()
        filename = txt[16:] + '.txt'
        if filename[0] not in string.digits:
            break
        bob.append(f.getinfo(filename).comment)
    chop = []
    for i in bob:
        chop.append(str(i).strip("b'"))
    for j in chop:
        if j == '\\n':
            print('')
        print(j, end = '')

