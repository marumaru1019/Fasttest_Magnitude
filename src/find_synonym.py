# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from utils import CreateText
from model import LoadMagnitude

import pandas as pd


class FindSynonym:
    def __init__(self, arg):
        self.col = ["word1", "word2", "siimirality", "credibility"]

    # Calculate similarity using the principle of combination to avoid duplication
    def calc_similarity(self, wakati_dic: dict, fasttext_model):
        wakati_word = [k for k, v in wakati_dic.items()]
        sim_list = []
        '''
        ex
        ["WORD1", "WORD2", "WORD3"]

        1. Fetch the first element
        2. Compare the second and subsequent elements in order
        >> WORD1:WORD2
        >> WORD1:WORD3
        3. Pop first element  ["WORD1", "WORD2", "WORD3"] > ["WORD2", "WORD3"]

        Loop 1~3 whitin sim_list existed
        '''
        while wakati_word:
            for i in range(len(wakati_word)-1):
                # Compare the first element of wakati_list with the second and subsequent elements.
                word_sim = fasttext_model.similarity(wakati_word[0], wakati_word[i+1])

                if wakati_word[0] in fasttext_model and wakati_word[i+1] in fasttext_model:
                    sim_list.append([wakati_word[0], wakati_word[i+1], word_sim, "high"])
                elif wakati_word[0] in fasttext_model or wakati_word[i+1] in fasttext_model:
                    sim_list.append([wakati_word[0], wakati_word[i+1], word_sim, "middle"])
                else:
                    sim_list.append([wakati_word[0], wakati_word[i+1], word_sim, "low"])
            # Remove first element
            wakati_word.pop(0)
        # Store result in table
        df = pd.DataFrame(sim_list, columns=self.col)

        return df_text

    def output_synonym_file(self, df):
        result = df[df["similarity"]>=arg.threshold]

        if arg.file_type == "csv":
            result.to_csv(f"{arg.file_name}.csv")
        elif arg.file_type == "xlsx":
            result.to_xlsx(f"{arg.file_name}.xlsx")
        else:
            raise TypeError("Chose file type in csv or xlsx")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(allow_abbrev=False)

    # utils argparse
    parser.add_argument("--text_file_path", type=str, default="../input_data/sample.txt", help="Chose your text file to get synonym")
    parser.add_argument("--normalize", type=bool, default=True, help="Resolution of notation distortions")
    parser.add_argument("--part_of_speech", type=str, default="dm", help="d:動詞, m:名詞, k:形容詞")

    # model argparse
    parser.add_argument("--load_data", type=str, default="v3", help="Chose pretrained dataset volume")

    # find synonym argparse
    parser.add_argument("--file_type", type=str, default="csv", help="Chose file type {csv or xlsx}")
    parser.add_argument("--file_name", type=str, default="synonym", help="Fill in the file name")
    parser.add_argument("--threshold", type=int, default=0,
                    help="What is the threshold of sord similarity? MIN:0 MAX:1 0.5 is better")


    arg = parser.parse_args()

    logging.info("Loading model ...")
    model = LoadMagnitude(arg)
    output = model.build_model()
    logging.info("Finish loading model!")

    txt = CreateText(arg)
    text = txt.load_sentence()
    normalized_text = txt.normalize(text)

    tagger = txt.set_mecab_dict()

    wakati_dic = txt.wakati_text(normalized_text, tagger)

    logging.info("Finding synonym ...")
    syn = FindSynonym(arg)
    df_text = syn.calc_similarity(wakati_dic, output)
    logging.info("Finish finding synonym!")

    syn.output_synonym_file(df_text)
    logging.info(f"Create synonym file {arg.file_type}")






