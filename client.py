# -*- coding: utf-8 -*-
import requests

url = "http://localhost:8080/D:/scalab/SC1/test1.txt"

response = requests.get(url)
print(response.text)

sinp = input("input data")
writeresp = requests.post(url, data = sinp)
print(writeresp.text)
