from utils import *
import os

class Codimage:

    @staticmethod
    def encrypt(image_path, code_path, export_path, password):
        """
        encrypt code into a image

        :param image_path: image path
        :param code_path: code path
        :param export_path: export image path
        :param password: password used for encryption
        :return: None
        """

        # read in original image
        image_array = read_image(image_path)
        image_x, image_y = image_array.shape[0], image_array.shape[1]
        image_1d_array = flatten_image(image_array)

        # read in code to be encrypted
        code = read_code(code_path)
        acsii_code = convert_acsii(code)
        code_digit_lst = convert_cnt_digit(acsii_code)

        code_digit_len = len(code_digit_lst)
        code_digit_len_lst = list_padding(convert_cnt_digit([code_digit_len]), 10)

        assert os.path.splitext(image_path)[1] == '.png', "Uploaded image must be png format"
        assert len(image_1d_array) >= code_digit_len + 138, "Uploaded image size is too small"

        # read in password
        password = convert_acsii(convert_md5(password))
        password_key = sum(password)
        password_lst = list_padding(convert_cnt_digit(password), 128)

        # shuffle the input list
        shuffle_key = password_key % code_digit_len
        print(code_digit_lst)
        print(shuffle_key)
        code_digit_lst = shuffle(code_digit_lst, shuffle_key)

        # append code length and password list behind
        code_digit_lst = list_padding(code_digit_lst, len(image_1d_array) - 138) + code_digit_len_lst + password_lst

        # compute export image array
        image_code_array = code_image_embed(image_1d_array, code_digit_lst)

        # export the image
        save_image(image_code_array, export_path, [image_x, image_y])

    @staticmethod
    def decrypt(original_image_path, code_image_path, export_path, password):
        """
        decrypt the code from the image

        :param original_image_path: original image path
        :param code_image_path: code embedded image path
        :param export_path: code export path
        :param password: password used for encryption
        :return: None
        """

        # read in images
        original_image_array = read_image(original_image_path)
        code_image_array = read_image(code_image_path)

        original_1d_array = flatten_image(original_image_array).tolist()
        code_1d_array = flatten_image(code_image_array).tolist()

        # read in password
        password = convert_acsii(convert_md5(password))
        password_key = sum(password)
        password_lst = list_padding(convert_cnt_digit(password), 128)

        # extract code from two images
        code_lst = extract_code(original_1d_array, code_1d_array)

        # check password md5 signature
        assert code_lst[-128:].tolist() == password_lst, "Unable to decrypt: wrong password"

        # get original code list length
        code_len_lst = code_lst[-138:-128]
        code_len = convert_int_list(code_len_lst)[0]

        # get original code list
        code_lst = code_lst[:code_len]

        # reverse shuffle using the key
        shuffle_key = password_key % code_len
        code_lst = shuffle_reverse(code_lst, shuffle_key)

        # retrieve the code
        code_lst = convert_int_list(code_lst)
        code_str = "".join([chr(i) for i in code_lst])

        with open(export_path, 'w') as file:
            file.write(code_str)





