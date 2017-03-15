# -*- coding:utf-8 -*-
'''

@author: fightingliu
'''
#模型测试
import gensim

model = gensim.models.Word2Vec.load("f:\\wiki.en.text.jian.model")

result=model.most_similar(u'你')

for e in result:
    print(e[0],e[1])

