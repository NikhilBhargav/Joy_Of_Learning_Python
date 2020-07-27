# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:58:47 2020
JSON in python
@author: Nikhil Bhargava
"""
import json
data='''{
"name":"Nikhil",
"phone":{
  "type":"intl",
  "number":"+91 991 006 32000"
},
"email":{
  "hide":"yes"
}
}
'''

info=json.loads(data)
print('Name: ',info['name'])
print('Email Hidden: ',info['email']["hide"])

                            
