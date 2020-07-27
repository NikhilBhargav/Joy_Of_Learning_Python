# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:37:00 2020

Parsing of XML in Python
@author: Nikhil Bhargava
"""
import xml.etree.ElementTree as ET
data ='''
<person>
<name>Nikhil</name>
<phone>+91 991 006 3200</phone>
<email hide="yes"/>
</person>
'''
tree=ET.fromstring(data)
print('Name:',tree.find('name').text)
print('Attr:',tree.find('email').get('hide'))      



