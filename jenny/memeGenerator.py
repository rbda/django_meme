from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from django.utils.datetime_safe import datetime
from django.utils.text import slugify


def make_meme(title, filename, top_string="", bottom_string=""):
    img = Image.open(filename)
    image_size = img.size
    font_size = int(image_size[1] / 5)
    font = ImageFont.truetype("/Library/Fonts/Impact.ttf", font_size)
    top_text_size = font.getsize(top_string)
    bottom_text_size = font.getsize(bottom_string)
    while top_text_size[0] > image_size[0] - 20 or bottom_text_size[0] > image_size[0] - 20:
        font_size = font_size - 1
        font = ImageFont.truetype("/Library/Fonts/Impact.ttf", font_size)
        top_text_size = font.getsize(top_string)
        bottom_text_size = font.getsize(bottom_string)

    top_text_position_x = (image_size[0] / 2) - (top_text_size[0] / 2)
    top_text_position_y = 0
    top_text_position = (top_text_position_x, top_text_position_y)

    bottom_text_position_x = (image_size[0] / 2) - (bottom_text_size[0] / 2)
    bottom_text_position_y = image_size[1] - bottom_text_size[1]
    bottom_text_position = (bottom_text_position_x, bottom_text_position_y)

    draw = ImageDraw.Draw(img)

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
    img.filename = filename_slug
    return img
