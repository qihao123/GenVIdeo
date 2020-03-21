# coding=utf-8

from DataBase import DataBase
from CutWorld import CutWorld
from TextToAudio import TextToAudio
from Audio_Process import Audio_Process
from Gen_Video import Gen_Video

'''

'''

class run():
    def __init__(self):
        pass
    def get_word(self):
        '''
        从数据库获取一条未生成视频的语料
        :return: text
        '''
        text = DataBase().get_word()
        return text
    def run(self):
        text,uuid = self.get_word()
        wordlist = CutWorld().CutWorld(text)
        audio = TextToAudio().TextToAudio(text)
        beat_info = Audio_Process().Audio_Process(audio)
        Gen_Video().Gen_Video(beat_info,wordlist,audio,uuid)

if __name__ == '__main__':
    run().run()
