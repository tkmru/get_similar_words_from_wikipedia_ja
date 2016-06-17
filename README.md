#distance wikipedia
Word2vecを用いて日本語版 wikipediaのデータを学習させ、単語の共起関係を求めた。

##学習データ取得方法
まず、ダウンロードしてきたjawiki-latest-pages-articles.xml.bz2を、wp2txtを用いてテキストに変換、そして得たテキストの、分かち書きをmecabを用いて求める。最後に分かち書きをword2vecに学習させる。
コマンドは以下。

```
$ wp2txt -i jawiki-latest-pages-articles.xml.bz2
$ cat jawiki-latest-pages-articles.xml-* > jawiki.txt
$ mecab -Owakati -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd -b 81920 jawiki.txt > jawikisep.txt
$ ./word2vec -train jawikisep.txt -output jawikisep.bin -size 200 -threads 4 -binary 1 -window 5 -sample 1e-3 
```

##共起関係を出力する

##Licence
"THE BEER-WARE LICENSE"

If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
