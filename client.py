# -*- coding: utf-8 -*-
import requests
import shelve
from requests.auth import HTTPBasicAuth
# =============================================================================
# url = "http://localhost:8080/D:/scalab/SC1/test1.txt"
# =============================================================================
d_url = "http://localhost:8005/"
l_url = "http://localhost:8082/"
url = "http://localhost:"
unlock_url = "http://localhost:8082/unlock/"
login_url = "http://localhost:8083/"

#filename = "test1.txt"
#durl = d_url+filename
print("a.login / b.signup : ")
inp_a = input("enter a/b:")
if inp_a == "a":
  username = input("Enter Username: ")
  password = input("Enter Password: ")
  auth1= requests.get('http://localhost:8083/', auth=HTTPBasicAuth(username, password))
  #print("Authorization: "+auth1.text)
  if auth1.text == "Not Authorized!":
    print("Sorry "+auth1.text )
  else:
    print(auth1.text)
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

elif inp_a == "b":
  user1 = input("Enter USername:")
  pass1 = input("Enter Password:")
  try:
    shelve1 = shelve.open("login.dat")
    shelve1[user1] = (pass1)
  except:
    shelve1.close()
      
  
  
