import numpy as np
from PIL import Image

arr1 = np.loadtxt('input.txt', dtype=np.uint8)
arr2 = np.loadtxt('output.txt', dtype=np.uint8)


img1= Image.fromarray(arr1, mode='L')  # 'L' indica imagem em escala de cinza
img2 = Image.fromarray(arr2, mode='L')

# Salvar a imagem
img1.save('imgs/input_image.png')
img2.save('imgs/output_image.png')

# Exibir a imagem
img1.show()
img2.show()