
import jieba
import sys
import importlib
importlib.reload(sys)

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
    def CutWorld(self,text,uuid):
        with open(uuid+'.txt', 'w',encoding='utf-8-sig') as f:
            seg_list = jieba.lcut(text)
            punct = set(''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒
            ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠
            々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻
            ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…/\\''')
            word_list = list(filter(lambda x: x not in punct, seg_list))
            for word in word_list:
                f.write(word+'\n')
            f.close()
            return len(word_list)+1
if __name__ == '__main__':
    text ='3月9日某某访问某某'
    uuid= '1'
    CutWorld().CutWorld(text,uuid)