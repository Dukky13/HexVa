import math
import os

def get_size_and_txt(filee):
    with open(filee, "rb") as f:
        global txt
        global tamanho
        f.seek(0)
        txt = f.read() 
        tamanho = f.tell()

def calcular_n_pixeis_e_tamanho_de_imagem():
    global pixels
    global side
    global width
    global height
    pixels = math.ceil(tamanho / 3)
    side = math.ceil(math.sqrt(pixels))
    width = side
    height = side

def calc_padding():
    global bytes_per_width_or_height
    global padding
    global bytes_per_line
    global pixel_data_size
    bytes_per_width_or_height = side * 3
    padding = (4 - (bytes_per_width_or_height % 4)) % 4
    bytes_per_line = width * 3 + padding
    pixel_data_size = bytes_per_line * height

def calc_size_of_file():
    global file_size
    file_size = 54 + pixel_data_size

def write_new_file():
    with open("image.bmp", "wb") as f:

        f.write(b"BM")
        f.write(file_size.to_bytes(4, "little"))

        f.write(b"\x00\x00")
        f.write(b"\x00\x00")

        f.write((54).to_bytes(4, "little"))
        f.write((40).to_bytes(4, "little"))

        f.write(width.to_bytes(4, "little"))
        f.write(height.to_bytes(4, "little"))

        f.write((1).to_bytes(2, "little"))
        f.write((24).to_bytes(2, "little"))

        f.write((0).to_bytes(4, "little"))

        f.write(pixel_data_size.to_bytes(4, "little"))

        f.write((2835).to_bytes(4, "little"))
        f.write((2835).to_bytes(4, "little"))

        f.write((0).to_bytes(4, "little"))
        f.write((0).to_bytes(4, "little"))

        i = 0

        for y in range(height):

            for x in range(width):

                pixel = txt[i:i+3]
                i += 3

                if len(pixel) < 3:
                    pixel += b"\x00" * (3 - len(pixel))

                f.write(pixel)

            f.write(b"\x00" * padding)

print("Please input the name of your file")
print(os.system('ls'))
print('\n')
file_name = input("> ")
get_size_and_txt(file_name)
calcular_n_pixeis_e_tamanho_de_imagem()
calc_padding()
calc_size_of_file()
write_new_file()

with open("image.bmp", "rb") as g:
    global tamanho2
    g.seek(0)
    g.read()
    tamanho2 = g.tell()

os.system('clear')
print(f"File name: {file_name}")
print(f"Size: {tamanho2} bytes")
print(f"Pixels: {pixels}")
print(f"Dimension: {width}x{height}")
