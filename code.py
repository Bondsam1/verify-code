#创建四个英文字母的验证码


from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
def create_verify_code(squ):
    width=squ*4+10
    height=squ+20
    im=Image.new('RGB',(width,height),'white')
    def rndChar():
        return chr(random.randint(65,90))
    def rndColorLight():
        return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
    def rndColorDark():
        return (random.randint(0,64),random.randint(0,64),random.randint(0,64))
    font=ImageFont.truetype('Arial.ttf',squ)
    draw = ImageDraw.Draw(im)
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndColorLight())
    for t in range(4):
        draw.text((squ*t+10,10),rndChar(),font=font,fill=rndColorDark())
    im=im.filter(ImageFilter.BLUR)
    im.save('code.jpg','jpeg')
if __name__=='__main__':
    create_verify_code(int(input('plz enter the length of one character: ')))
