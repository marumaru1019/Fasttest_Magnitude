# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import neologdn
import MeCab
import subprocess

import logging

class CreateText:
    def __init__(self, arg):
        self.get_speech = []
        if "d" in arg.part_of_speech:
            self.get_speech.append("動詞")
        if "m" in arg.part_of_speech:
            self.get_speech.append("名詞")
        if "k" in arg.part_of_speech:
            self.get_speech.append("形容詞")

    def load_sentence(self, text_file_path):
        txt_data = open(text_file_path, 'r')
        text = "".join(txt_data.readlines())
        return text

    def normalize(self, text:str):
        normalize_text = neologdn.normalize(text)
        return normalize_text

    def set_mecab_dict(self):
        # neologdの辞書をセット
        logging.info("start setting mecab dictionary")
        cmd = 'echo `mecab-config --dicdir`"/mecab-ipadic-neologd"'
        path = (subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                shell=True).communicate()[0]).decode('utf-8')
        tagger = MeCab.Tagger("-d {0}".format(path))
        logging.info("finish setting mecab dictionary")
        return tagger

    def wakati_text(self, text:str, tagger):
        '''
        文書textを分かち書きして、半角スペース区切りの単語文字列に変換する

        Parameters
        ----------
        text: str
            文書
        Returns
        -------
        text_result: str
            分かち書きされた文書
        '''
        # 分けてノードごとにする
        node = tagger.parseToNode(text)
        wakati_dic = {}
        while node:
            # 単語
            term = node.surface
            # 品詞
            pos = node.feature.split(',')[0]
            # もし品詞が条件と一致してたら
            if pos in self.get_speech:
                wakati_dic[term] = pos
            node = node.next

        return wakati_dic


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser.add_argument("--text_file_path", type=str, default="../input_data/sample.txt", help="Chose your text file to get synonym")
    parser.add_argument("--part_of_speech", type=str, default="dm", help="d:動詞, m:名詞, k:形容詞")

    arg = parser.parse_args()
