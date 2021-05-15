# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pymagnitude import *
import logging

#########################
# Magnitude + fasttext(word2vec)
# Magnitude is a natural language library that is upwardly compatible with genisum,
# and can retrieve word vectors at high speed.
# Unknown words can be dealt with based on the vector of similar known words in the same string.
# Reference: https://kamujun.hatenablog.com/entry/2019/02/28/160616
#########################

class LoadMagnitude:
    def __init__(self, arg):

        '''
        Chose pre toraining magunitude data

        ARG(version)        VOLUME
        v1                 2.4GB
        v2                 1.5GB
        v3(default)        0.8GB

        more information in below reference
        https://github.com/WorksApplications/chiVe
        '''

        self.data = {
            "v1": "https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.2-mc15.magnitude",
            "v2": "https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.2-mc30.magnitude",
            "v3": "https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.2-mc90.magnitude"
        }
        self.load_version = arg.load_data
        self.load_data = self.data[arg.load_data]

    def build_model(self):
        logging.info(f"select data is {self.load_version}")
        model = Magnitude(self.load_data)
        logging.info("finish load data")
        return model


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument("--load_data", type=str, default="v3", help="Chose pretrained dataset volume")

    arg = parser.parse_args()

    model = LoadMagnitude(arg)
    model.build_model()
