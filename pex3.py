def pex3():
    '''
    Answer: linkedlist
    '''
    import re
    file = open('pex3.txt')
    text = file.read()
    pattern = re.compile('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')
    return re.findall(pattern, text)
