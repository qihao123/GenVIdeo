# coding=utf-8
import jieba

'''
分词模块
利用jieba分词对预料进行分析
返回分词后的列表
Time:2020/03/07 18:21
Author:@qh
'''
class CutWorld():
    def __init__(self):
        pass
    def CutWorld(self,text):
        seg_list = jieba.lcut(text)
        punct = set(''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
        ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
        々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
        ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…/\\''')
        word_list = list(filter(lambda x: x not in punct, seg_list))
        return word_list
