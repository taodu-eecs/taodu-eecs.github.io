from PIL import Image
import numpy as np
import sys

# Load image.
input_name = sys.argv[1]
input_image = Image.open(input_name)
pixels = np.array(input_image)

print(pixels.shape)
pixels = pixels[300:2200, :, :]

# Write image back.
output_name = sys.argv[2]
output_image = Image.fromarray(np.uint8(pixels))
output_image.save(output_name)