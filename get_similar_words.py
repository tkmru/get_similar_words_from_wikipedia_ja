#!/usr/bin/env python3
# coding: UTF-8

import gensim

model = gensim.models.Word2Vec.load_word2vec_format('jawikisep.bin', binary=True, unicode_errors='ignore')
counter = 0

with open('jawiki_meishi.txt', 'r') as f:
    for line in f:
        meishi = line.strip().split(' ')[1]
        # 数字と1文字のアルファベットを除く
        if not meishi.isdigit() and not (len(meishi) == 1 and ('a' <= meishi <= 'z' or 'A' <= meishi <= 'Z')):
            result = model.most_similar(positive=[meishi])
            for similar_word, distance in result:
                counter += 1
                print(counter, meishi, similar_word)

                with open('similar_words.txt', 'a') as f:
                    f.write(meishi + '\t' + similar_word + '\n')
