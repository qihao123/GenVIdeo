# coding=utf-8
from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
'''
视频生成类
生成1280X720的视频
传入音频鼓点，分词后的语料，音频地址，语料id
Time：2020/03/07 18:42
Author:@qh

Time:2020/03/07
bug:
1、中文语料无法插入到视频中
编码问题待解决
2、音频的beat_info不准确需要重新计算
'''

class Gen_Video():
    def __init__(self):
        pass
    def Gen_Video(self,beat_times,word_list,mp3path,uuid):
        clips = []
        for index, beat_time in enumerate(beat_times[:-1]):
            if index >= len(word_list):
                break
            print(f'{index + 1}/{len(beat_times)}——{word_list[index]}')
            text_clip = TextClip(
                word_list[index].encode('utf-8'),
                fontsize=320 // 8,
                color='white',
                size=(320, 640),
                method='caption',
                font='msyhbd.ttc') \
                .set_start(beat_time) \
                .set_end(beat_times[index + 1])
            text_clip = text_clip.set_pos('center')
            clips.append(text_clip)
        final_clip = CompositeVideoClip(clips)
        audio_clip = AudioFileClip(mp3path)
        final_video = final_clip.set_audio(audio_clip)
        final_video.write_videofile(
            str(uuid) + '.mp4',
            fps=30,
            codec='mpeg4',
            preset='ultrafast',
            audio_codec="libmp3lame",
            threads=4)