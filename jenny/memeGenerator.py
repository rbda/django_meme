from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from django.utils.datetime_safe import datetime
from django.utils.text import slugify


def make_meme(title, filename, top_string="", bottom_string=""):
    img = Image.open(filename)
    image_size = img.size

    # find biggest font size that works
    font_size = int(image_size[1] / 5)
    font = ImageFont.truetype("/Library/Fonts/Impact.ttf", font_size)
    top_text_size = font.getsize(top_string)
    bottom_text_size = font.getsize(bottom_string)
    while top_text_size[0] > image_size[0] - 20 or bottom_text_size[0] > image_size[0] - 20:
        font_size = font_size - 1
        font = ImageFont.truetype("/Library/Fonts/Impact.ttf", font_size)
        top_text_size = font.getsize(top_string)
        bottom_text_size = font.getsize(bottom_string)

    # find top centered position for top text
    top_text_position_x = (image_size[0] / 2) - (top_text_size[0] / 2)
    top_text_position_y = 0
    top_text_position = (top_text_position_x, top_text_position_y)

    # find bottom centered position for bottom text
    bottom_text_position_x = (image_size[0] / 2) - (bottom_text_size[0] / 2)
    bottom_text_position_y = image_size[1] - bottom_text_size[1]
    bottom_text_position = (bottom_text_position_x, bottom_text_position_y)

    draw = ImageDraw.Draw(img)

    # draw outlines
    # there may be a better way
    outline_range = int(font_size / 15)
    for x in range(-outline_range, outline_range + 1):
        for y in range(-outline_range, outline_range + 1):
            draw.text((top_text_position[0] + x, top_text_position[1] + y), top_string, (0, 0, 0),
                      font=font)
            draw.text((bottom_text_position[0] + x, bottom_text_position[1] + y), bottom_string,
                      (0, 0, 0), font=font)

    draw.text(top_text_position, top_string, (255, 255, 255), font=font)
    draw.text(bottom_text_position, bottom_string, (255, 255, 255), font=font)

    filename_slug = slugify(title + "-" + str(datetime.now()))
    filename_slug = filename_slug + ".png"
    # img.save(filename_slug)
    img.filename = filename_slug
    return img


# def get_upper(somedata):
#     '''
#     Handle Python 2/3 differences in argv encoding
#     '''
#     result = ''
#     try:
#         result = somedata.decode("utf-8").upper()
#     except:
#         result = somedata.upper()
#     return result
#
#
# def get_lower(somedata):
#     '''
#     Handle Python 2/3 differences in argv encoding
#     '''
#     result = ''
#     try:
#         result = somedata.decode("utf-8").lower()
#     except:
#         result = somedata.lower()
#
#     return result


# if __name__ == '__main__':
#
#     args_len = len(sys.argv)
#     top_string = ''
#     meme = 'standard'
#
#     if args_len == 1:
#         # no args except the launch of the script
#         print('args plz')
#
#     elif args_len == 2:
#         # only one argument, use standard meme
#         bottom_string = get_upper(sys.argv[-1])
#
#     elif args_len == 3:
#         # args give meme and one line
#         bottom_string = get_upper(sys.argv[-1])
#         meme = get_lower(sys.argv[1])
#
#     elif args_len == 4:
#         # args give meme and two lines
#         top_string = get_upper(sys.argv[-2])
#         bottom_string = get_upper(sys.argv[-1])
#         meme = get_lower(sys.argv[1])
#     else:
#         # so many args
#         # what do they mean
#         # too intense
#         print('to many argz')
#
#     print(meme)
#     filename = str(meme) + '.jpg'
#     make_meme(top_string, bottom_string, filename)
