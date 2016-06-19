#distance wikipedia
Word2vecを用いて日本語版 wikipediaのデータを学習させ、単語の共起関係を求めた。

##ファイル
### get_similar_words.py
Word2Vecの学習データを用いてカテゴリ別に単語を出力する。gensimとCythonが必要。

```
$ pip install gensim
$ pip install cython
```

##similar_words.txt
get_similar_words.pyが出力した、100610個のカテゴリ分けされた単語が入っているファイル。
各行のtabの左にあるのがカテゴリで右にあるのが単語となっている。

##学習データ取得方法
まず、ダウンロードしてきたjawiki-latest-pages-articles.xml.bz2を、wp2txtを用いてテキストに変換、そして得たmecabを用いて得たテキストの分かち書きを求める。最後に分かち書きをword2vecに学習させる。
コマンドは以下。

```
$ wp2txt -i jawiki-latest-pages-articles.xml.bz2
$ cat jawiki-latest-pages-articles.xml-* > jawiki.txt
$ mecab -Owakati -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd -b 81920 jawiki.txt > jawikisep.txt
$ ./word2vec -train jawikisep.txt -output jawikisep.bin -size 200 -threads 4 -binary 1 -window 5 -sample 1e-3 
```

##単語をカテゴリに分類する
単語の共起関係を求めることで単語をカテゴリ分けする。
どの単語との共起関係を求めるか考えたところ、出現回数が多い単語の共起関係を求めたほうが正確になるとの考えに至った。
以下のコマンドで名詞をwikipediaのテキストから出現回数順に出力した。jawiki.txtが5.47GBあるので時間がかかった。
ファイルを分割して並列でやるべきだった。

```
$ cat jawiki.txt | mecab -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd -b 81920| grep $"\t名詞"| cut -f1 | sort | uniq -c | sort -nr > jawiki_meishi.txt
```

出力された jawiki_meishi.txt の中身、行数は以下のようになっている。

```
$ head jawiki_meishi.txt 
3046624 2
3014297 1
2620012 こと
2575308 年
2101172 ref
1935276 3
1682829 http://
1577551 4
1427831 ため
1176034 www
$ wc -l jawiki_meishi.txt 
 5534241 jawiki_meishi.txt
```

出現頻度が高い名詞の中には、数値やアルファベット一文字のものがあったが、これらをカテゴリ分けしても意味が無いと思ったので、これらを除く単語の共起関係をファイルに出力するスクリプトを書いた。

```
$ python get_similar_words.py
1 こと 事
2 こと ため
3 こと もの
4 こと ところ
5 こと ので
6 こと よう
7 こと 場合
8 こと はず
9 こと 可能性
10 こと が
11 年 年間
12 年 8年
13 年 か月
14 年 ヶ月
15 年 ヵ月
16 年 歳
17 年 元年
18 年 カ月
19 年 1877年
20 年 年頃
21 ref REF
22 ref blockquote
23 ref noinclude
24 ref reF
25 ref small
26 ref nowiki
```  

このスクリプトはjawiki_meishi.txtに含まれる5534241個の名詞に関連する単語を出力するが、今回はそこまでやる必要がなかったので、100610件出力した時点で終了した。

```
$ head similar_words.txt 
こと  事
こと  ため
こと  もの
こと  ところ
こと  ので
こと  よう
こと  場合
こと  はず
こと  可能性
こと  が

$ wc -l similar_words.txt 
  100610 similar_words.txt
```


##参考資料
- [Statistical Semantic入門 ~分布仮説からword2vecまで~](http://www.slideshare.net/unnonouno/20140206-statistical-semantics)
- [自然言語処理をなにも知らない私がword2vecを走らせるまで: 最尤日記](http://saiyu.cocolog-nifty.com/zug/2014/02/word2vec-1867.html)
- [Ubuntu + word2vecで日本語版wikipediaを自然言語処理してみた - from umentu import stupid](http://blog.umentu.work/ubuntu-word2vec%E3%81%A7%E6%97%A5%E6%9C%AC%E8%AA%9E%E7%89%88wikipedia%E3%82%92%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%87%A6%E7%90%86%E3%81%97%E3%81%A6%E3%81%BF%E3%81%9F/)
- [青空文庫のデータを使って、遅ればせながらword2vecと戯れてみた - 東京で働くデータサイエンティストのブログ](http://tjo.hatenablog.com/entry/2014/06/19/233949)

##Licence
"THE BEER-WARE LICENSE"

If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
