# 教育部臺灣閩南語字詞頻調查工作資料轉換工具

參考允言老師主機[ip093](https://github.com/Taiwanese-Corpus/Ungian_Tsu2-ki1#ip093)的程式`/home/luibenghan/src/kip/ke-si/doc2db`
```
sudo apt-get install -y wv
wvWare 57-火燒紅蓮寺歌.doc 
```


## 開發
```
virtualenv --python python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install beautifulsoup4 lxml
python -m unittest
```