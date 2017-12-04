import os
from PIL import Image
import numpy
from collections import Counter


def get_most_common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][0]


def calc_blue(chr, r, g):
    return int(round(chr * (r / 256) * (g / 256) * 10))


def generate_files_in_dir(dirname):
    return [os.path.join(dirname, fname) for fname in os.listdir(dirname)]


def get_image_width(image_name):
    img = Image.open(image_name)
    return img.size[0]


def generate_reliable_pixels(img_data):
    for i, (r, g, b) in enumerate(img_data):
        if b != 255:
            yield i, (r, g, b)


def get_char_candidates(r, g, b):
    ret = []
    for c in range(31, 127):
        if b == calc_blue(c, r, g):
            ret.append(c)
    return ret


if __name__ == '__main__':
    fnames = generate_files_in_dir('encoded_prod')

    image_width = get_image_width(fnames[0])
    candidate_pool = []
    for i in range(image_width):
        candidate_pool.append([])

    for fname in fnames:
        img = Image.open(fname)
        img_data = numpy.asarray(img)[0]
        for i, (r, g, b) in generate_reliable_pixels(img_data):
            candidates = get_char_candidates(r, g, b)
            print(i, r, g, b, candidates)
            candidate_pool[i] += candidates

    flag = ''
    for candidate in candidate_pool:
        flag += chr(get_most_common(candidate))

    print(flag)

