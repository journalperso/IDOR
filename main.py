import requests

with requests.session() as s:
    for i in range(0, 200):
        response = s.get("http://testasp.vulnweb.com/showthread.asp?id=%s" % (str(i)))
        if "admin" in response.text:
            print(response.url)
