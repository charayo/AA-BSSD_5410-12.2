
from PIL import Image, ImageOps
import math


def convolve(img, sz, step):
    # if the pixels are an odd size, we need a whole number
    start = math.floor(sz / 2)
    con_pixels = []
    for x in range(start, img.size[0] - 1, step):
        for y in range(start, img.size[1] - 1, step):
            # top row
            tl = img.getpixel((y - 1, x - 1))
            tc = img.getpixel((y - 1, x))
            tr = img.getpixel((y - 1, x + 1))

            # center row
            lc = img.getpixel((y, x - 1))
            cc = img.getpixel((y, x))
            rc = img.getpixel((y, x + 1))

            # bottom row
            bl = img.getpixel((y + 1, x - 1))
            bc = img.getpixel((y + 1, x))
            br = img.getpixel((y + 1, x + 1))

            sum = tl * 3 + tc * 10 + tr * 3 + lc * 0 + cc * 0 + rc * 0 + bl * -3 + bc * -10 + br * -3
            div = 1
            y_ave = math.floor(sum / div)

            sum = tl * 3 + tc * 0 + tr * -3 + lc * 10 + cc * 0 + rc * -10 + bl * 3 + bc * 0 + br * -3
            div = 1
            x_ave = math.floor(sum / div)

            sum = tl*-3 + tc*-10 + tr*-3 + lc*0 + cc*0 + rc*0 + bl*3 + bc*10 + br*3
            div = 1
            n_y_ave = math.floor(sum / div)
            #
            sum = tl*-3 + tc*0 + tr*3 + lc*-10 + cc*0 + rc*10 + bl*-3 + bc*0 + br*3
            div = 1
            n_x_ave = math.floor(sum / div)

            ave = 0
            if y_ave > 0:
                ave = math.floor(y_ave)
            if n_y_ave > 0:
                ave = math.floor(n_y_ave)
            if x_ave > 0:
                ave = math.floor(x_ave)
            if n_x_ave > 0:
                ave = math.floor(n_x_ave)
            con_pixels.append(ave)
    # our new image is smaller than original and needs to be a whole number
    dims = (math.floor(img.size[0] / step) - 1, math.floor(img.size[1] / step) - 1)
    output = Image.new('L', dims)
    print(len(con_pixels))
    output.putdata(con_pixels)
    output.show()


# end def convolve (img, sz, step):


def main():
    og_image = Image.open("demo.png")
    # convert to grayscale
    gray_image = ImageOps.grayscale(og_image)
    # open original for comparison
    gray_image.show()
    # kernel size of 3x3
    convolve(gray_image, 3, 2)


# end def main):


if __name__ == "__main__":
    main()
