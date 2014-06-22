## Python Challenge Solutions
## MIT License, 2014 Gurjot S. Sidhu

def pex5():
    import pickle
    '''
    Unpickle the banner.p file in the source code and then "print the banner"

    Answer: channel
    '''
    f = open('banner.p', 'rb')
    stuff = pickle.load(f)
    for i in a:
            for j in range(0, len(i)):
                    if j == len(i)-1:
                            print(i[j][0]*i[j][1])
                    print(i[j][0]*i[j][1], end='')
