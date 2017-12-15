# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:13:34 2017

@author: acer
"""

import web
import shelve
import mywebclass

urls = (
  '/(.*)', 'index'
)

class index:
    def GET(self, filename):
      try:
        print(filename)
        shelve1 = shelve.open("mydict.dat")
        (port,filepath) = shelve1[filename]
      finally:
        shelve1.close()
      fullfilepath = str(port)+str(filepath)
      print(fullfilepath)
      return fullfilepath

    
if __name__ == "__main__":
# =============================================================================
#     app = web.application(urls, globals())
# =============================================================================
    app = mywebclass.mywebclass(urls, globals())
    app.run(port = 8005)