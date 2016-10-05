#!/usr/bin/python
def output4():
    print 'guan'

if __name__ == '__main__':
    import re
    import urllib

    def getImg(url):
        r = r'<img src="(.{1,100}\.jpg)"'
        rc = re.compile(r)
        return re.findall(rc, urllib.urlopen(url).read())

    img = getImg("http://image.baidu.com/")
    for k in range(len(img)):
        print k + 1, ':', img[k]
        urllib.urlretrieve(img[k], "%s.jpg" % k)