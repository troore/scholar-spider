#coding=utf-8

import urllib
import re
import string
import urllib2

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getHtml403(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    req = urllib2.Request(
        url = url,
        headers = req_header
        )
    resp = urllib2.urlopen(req)
    html = resp.read()
    return html

def getTitle(html, lst):
#    reg = r'src="(.+?\.jpg)" pic_ext'
#    reg = r'<span id="art-abs-title-[0-9]+">(.*)</span>'
    reg = r'<span class="title" itemprop="name">([^<]+\.)</span>'
    body = re.compile(reg)
    urltlst = re.findall(body, html)
#    x = 0
    cnt = 0
    for ttl in urltlst:
     #   print ttl
        strinfo = re.compile(' ')
        b = strinfo.sub('+', ttl)
     #   print b
        lst.append([b, 0])
    #    urllib.urlretrieve(imgurl,'%s.jpg' % x)
    #    x+=1

def getCiteN(lst):
    template = "http://scholar.glgoo.org/scholar?q=TITLE"

    glgoo= "http://scholar.glgoo.org/scholar?q=8Gbps+high-speed+I%2FO+transmitter+with+scalable+speed%2C+swing+and+equalization+levels&btnG=&hl=zh-CN&as_sdt=0%2C5"
#    glgoo = "http://www.mit.edu"
    html = getHtml403(glgoo)
 
#    reg = r'<a href=".*">被引用次数：([0-9]+)</a>'
    reg = r'<div id="gs_ftr" role="([a-z]+)" style="display:none;">'
#    reg = r'<a href="http://ieeexplore\.ieee\.org/xpls/ab\s_all\.jsp\?arnumber=[0-9]+" data-clk=".*">([a-zA-Z ]+)</a>'
    body = re.compile(reg)
    citelst = re.findall(body, html)
#    print citelst
    for cite in citelst:
        print cite
    
#    for entry in lst:
#        glgoo = string.replace(template, 'TITLE', entry[0])
    #    print glgoo
#        html = getHtml403(glgoo)
#        reg = r'<a href=".*">被引用次数：([0-9]+)</a>'
#        reg1 = r'<a href="http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=[0-9]+" data-clk=".*">([a-zA-Z ]+)</a>'
#        body = re.compile(reg)
#        body1 = re.compile(reg1)
#        citelst = re.findall(body, html)
#        ttllist = re.findall(body1, html)
#        print ttllist
#        if (len(citelst) > 0 and len(ttllist) > 0):
#            print ttllist[0]
#            print entry[0]
#            if (entry[0] == ttllist[0]):
#                entry[1] = int(citelst[0])
#            else:
#                entry[1] = int(entry[1])
#        else:
#            entry[1] = int(entry[1])
            
     #   print entity
   #     for cite in citelst:
   #         print cite

def mycmp(x, y):
    return cmp(x[1], y[1])

if __name__ == '__main__':

    blanklist = []
    ttllist = []
    citelist = []
    
#    urls = ["http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=10415&filter%3DAND%28p_IS_Number%3A33077%29&pageNumber=1",
#            "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=10415&filter%3DAND%28p_IS_Number%3A33077%29&pageNumber=2",
#            "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=10415&filter%3DAND%28p_IS_Number%3A33077%29&pageNumber=3",
#            "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=10415&filter%3DAND%28p_IS_Number%3A33077%29&pageNumber=4",
#            "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4062990&filter%3DAND%28p_IS_Number%3A4062991%29&pageNumber=1",
#             "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4062990&filter%3DAND%28p_IS_Number%3A4062991%29&pageNumber=2",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4062990&filter%3DAND%28p_IS_Number%3A4062991%29&pageNumber=3",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4062990&filter%3DAND%28p_IS_Number%3A4062991%29&pageNumber=4",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4540056&filter%3DAND%28p_IS_Number%3A4545405%29&pageNumber=1",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4540056&filter%3DAND%28p_IS_Number%3A4545405%29&pageNumber=2",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4540056&filter%3DAND%28p_IS_Number%3A4545405%29&pageNumber=3",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4540056&filter%3DAND%28p_IS_Number%3A4545405%29&pageNumber=4",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=1",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=2",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=3",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=4",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=1",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=2",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=3",
#              "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4632904&filter%3DAND%28p_IS_Number%3A4641463%29&pageNumber=4",
 #             "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5379508&filter%3DAND%28p_IS_Number%3A5397993%29&pageNumber=1",
 #             "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5379508&filter%3DAND%28p_IS_Number%3A5397993%29&pageNumber=2",
 #             "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5379508&filter%3DAND%28p_IS_Number%3A5397993%29&pageNumber=3",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5379508&filter%3DAND%28p_IS_Number%3A5397993%29&pageNumber=4",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5379508&filter%3DAND%28p_IS_Number%3A5397993%29&pageNumber=5",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5379508&filter%3DAND%28p_IS_Number%3A5397993%29&pageNumber=6",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6076821&filter%3DAND%28p_IS_Number%3A6085068%29&pageNumber=1",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6076821&filter%3DAND%28p_IS_Number%3A6085068%29&pageNumber=2",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6076821&filter%3DAND%28p_IS_Number%3A6085068%29&pageNumber=3",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6076821&filter%3DAND%28p_IS_Number%3A6085068%29&pageNumber=4",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6387373&filter%3DAND%28p_IS_Number%3A6398324%29&pageNumber=1",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6387373&filter%3DAND%28p_IS_Number%3A6398324%29&pageNumber=2",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6387373&filter%3DAND%28p_IS_Number%3A6398324%29&pageNumber=3",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6387373&filter%3DAND%28p_IS_Number%3A6398324%29&pageNumber=4",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6745905&filter%3DAND%28p_IS_Number%3A6749643%29&pageNumber=1",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6745905&filter%3DAND%28p_IS_Number%3A6749643%29&pageNumber=2",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6745905&filter%3DAND%28p_IS_Number%3A6749643%29&pageNumber=3",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6937053&filter%3DAND%28p_IS_Number%3A6948870%29&pageNumber=1",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6937053&filter%3DAND%28p_IS_Number%3A6948870%29&pageNumber=2",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6937053&filter%3DAND%28p_IS_Number%3A6948870%29&pageNumber=3",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6937053&filter%3DAND%28p_IS_Number%3A6948870%29&pageNumber=4",
 #       "http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=6937053&filter%3DAND%28p_IS_Number%3A6948870%29&pageNumber=5",
 #       ]

    urls = ["http://dblp.uni-trier.de/db/conf/socc/socc2010.html"]
#    urls = [" http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=10415&filter%3DAND%28p_IS_Number%3A33077%29&pageNumber=1"]
   

    for url in urls:
        html = getHtml(url)
    #    getTitle(html, blanklist)
        getTitle(html, ttllist)

#    print blanklist

#    f = open("database.dat", 'w')
#    for entry in blanklist:
#        f.write("%s %s\n" % (entry[0], entry[1]))
#    f.close()

#    f = open("database.dat", 'r')
#    while True:
#        line = f.readline()
#        if not line: break
#        line = line.replace('\n', '')
    #    print line
#        ttllist.append(line.split(' '))
#    f.close()
        
#    print ttllist

    getCiteN(ttllist)

#    ttllist.sort(mycmp, reverse=True)
    ttllist.sort(lambda x, y:cmp(x[1], y[1]), reverse=True)   

    f = open("cite.dat", 'w')
    for entry in ttllist:
    #    print entry
        f.write("%s %s\n" % (entry[0], entry[1]))
    f.close()

    

#    f = open("cite.dat", 'r')
#    while True:
#        line = f.readline()
#        if not line: break
#        line = line.replace('\n', '')
        #    print line
#        citelist.append(line.split(' '))
#    f.close()

#    for entry in citelist:
#        entry[1] = int(entry[1])
#    citelist.sort(mycmp, reverse=True)
#    citelist.sort(lambda x, y:cmp(x[1], y[1]), reverse=True)
    #    ttllist.sort(mycmp)    

#    for entry in citelist:
#        print entry
