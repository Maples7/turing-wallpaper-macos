import os
import datetime

from PIL import Image, ImageFilter

PDF_SOURCE = '/Users/maples7/wallpapers/images/{:04d}.jpg'
BACKGROUND_SOURCE = '/Users/maples7/wallpapers/wallpaper.jpg'

PAGE_OFFSET = 7
MARGIN_LEFT = 400
MARGIN_TOP = 400

current_week = datetime.datetime.now().isocalendar()[1]
OUTPUT = '/Users/maples7/Pictures/wallpaper-{}.png'.format(current_week)
page = PAGE_OFFSET + current_week

calendar = Image.open(PDF_SOURCE.format(page))
background = Image.open(BACKGROUND_SOURCE)
calendar = calendar.convert('RGBA')
background = background.convert('RGBA')

# datas = calendar.getdata()
# newData = list()
# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# calendar.putdata(newData)
# calendar = calendar.filter(ImageFilter.DETAIL)

# calendar.save('tmp.png')

background.paste(calendar, (MARGIN_TOP, MARGIN_LEFT))
background.save(OUTPUT)

os.system(''' 
osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{0}"' 
'''.format(OUTPUT))

print('Executed at {0}'.format(str(datetime.datetime.now())))

# with Image(filename=PDF_SOURCE.format(page), resolution=300) as calendar:
#     calendar.format = 'png'
#     # with Color('#fff') as white:
#     #     for row in calendar:
#     #         for col in row:
#     #             if col == white:
#     #                 calendar.colorspace = Color('#fff0')
#     with Image(filename=BACKGROUND_SOURCE) as background:
#         background.composite_channel('default_channels', calendar, 'blend', MARGIN_LEFT, MARGIN_TOP)
#         background.save(filename=OUTPUT)
