import PIL.Image
import numpy as np
import hashlib
import random
import os
import datetime

def read_image(image_path):
    """
    read RGB numpy array for the input image
    :param image_path: input image pass
    :return: RGB numpy array
    """
    return np.array(PIL.Image.open(image_path))

def flatten_image(image_array):
    """
    flatten a x*y*3 3D image numpy array to a 1D array
    :param image_array: RGB numpy array
    :return: 1D RGB numpy array
    """
    image_x, image_y = image_array.shape[0], image_array.shape[1]
    return image_array.reshape([1, image_x * image_y * 3])[0]

def code_image_embed(image_1d_array, code_array):
    """
    embed the code array into the rgb array
    :param image_1d_array: 1D RGB numpy array
    :param code_array: processed code array
    :return: code embeded 1D RGB numpy array
    """
    image_code_array = []
    for i in range(len(code_array)):
        if image_1d_array[i] >= code_array[i]:
            image_code_array.append(image_1d_array[i] - code_array[i])
        else:
            image_code_array.append(image_1d_array[i] + code_array[i])

    return image_code_array

def extract_code(image_array, image_code_array):
    """
    extracted embedded code from the image code array
    :param image_array: original 1D RBG numpy array
    :param image_code_array: code embeded 1D RGB numpy array
    :return: code array
    """
    return np.abs(np.subtract(image_array, image_code_array))

def save_image(image_processed_array, export_path, image_size):
    """
    save the code embeded 1D RGB numpy as a png image
    :param image_processed_array: image array to be saved
    :param image_size: list of image x and y
    :param export_path: path for the output image
    :return: None
    """
    image_export = np.asarray(image_processed_array)\
        .reshape([image_size[0], image_size[1], 3]).astype(np.uint8)
    im = PIL.Image.fromarray(image_export, 'RGB')
    im.save(export_path, quality=100)

def read_code(code_path):
    """
    read code to be encrypted as a plain text file
    :param code_path: code path
    :return: code in text format
    """
    code_text = {}

    if os.path.isfile(code_path):
        code_text[code_path] = "".join(list(open(code_path).readlines()))
    elif os.path.isdir(code_path):
        for code in os.listdir(code_path):
            if os.path.isfile(os.path.join(code_path, code)):
                code_text[code] = "".join(list(open(os.path.join(code_path, code)).readlines()))
    return str(code_text)

def save_code(code_str, export_path):
    """
    create a folder in the expath path and save all codes to the folder
    :param code_str: code string to be save
    :param export_path: export path
    :return: None
    """
    code_text = eval(code_str)
    export_folder = "codimage-{}".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    export_folder = os.path.join(export_path, export_folder)

    if not os.path.isdir(export_folder):
        os.mkdir(export_folder)

    for i in code_text.keys():
        with open(os.path.join(export_folder, i), 'w') as file:
            file.write(code_text[i])

def convert_acsii(text):
    """
    convert input text or number into a list of acsii code
    :param text: text or number
    :return: list of acsii code for each digit / character in the input
    """
    return [ord(i) for i in str(text)]

def convert_cnt_digit(int_list):
    """
    given a list of integers, i.e. [10, 213], convert each element in the list into
    [number of digits, digit 1...] structure. example list will be converted into [2,1,0,3,2,1,3]
    which [2,1,0] represents 10 and [3,2,1,3] represents 213
    :param int_list: list of integers
    :return: digit list
    """
    digit_list = []
    for num in int_list:

        num = str(num)
        num_len = len(num)
        digit_list.append(num_len)

        for i in range(num_len):
            digit_list.append(int(num[i]))
    return digit_list

def convert_int_list(digit_list):
    """
    given a digit list, convert it back to int list
    :param digit_list: digit list
    :return: integer list
    """
    code_str = []

    acsii_len = None
    acsii_code = ""
    acsii_counter = 0
    for i in digit_list:
        if not acsii_len:
            acsii_len = i
            acsii_code = ""
            acsii_counter = 0
        else:
            acsii_code += str(i)
            acsii_counter += 1

            if acsii_counter == acsii_len:
                code_str.append(int(acsii_code))
                acsii_len = None
    return code_str

def list_padding(lst, target_length, fill_with=0):
    """
    pad a list with 0 (by default) to a given length
    :param lst: list to be padded
    :param target_length: target length for the padded list
    :param fill_with: element to pad
    :return: padded list
    """
    return lst + [fill_with] * (target_length - len(lst))

def convert_md5(text):
    """
    return md5 encode for a given text
    :param text: text to convert to md5
    :return: md5 encode
    """
    return hashlib.md5(text.encode()).hexdigest()

def shuffle(lst, key):
    """
    implementation of Fisher-Yates algorithm with a key to shuffle a list
    :param lst: list to be shuffled
    :param key: shuffle key
    :return: shuffled list
    """
    random.seed(key)
    swap_list = [random.randint(0, len(lst) - 1) for _ in range(len(lst))]
    for i in range(len(lst)):
        to_swap = swap_list[i]
        lst[i], lst[to_swap] = lst[to_swap], lst[i]
    return lst

def shuffle_reverse(lst, key):
    """
    reverse the shuffled list with the original key
    :param lst: shuffled list
    :param key: shuffle key
    :return: original list
    """
    random.seed(key)
    swap_list = [random.randint(0, len(lst) - 1) for _ in range(len(lst))]
    for i in range(len(lst) - 1, -1, -1):
        to_swap = swap_list[i]
        lst[i], lst[to_swap] = lst[to_swap], lst[i]
    return lst