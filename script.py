import PIL.Image

# ascii character used to build the output text
ASCII_CHARS = ['@', '%', '#', '*', '+', ';', '-', ':', ',', '.', ' ']
# ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

# resize image according to a new width
def resize_image(image, new_width=600):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert('L')
    return (grayscale_image)


# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ''.join(ASCII_CHARS[pixel//25] for pixel in pixels)
    return (characters)

# attempt to open image from user-input
def main(new_width=600):
    path = input('Enter the path of the image: ')
    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'is not a valid path to image file')
    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    # format
    pixels_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixels_count, new_width))

# print ASCII image
    print(ascii_image)

# save result to 'ascii_image.txt'
    with open('ascii_image.txt', 'w') as f:
        f.write(ascii_image)

main()