#!/bin/sh

####################################
# Mecab setup shell script
# Install mecab dictionary from
#
# Reference : https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md
####################################

# Install MeCab
apt install mecab libmecab-dev mecab-ipadic-utf8

# Install mecab-ipadic-NEologd
apt install git make curl xz-utils file
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a

# Ref: https://qiita.com/Fulltea/items/90f6ebe6dcceaf64eaef
# Ref: https://qiita.com/SUZUKI_Masaya/items/685000d569452585210c

ln -s /etc/mecabrc /usr/local/etc/mecabrc
# Ref: https://qiita.com/Naritoshi/items/8f55d7d5cce9ce414395
