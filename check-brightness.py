from PIL import Image, ImageStat

im = Image.open("./new_test_image.jpg").convert("L")
stat = ImageStat.Stat(im).mean
print(stat[0]/255)