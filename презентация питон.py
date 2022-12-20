from PIL import Image
from PIL import Image, ImageDraw
from moviepy.editor import *
import os
def video():
    directory = 'C:/Users/student/Documents/милые котята'
    files = os.listdir(directory)
    images = list(filter(lambda x: x.endswith('.jpg'), files))
    clips = [ImageClip(m).set_duration(2) for m in images]

    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile('test.mp4', fps=24)


def m():

    im = Image.new('RGB', (200,200), color=('#AFEEEE'))
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (200,200),
        'cute cats',
        fill=('#1C0606')
    )
    im.save()


a=input()
if a==1:
    video()
elif a==2:
    m()
    
