import http.client

conn = http.client.HTTPConnection("api.reverieinc.com")
ldstr = "भूपेन"
payload = "{\"inArray\":[%s],\"REV-APP-ID\":\"rev.web.com.rev.master\",\"REV-API-KEY\":\"9757f28c968b561ea36ffbea2ff562679148\",\"webSdk\":0}"%(ldstr.encode('cp1252'))

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "84de87db-ddfc-7d16-1315-7c41836525a0"
    }

conn.request("POST", "/parabola/reverseTransliterateSimple", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))