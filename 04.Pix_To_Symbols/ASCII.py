from PIL import Image, ImageFont, ImageDraw
from math import inf


def font_size(characters: str, size: tuple, font: str = 'arial'):
    def maximal_font_size(string):
        i = 1
        while True:
            font_ = ImageFont.truetype(font, i)
            exact_size = font_.getsize(string)
            if exact_size[0] > size[0] or exact_size[1] > size[1]:
                i -= 1
                break
            else:
                i += 1
        if i == 0:
            return False
        else:
            return i

    minimum = inf
    for char in characters:
        tmp = maximal_font_size(char)
        if not tmp:
            return False
        if tmp < minimum:
            minimum = tmp
    return minimum


def density_sorter(characters: str, font: str = 'arial', check_size: tuple = (50, 50)):
    def density_calculator(string):
        im = Image.new('RGB', check_size, (255, 255, 255))
        font_ = ImageFont.truetype(font, font_s)
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), string, (0, 0, 0), font=font_)

        load = im.load()
        counter = 0
        for i in range(check_size[0]):
            for j in range(check_size[1]):
                if load[i, j] != (255, 255, 255):
                    counter += 1
        return counter / (check_size[0] * check_size[1])

    font_s = font_size(characters, check_size, font)
    if not font_s:
        return False
    return ''.join(sorted(list(characters), key=density_calculator))


def picture_to_ascii_black_and_white(address: str, save_to: str, characters: str,
                                     divide=(10, 10), font='arial', scale=1, bg_color: int = 255):
    im = Image.open(address).convert('L')

    step_x, step_y = int(im.size[0]/divide[0]), int(im.size[1]/divide[1])
    if step_x == 0 or step_y == 0:
        raise ValueError('Divide is too big.')

    back = Image.new('L', (step_x*(divide[0] + 1), step_y*(divide[1] + 1)), 255)
    dif_x, dif_y = int((step_x*(divide[0] + 1) - im.size[0])/2), int((step_y*(divide[1] + 1) - im.size[1])/2)
    back.paste(im, (dif_x, dif_y, im.size[0] + dif_x, im.size[1]+dif_y))

    font_ = ImageFont.truetype(font, font_size(characters, (step_x*scale, step_y*scale), font))

    load = back.load()
    output = Image.new('L', (step_x*(divide[0] + 1) * scale, step_y*(divide[1] + 1) * scale), bg_color)
    draw = ImageDraw.Draw(output)
    for i in range(0, back.size[0], step_x):
        for j in range(0, back.size[1], step_y):
            summation = 0
            for k in range(i, i + step_x):
                for z in range(j, j + step_y):
                    summation += load[k, z]

            color = int(summation/(step_x * step_y))
            index = int(((255 - color)/255) * (len(characters) - 1))
            text_size = draw.textsize(characters[index], font_)
            dif_x, dif_y = int((step_x * scale - text_size[0])/2), int((step_y * scale - text_size[1])/2)
            draw.text((i * scale + dif_x, j * scale + dif_y), characters[index], font=font_, fill=color)


    output.save(save_to)


def picture_to_ascii_rgb(address: str, save_to: str, characters: str,
                                     divide=(10, 10), font='arial', scale=1, bg_color: tuple = (255, 255, 255)):
    im = Image.open(address).convert('RGB')

    step_x, step_y = int(im.size[0]/divide[0]), int(im.size[1]/divide[1])
    if step_x == 0 or step_y == 0:
        raise ValueError('Divide is too big.')

    back = Image.new('RGB', (step_x*(divide[0] + 1), step_y*(divide[1] + 1)), (255, )*3)
    dif_x, dif_y = int((step_x*(divide[0] + 1) - im.size[0])/2), int((step_y*(divide[1] + 1) - im.size[1])/2)
    back.paste(im, (dif_x, dif_y, im.size[0] + dif_x, im.size[1]+dif_y))

    font_ = ImageFont.truetype(font, font_size(characters, (step_x*scale, step_y*scale), font))

    load = back.load()
    output = Image.new('RGB', (step_x*(divide[0] + 1) * scale, step_y*(divide[1] + 1) * scale), bg_color)
    draw = ImageDraw.Draw(output)
    for i in range(0, back.size[0], step_x):
        for j in range(0, back.size[1], step_y):
            summation = [0, 0, 0]
            for k in range(i, i + step_x):
                for z in range(j, j + step_y):
                    summation[0] += load[k, z][0]
                    summation[1] += load[k, z][1]
                    summation[2] += load[k, z][2]

            color = [int(summation[ind]/(step_x * step_y)) for ind in range(3)]
            index = int(((255 - (sum(color)/3))/255) * (len(characters) - 1))
            text_size = draw.textsize(characters[index], font_)
            dif_x, dif_y = int((step_x * scale - text_size[0])/2), int((step_y * scale - text_size[1])/2)
            draw.text((i * scale + dif_x, j * scale + dif_y), characters[index], font=font_, fill=tuple(color))


    output.save(save_to)


