# -*- coding: utf-8 -*-
import requests

# =============================================================================
# url = "http://localhost:8080/D:/scalab/SC1/test1.txt"
# =============================================================================
d_url = "http://localhost:8005/"
l_url = "http://localhost:8082/"
url = "http://localhost:"
unlock_url = "http://localhost:8082/unlock/"

#filename = "test1.txt"
#durl = d_url+filename

menu = input("1.Read File / 2.Write file : ")
if menu == '1':
  filename = input("Enter File Name: ")
  durl = d_url+filename
  response = requests.get(durl)
  print("Response = " + response.text)
  
  port = response.text[0:4]
  print ("port = "+port)
  path = response.text[4:]
  print("path = " + path)
  furl = url + port +"/"+path
  
  response = requests.get(furl)
  print("Text Data:")
  print(response.text)
else:
  filename = input("Enter File Name: ")
  #access directory server
  durl = d_url+filename
  response = requests.get(durl)
  print(response.text)
  
  port = response.text[0:4]
  print (port)
  path = response.text[4:]
  print(path)
  furl = url + port +"/"+path
  
  #access lock server
  lurl = l_url+filename
  resp_lock = requests.get(lurl)
  print("Lock Status: "+resp_lock.text)
  unlockurl = unlock_url+filename
  
  if resp_lock.text == "0":
    writelock = requests.post(lurl)
    #access file server
    sinp = input("input data: ")
    writeresp = requests.post(furl, data = sinp)
    print(writeresp.text)
    writeunlock = requests.post(unlockurl)
    print("lock status"+writeunlock.text)
  else:
    print("The file is currenly locked by another user")
