# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 17:27:29 2017

@author: acer
"""
import web
class mywebclass(web.application):
  def run(self, port=8080, *middleware):
    function1 = self.wsgifunc(*middleware)
    return web.httpserver.runsimple(function1,('0.0.0.0',port))