# orig src : screenbloom
# https://github.com/kershner/screenBloom/blob/d89d3cf9655ee4b10cd1151d8b307665f69a88b2/app/modules/img_proc.py#L103

from PIL import ImageEnhance
from PIL import ImageGrab


LOW_THRESHOLD = 10
MID_THRESHOLD = 40
HIGH_THRESHOLD = 240


# Return avg color of all pixels and ratio of dark pixels for a given image
def img_avg(img):
    dark_pixels = 1
    mid_range_pixels = 1
    total_pixels = 1
    r = 1
    g = 1
    b = 1

    # Win version of imgGrab does not contain alpha channel
    if img.mode == 'RGB':
        img.putalpha(0)

    # Create list of pixels
    pixels = list(img.getdata())

    for red, green, blue, alpha in pixels:
        # Don't count pixels that are too dark
        if red < LOW_THRESHOLD and green < LOW_THRESHOLD and blue < LOW_THRESHOLD:
            dark_pixels += 1
        # Or too light
        elif red > HIGH_THRESHOLD and green > HIGH_THRESHOLD and blue > HIGH_THRESHOLD:
            pass
        else:
            if red < MID_THRESHOLD and green < MID_THRESHOLD and blue < MID_THRESHOLD:
                mid_range_pixels += 1
                dark_pixels += 1
            r += red
            g += green
            b += blue
        total_pixels += 1

    n = len(pixels)
    r_avg = r / n
    g_avg = g / n
    b_avg = b / n
    rgb = [r_avg, g_avg, b_avg]

    # If computed average below darkness threshold, set to the threshold
    for index, item in enumerate(rgb):
        if item <= LOW_THRESHOLD:
            rgb[index] = LOW_THRESHOLD

    rgb = (rgb[0], rgb[1], rgb[2])

    data = {
        'rgb': rgb,
        'dark_ratio': float(dark_pixels) / float(total_pixels) * 100
    }
    return data


# Grabs screenshot of current window, calls img_avg (including on zones if present)
def screen_avg():
    screen_data = {}
    img = ImageGrab.grab()

    # Resize for performance - this could be a user editable setting
    size = (16, 9)
    img = img.resize(size)

    # Enhance saturation according to user settings
    #sat_scale_factor = float(_screen.sat)
    #if sat_scale_factor > 1.0:
    #    sat_converter = ImageEnhance.Color(img)
    #    img = sat_converter.enhance(sat_scale_factor)

    screen_data = img_avg(img)
    return screen_data
