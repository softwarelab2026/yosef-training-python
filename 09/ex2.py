import urllib.request

URL = "https://www.picshare.co.il/s_pictures/img56489.jpg"
FILE_NAME = r"/home/yosef/clones/yosef-training-python/09/image1.jpg"

with urllib.request.urlopen(URL) as response:
    image = response.read()

    with open(FILE_NAME, 'wb') as output_file:
        output_file.write(image)


