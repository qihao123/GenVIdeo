import os.path
from pathlib import Path
from moviepy.editor import AudioFileClip

'''
音乐分离类

传入视频地址&视频名，想保存的音频地址&音频名（默认与视频同目录且同名）
Time：2021/04/21 21:38
Author:@qh
'''


class Audio_Visual_Separation:

    def __init__(self):
        self.Video_Path = ''
        self.Video_Name = ''
        self.Audio_Path = ''
        self.Audio_Name = ''

    @staticmethod
    def _path_check(path):
        """
        文件地址检验函数
        :param path:文件地址，或文件所在文件夹地址
        :return: 存在该地址或者存在该文件夹则返回True，否则返回False
        """
        FileName = Path(path)
        if FileName.exists():
            return True
        elif FileName.is_file():
            return True
        elif FileName.is_dir():
            return True
        else:
            return False

    def Audio_Visual_Separation(self, Video_Path, Video_Name, Audio_Path=None, Audio_Name=None):
        """
        音频分离函数
        首先检查地址是否存在，默认只需要视频地址和视频名称，音频默认存放之视频地址下
        视频是MP4格式，音频默认是MP3格式
        :param Video_Path:视频地址
        :param Video_Name: 视频名
        :param Audio_Path: 音频地址
        :param Audio_Name: 音频名称
        :return: 分离好的音频
        """
        self.Video_Path = Video_Path
        self.Video_Name = Video_Name
        if Audio_Path is not None:
            self.Audio_Path = Audio_Path
        else:
            self.Audio_Path = Video_Path
        if Audio_Name is not None:
            self.Audio_Name = Audio_Name
        else:
            self.Audio_Name = Video_Name.replace(".mp4", ".mp3")
        if self._path_check(self.Video_Path + self.Video_Name):
            if self._path_check(self.Audio_Path):
                __video_path = self.Video_Path + self.Video_Name
                __audio_path = self.Audio_Path + self.Audio_Name
                my_audio_clip = AudioFileClip(__video_path)
                my_audio_clip.write_audiofile(__audio_path)
            else:
                print('error! :audio file path cant find')
        else:
            print('error! :video file or file path cant find')


if __name__ == '__main__':
    """
    test
    """
    video_path = '../Lib/lib_video/'
    video_name = 'example_video1.mp4'
    Audio_Visual_Separation = Audio_Visual_Separation()
    Audio_Visual_Separation.Audio_Visual_Separation(video_path, video_name, Audio_Path='./')
