# 教育部臺灣閩南語字詞頻調查工作資料轉換工具

[![Build Status](https://travis-ci.org/sih4sing5hong5/KIPsupin_doc2yaml.svg?branch=master)](https://travis-ci.org/sih4sing5hong5/KIPsupin_doc2yaml)
[![Coverage Status](https://coveralls.io/repos/github/sih4sing5hong5/KIPsupin_doc2yaml/badge.svg?branch=master)](https://coveralls.io/github/sih4sing5hong5/KIPsupin_doc2yaml?branch=master)

參考允言老師主機[ip093](https://github.com/Taiwanese-Corpus/Ungian_Tsu2-ki1#ip093)的程式`/home/luibenghan/src/kip/ke-si/doc2db`使用`wvWare`來轉`doc`
```
sudo apt-get install -y wv g++ libxml2-dev libxslt1-dev python3-dev
virtualenv --python python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install KIPsupin_doc2yaml
轉換doc到json <doc的資料夾> <json的資料夾>
```

## 相關格式專案
* [教育部臺灣閩南語字詞頻調查工作](https://github.com/Taiwanese-Corpus/Ungian_2009_KIPsupin)
* [臺語國校仔課本](https://github.com/Taiwanese-Corpus/kok4hau7-kho3pun2)
* [新約聖經語料](https://github.com/Taiwanese-Corpus/Pakhelke-1916_KoTan-1975_hiantaiekpun-2008_tailwanese-bible)

## 轉換了json格式

* 頭前的`出版年`、`文類`、…，看語料才知影有抑無
* 一定有`資料`
* `資料`內底一定有`段`，無一定有`作者`、`文類`，`出版年`、…。看語料有照逐筆資料提供無

```
{
  "出版年": "2007",
  "文類": "報導文學",
  "書名": "臺灣閩南語朗讀文章選輯",
  "書寫系統": "漢羅",
  "資料": [
    {
      "作者": "林文平",
      "段": [
        [
          "漢字",
          "白話字"
        ],
        [
          "漢字",
          "白話字"
        ],
        ]
      ],
      "篇名": "芎蕉王國──旗山"
    },
    {
      "作者": "江榮慶",
      "段": [
        [
          "漢字",
          "白話字"
        ],
        [
          "漢字",
          "白話字"
        ],
        ],
      "篇名": "毋免放尿的囡仔"
    },
  ]
}
```

## 開發
```
sudo apt-get install -y wv g++ libxml2-dev libxslt1-dev python3-dev
virtualenv --python python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install beautifulsoup4 lxml
python -m unittest
```
