# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:02:57 2017

@author: acer
"""

import shelve

fname = input("filename: ")
fpath = input("filepath: ")
fport = input("port: ")

shelve1 = shelve.open("mydict.dat", writeback=True)
#finalfile = fpath + fname
shelve1[fname] = (fport, fpath)
shelve1.close()

###########
fname = input("filename: ")
lockstat = "0"

shelve2 = shelve.open("lock.dat", writeback=True)
shelve2[fname] = (lockstat)
shelve2.close()

###########
uname = input("Username: ")
pwd   = input("Password: ")

shelve3 = shelve.open("login.dat", writeback=True)
shelve3[uname] = (pwd)
shelve3.close()