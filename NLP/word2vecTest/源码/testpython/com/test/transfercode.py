# -*- coding:utf-8 -*-
'''
@author: fightingliu
'''
import sys
import string
import codecs
import os
import shutil

import string
import codecs
def changecode():
    tt=codecs.open('f:\\wiki.cn.text','rb')  #111.txt为unicode编码文件，以unicode编码打开，utf-16=unicode
    mm=open('f:\\wiki.cn.text.jian','wb')
    ff=tt.readlines()
    
    for i in ff:
        print(i)
        mm.write(str(i).encode('UTF-8'))
   
    tt.close
    mm.close

def checkyes():
    nn=open('f:\\wiki.cn.text.jian','rb')
    nnff=nn.readlines()
    nn.close()
    if nnff[-1]=='123':
        print ("finish")
    
changecode()