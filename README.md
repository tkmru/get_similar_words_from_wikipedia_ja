```
$ wp2txt -i jawiki-latest-pages-articles.xml.bz2
$ cat jawiki-latest-pages-articles.xml-* > jawiki.txt
$ mecab -Owakati -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/mecab-ipadic-neologd -b 81920 jawiki.txt > jawikisep.txt
$ ./word2vec -train jawikisep.txt -output jawikisep.bin -size 200 -threads 4 -binary 1
```