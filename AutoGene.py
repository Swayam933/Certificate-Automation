from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import csv

df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',70)
font1 = ImageFont.truetype("./MLSJN.TTF",110)
for index,j in df.iterrows():
    img = Image.open('as.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1300,1200),text='{}'.format(j['name']),fill=(24,19 ,0),font=font1)
    draw.text(xy=(860,1830),text='SYNERGINA',fill=(0,0,0),font=font)
    draw.text(xy=(2120,1830),text='28/03/2021',fill=(0,0,0),font=font) #Change-Daily
    img.save('pictures/{}.pdf'.format(j['name']))

