def pex4(x):
    '''
    for i in link:
	sth = pex4(link[-1])
	link.append(sth)
	print(link)

    Answer: peak.html 
    '''
    import urllib.request as url
    import re
    link = []
    f = url.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x)
    text = f.read()
    f.close()
    pattern = re.compile(b'[0-9]+')
    pattern2 = re.compile('[0-9]+')
    num = re.findall(pattern, text)
    a = ''
    for i in num:
        a = str(i)
    link = re.findall(pattern2, a)

    return link[0]
