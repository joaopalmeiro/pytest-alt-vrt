from itertools import chain

import numpy as np


def flatten(seq_of_seqs):
    return chain.from_iterable(seq_of_seqs)


def pil2np(img):
    return np.array(img)
