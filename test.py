import urllib2
url="http://scholar.glgoo.org/scholar?q=Support+for+multiprocessor+synchronization+and+resource+sharing+in+system-on-programmable+chips+with+softcores"
req_header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = urllib2.Request(
    url = url,
    headers = req_header
    )
resp = urllib2.urlopen(req)
html = resp.read()
print(html)
