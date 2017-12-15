# -*- coding: utf-8 -*-
import requests

d_url = "http://localhost:8005/"
# =============================================================================
# url = "http://localhost:8080/D:/scalab/SC1/test1.txt"
# =============================================================================
url = "http://localhost:"

filename = "test1.txt"
durl = d_url+filename

# =============================================================================
# menu = input("1.Read File / 2.Write file")
# if menu == '1':
# =============================================================================
response = requests.get(durl)
print(response.text)

port = response.text[0:4]
print (port)
path = response.text[4:]
print(path)
furl = url + port +"/"+path

response = requests.get(furl)
print(response.text)
# =============================================================================
# else:
#   sinp = input("input data: ")
#   writeresp = requests.post(url, data = sinp)
#   print(writeresp.text)
# =============================================================================
