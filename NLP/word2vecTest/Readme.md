
# 安装gensim

```
pip install gensim  

```

[维基语料](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)

[英文语料数据](http://mattmahoney.net/dc/text8.zip)

[腾讯新闻语料](http://download.csdn.net/download/shmei_cool/4788802)

# 步骤

##   合并txt

腾讯新闻数据解压后是很多txt文件，需要进入cmd命令，进入解压后的文件中，确定目录无误后，输入“type *.txt >>f:\wiki.cn.txt”，该命令将把当前目录下的所有txt文件的内容输出到f:\wiki.cn.txt，然后把文件命名为wiki.cn.text,和后续步骤保持一致。具体操作见http://jingyan.baidu.com/article/d3b74d64a7cf671f77e609b5.html


##   将xml的文件转换成txt文件
如果用维基百科数据，需要转化成txt；如果用腾讯新闻数据，直接跳过这步
```
python process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.cn.text

```

得到**wiki.cn.text**

##  繁体转成简体


###    opencc windows

1.进入opencc文件中

2.把简繁转换的源文件（例如是深蓝词库转换出来的无拼音纯简体字文档）放在D:\opencc目录下，假设是sc.txt

2.打开命令提示符，进入D:\opencc目录

3.键入`opencc -i wiki.cn.text -o wiki.cn.text.jian -c t2s.json`（也可键入“opencc --help”参阅详细命令说明）

4.转换后的文档就是 **wiki.cn.text.jian**，同样在D:\opencc目录下




##  结巴分词

```
python separate_words.py wiki.cn.text.jian wiki.cn.text.jian.seq 
```
得到**wiki.cn.text.jian.seq**


**如果遇到“'gbk' codec can't decode byte 0x80 in position 0”错误，修改separate_words.py**

```
output = open(outp, 'w')
    inp = open('f:\\wiki.cn.text', 'rb')

    for line in inp.readlines():
        seg_list = jieba.cut(str(line).encode(encoding='utf_8'))
        output.write(space.join(seg_list) + '\n')
```        
##  去除多余的其他字符

```
python remove_words.py wiki.cn.text.jian.seq wiki.cn.text.jian.removed
```
得到**wiki.cn.text.jian.removed**


##  训练模型

```
python train_word2vec_model.py wiki.cn.text.jian.removed wiki.en.text.jian.model wiki.en.text.jian.vector
```
其中**wiki.en.text.jian.model**是我们训练出来的模型

## 模型测试

```
python test_model.py
```



