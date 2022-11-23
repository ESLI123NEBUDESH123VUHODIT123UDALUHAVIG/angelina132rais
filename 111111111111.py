from PIL import Image, ImageDraw, ImageFont
def meretin(t,x,y,n):
    im = Image.new('RGB', (x,y), color=('#1FCECB'))
    font = ImageFont.truetype(
        'C:/Windows/Fonts/times.ttf',
                          size=100)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (30,480),
        t,
        font=font,
        fill=('#1C0606')
        )
    im.save('C:C:/Users/student/Desktop/презентация'+str(n)+'.jpg')

t=['СубханАллахи\n'
   'ва\n'
   'бихамдихи\n'
   'адада\n'
   'халкихи\n'
   'ва\n'
   'ридда\n'
   'нафсихи\n'
   'ва\n'
   'зинита\n'
   'аршихи\n'
   'ва\n'
   'мидада\n'
   'калиматихи\n',]

for i in range(15):
    meretin(t[i],1000,1000,i)
