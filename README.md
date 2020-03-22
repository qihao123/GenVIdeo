# GenVIdeo
一种基于python编写的视频自动生成程序<br>
<h2>一、想要设计的功能：</h2>
<h3>1、文字转视频</h3>
 任意输入或者利用爬虫爬取一段文字语料，首先将其生成音频，然后将这段音频生成视频并添加字幕。<br>
 音频中可加入各种声效，视频可换任意背景图<br>
<h3>2、音频转视频</h3>
输入一段音频，语音识别生成文字，然后生成对应的字幕视频。<br>
<h3>3、快速生成动态排名数据可视化视频</h3>
将[Historical-ranking-data-visualization-based-on-d3.js](https://github.com/Jannchie/Historical-ranking-data-visualization-based-on-d3.js)
项目运行利用python截取网页屏幕，将图片串成视频。
<h3>4、快速生成图片字幕类视频</h3>
输入文字，图片， 音频，快速生成视频。
<br>
<br>
<h2>二、目前需要的python依赖：</h2>
moviepy,pymysql,json,jieba,urllib,librosa,uuid,datatime,baidu-aip<br>
(有些依赖比较难装，我装了好久QAQ，有问题可以给我发邮件哦)