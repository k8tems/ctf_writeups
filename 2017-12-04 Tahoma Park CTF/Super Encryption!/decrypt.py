import unittest


def derive_key(i):
    key = [5, 5, 1, 1, 0, 0, 10, 10, 9, 9, 0, 0, 10, 10, 9, 9, 8, 8, 4, 4, 3, 3, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 0, 0]
    return key[i]


def sub_key(cipher):
    """Derive key from `i` and subtract from `inp`"""
    ret = ''
    for i, c in enumerate(cipher):
        ret += chr(ord(c) - derive_key(i))
    return ret


def divide(inp, chunk_size):
    ret = []
    while inp:
        ret.append(inp[:chunk_size])
        inp = inp[chunk_size:]
    return ret


def shuffle(inp, chunk_size):
    ret = ''
    divided = divide(inp, chunk_size)
    for chunk in divided:
        if len(chunk) < chunk_size:
            ret += chunk
        else:
            ret += ''.join(reversed(chunk))
    return ret


def decrypt(inp):
    inp = shuffle(inp, 3)
    inp = shuffle(inp, 5)
    inp = sub_key(inp)
    return inp


class Test(unittest.TestCase):
    def test_sub_key(self):
        self.assertEqual('abcde', sub_key('fgdee'))

    def test_divide(self):
        self.assertEqual(['eeg', 'df'], divide('eegdf', 3))

    def test_shuffle(self):
        self.assertEqual('deegf', shuffle('eedgf', 3))

    def test_decrypt(self):
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', decrypt('deesfgqrrxxfklwzwxzyyyyzx{'))


if __name__ == '__main__':
    # unittest.main()
    print(decrypt('dufhyuc>bi{{f0|;vwh<~b5p5thjq6goj}'))
