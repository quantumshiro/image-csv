import sys
import csv
from PIL import Image

args = sys.argv

# read Image file
image = Image.open(args[1])

# convert to grayscale
image = image.convert('L')
width, height = image.size

data = list(image.getdata())

with open(args[2]+'.csv', 'w', newline="") as csvfile:
    spamwriter = csv.writer(csvfile)
    
    x = 0
    for y in range(height):
        line_data = data[x:x+width]
        spamwriter.writerow(line_data)
        x += width