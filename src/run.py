# coding=utf-8

from src.DataBase import DataBase
from src.CutWorld import CutWorld
from src.TextToAudio import TextToAudio
from src.Audio_Process import Audio_Process
from src.Gen_Video import Gen_Video

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
