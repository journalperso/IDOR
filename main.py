import requests

with requests.session() as s:
    i = 0
    while True:
        response = s.get("http://testasp.vulnweb.com/showthread.asp?id=%s" % (str(i)))
        if "admin" in response.text:
            print(response.url)
        i += 1
