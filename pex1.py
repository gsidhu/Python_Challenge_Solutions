## Python Challenge Solutions
## MIT License, 2014 Gurjot S. Sidhu


def pex1():
    '''
    Answer: ocr
    '''
    import string
    alpha = list(string.ascii_lowercase)
    alpha.extend(['a', 'b'])
    cin = input("String: ")
    cin_alpha = list(cin)
    answer = []
    for i in cin:
        if i in string.ascii_lowercase:
            alpha_index = alpha.index(i)
            answer.append(alpha[alpha_index+2])
        else:
            answer.append(i)
    return ''.join(answer)
