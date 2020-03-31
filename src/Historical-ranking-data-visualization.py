# coding=utf-8

'''
生成动态排名可视化视频
传入一个excel表格，传入一个配置的json
'''

import matplotlib.pyplot as plt
import numpy as np
from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy
import math
from operator import itemgetter
# duration 控制时间
duration = 5
#画图
#类别
xi = ["city1","city2","city3","city4","city5","city6","city7"]
#设置初始值
yi = [10,11,12,13,14,8,9]
#时间节点
ti=[2016,2017,2018,2019,2020]
#变化值
y1=[[10,11,12,13,14,8,9],[11,12,13,14,15,19,18],[12,13,14,15,19,16,20],[18,14,15,16,19,17,20],[17,16,13,15,16,14,20]]

def gen_xy(t):
    interlude = duration/len(ti)
    x = t%interlude
    n = math.floor(int(t/interlude))
    t1 = ti[n]
    m=5
    xx,yy = sortlist(n,m)
    xx = list(reversed(xx))
    yy = list(reversed(yy))
    return xx,yy,t1
def sortlist(n,m):
    xx = xi
    yy=y1[n]
    resultX=[]
    x =[]
    y = []
    resultY = list(reversed(np.sort(yy)))
    le = len(xi)
    for i in resultY:
        pos = yy.index(i)
        resultX.append(xx[pos])
    for i in range(m):
        x.append(resultX[i])
        y.append(resultY[i])
    return x,y

def make_frame_mpl(t):
    i = t/duration
    plt.cla()
    fig = plt.figure(figsize=(12.8,7.2))
    xx,yy,t1 = gen_xy(t)
    plt.barh(xx, yy)
    plt.title(str(t1)+"years")
    plt.yticks(xx)
    #fig = plt.figure(figsize=(7.2,12.8))

    #plt.show()
    #print(fig)
    return mplfig_to_npimage(fig) # RGB image of the figure
def run():
    animation =mpy.VideoClip(make_frame_mpl, duration=duration)
    #animation.write_gif("sinc_mpl.gif", fps=20)
    animation.write_videofile("Historical_ranking_data_visualization_example.mp4",fps=24)

class HRDV():
    def __init__(self):
        pass

if __name__ == '__main__':
    run()
    #make_frame_mpl(0.1)
    #gen_xy(0.1)
    #sortlist(0,5)


'''
#测试用例
import moviepy.editor as mpy
import skimage.exposure as ske
import skimage.filters as skf
clip = mpy.VideoFileClip("sinc.gif")
gray = clip.fx(mpy.vfx.blackwhite).to_mask()
def apply_effect(effect, label, **kw):
    """ Returns a clip with the effect applied and a top label"""
    filtr = lambda im: effect(im, **kw)
    new_clip = gray.fl_image(filtr).to_RGB()
    txt = (mpy.TextClip(label, font="Amiri-Bold", fontsize=25,
        bg_color='white', size=new_clip.size)
        .set_position(("center"))
        .set_duration(1))
    return mpy.concatenate_videoclips([txt, new_clip])
def run():
    equalized = apply_effect(ske.equalize_hist, "Equalized")
    rescaled = apply_effect(ske.rescale_intensity, "Rescaled")
    adjusted = apply_effect(ske.adjust_log, "Adjusted")
    blurred = apply_effect(skf.gaussian, "Blurred", sigma=4)
    clips = [equalized, adjusted, blurred, rescaled]
    animation = mpy.concatenate_videoclips(clips)
    animation.write_gif("sinc_cat.gif", fps=15)
import numpy as np
import mayavi.mlab as mlab
import moviepy.editor as mpy
duration= 2 # duration of the animation in seconds (it will loop)
# MAKE A FIGURE WITH MAYAVI
fig_myv = mlab.figure(size=(220,220), bgcolor=(1,1,1))
X, Y = np.linspace(-2,2,200), np.linspace(-2,2,200)
XX, YY = np.meshgrid(X,Y)
ZZ = lambda d: np.sinc(XX**2+YY**2)+np.sin(XX+d)
# ANIMATE THE FIGURE WITH MOVIEPY, WRITE AN ANIMATED GIF
def make_frame(t):
    mlab.clf() # clear the figure (to reset the colors)
    mlab.mesh(YY,XX,ZZ(2*np.pi*t/duration), figure=fig_myv)
    #mlab.test_plot3d()
    f = mlab.gcf()
    f.scene._lift()
    arr = mlab.screenshot(antialiased=True)
    return arr
def run():
    animation = mpy.VideoClip(make_frame, duration=duration)
    animation.write_gif("sinc.gif", fps=20)
'''
