# coding=utf-8
import librosa
'''
音频处理类
处理TTs后的音频文件，生成鼓点信息，配合语料显示
传入音频path
输出鼓点信息
Time:2020/03/07 18:48
Author:@qh
'''

class Audio_Process():
    def __init__(self):
        pass
    def Audio_Process(self,mp3path):
        y, sr = librosa.load(mp3path,sr=None)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = list(librosa.frames_to_time(beats, sr=sr))
        beat_times.append(beat_times[-1] + 1)
        return beat_times