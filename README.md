#distance wikipedia
Word2vecを用いて日本語版 wikipediaのデータを学習させ、単語の共起関係を求めた。

##学習データ取得方法
まず、ダウンロードしてきたjawiki-latest-pages-articles.xml.bz2を、wp2txtを用いてテキストに変換、そして得たmecabを用いて得たテキストの分かち書きを求める。最後に分かち書きをword2vecに学習させる。
コマンドは以下。

```
$ wp2txt -i jawiki-latest-pages-articles.xml.bz2
$ cat jawiki-latest-pages-articles.xml-* > jawiki.txt
$ mecab -Owakati -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd -b 81920 jawiki.txt > jawikisep.txt
$ ./word2vec -train jawikisep.txt -output jawikisep.bin -size 200 -threads 4 -binary 1 -window 5 -sample 1e-3 
```

##共起関係を出力する
どの単語との共起関係を求めるか考えたところ、出現回数が多い単語の共起関係を求めたほうが正確になるとの考えに至った。
以下のコマンドで名詞をwikipediaのテキストから出現回数順に出力した。jawiki.txtが5.47GBあるので時間がかかった。
ファイルを分割して並列でやるべきだった。

```
$ cat jawiki.txt | mecab -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd -b 81920| grep $"\t名詞"| cut -f1 | sort | uniq -c | sort -nr > jawiki_meishi.txt
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
