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
    def Audio_Process(self,mp3path,num):
        y, sr = librosa.load(mp3path,sr=None)
        time = librosa.get_duration(filename='./result.mp3')
        #tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        #beat_times = list(librosa.frames_to_time(beats, sr=sr))
        #beat_times.append(beat_times[-1] + 1)
        a = time/num
        b = []
        for i in range(num):
            b.append(i*a)
        return b

if __name__ == '__main__':
    num=32
    mp3='C:\\Users\\Administrator\\PycharmProjects\\GenVIdeo\\src\\result.mp3'
    Audio_Process().Audio_Process(mp3,32)