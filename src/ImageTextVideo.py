# coding=utf-8
from moviepy.editor import *
from moviepy.video.tools.credits import credits1
from moviepy.editor import CompositeVideoClip, AudioFileClip
'''
生成图片字母类视频
传入一段文字，一张图片，一段音频生成字幕视频吗
'''

class ImageTextVideo():
    def __init__(self):
        self.imagepath = ""
        self.textpath = ""
        self.musicpath = ""
        self.name = "final"
    def genVideo(self):
        #加载一个图片clip
        clip = [ImageClip(self.imagepath)]

        # 用一个文本文件内容生成字幕
        #credits = credits1('../../credits/credits.txt', 3 * clip.w / 4)
        credits = credits1(self.textpath, 3 * clip.w / 4)
        scrolling_credits = credits.set_pos(lambda t: ('center', -10 * t))

        # 添加音频
        audio = AudioFileClip(self.musicpath)

        final = CompositeVideoClip([clip,
                                    scrolling_credits])
        final_video = final.set_audio(audio)
        final_video.write_videofile(
            str(self.name) + '.mp4',
            fps=30,
            codec='mpeg4',
            preset='ultrafast',
            audio_codec="libmp3lame",
            threads=4)
