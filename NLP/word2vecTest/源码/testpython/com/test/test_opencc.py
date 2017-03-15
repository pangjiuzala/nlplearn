# -*- coding:utf-8 -*-
'''

@author: liuxing
'''
# opencc 繁体字转为简体
import opencc
cc = opencc.OpenCC('t2s') 
target="f:\\wiki.cn.text.jian"
fname="f:\\wiki.cn.text"
f = open(target,'w')
for line in open(fname).readlines():
       l= cc.convert(line)
       f.write(str(l)+'\n')
f.close()
print(len(open(target).readlines()))