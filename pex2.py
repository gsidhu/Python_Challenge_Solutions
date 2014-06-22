## Python Challenge Solutions
## MIT License, 2014 Gurjot S. Sidhu


def pex2():
    '''
    Answer: equality
    '''
    import string
    file = open('pex2.txt')
    line = file.read()
    key = list(line)
    alpha = list(string.ascii_letters)
    ans = []
    for i in key:
        if i in alpha:
            ans.append(i)
    file.close()
    return ans
