# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:50:22 2017

@author: acer
"""

import web
import mywebclass
import shelve

urls = (
  '/unlock/(.*)', 'unlock_class',
  '/(.*)', 'index' 
  
)


class index:
    def GET(self, filename):
      try:
        print(filename)
        shelve1 = shelve.open("lock.dat")
        (lockstat) = shelve1[filename]
      finally:
        shelve1.close()
      print("Status = ",lockstat)
      return lockstat
    
    def POST(self, filename):
      try:
        print(filename)
        shelve1 = shelve.open("lock.dat")
        (lockstat) = shelve1[filename]
        if lockstat == "0":
          shelve1[filename]="1"
      finally:
        shelve1.close()
      print("Status = ",lockstat)
      return lockstat
    
class unlock_class:
    
    def POST(self, filename):
      try:
        print(filename)
        shelve1 = shelve.open("lock.dat")
        (lockstat) = shelve1[filename]
        if lockstat == "1":
          shelve1[filename]="0"
          (lockstat) = shelve1[filename]
      finally:
        shelve1.close()
      print("Status = ",lockstat)
      return lockstat
    
    


if __name__ == "__main__":
    #app = web.application(urls, globals())
    app = mywebclass.mywebclass(urls, globals())
    app.run(port = 8082)