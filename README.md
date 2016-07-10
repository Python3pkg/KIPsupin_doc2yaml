# 教育部臺灣閩南語字詞頻調查工作資料轉換工具

參考允言老師主機[ip093](https://github.com/Taiwanese-Corpus/Ungian_Tsu2-ki1#ip093)的程式`/home/luibenghan/src/kip/ke-si/doc2db`
```
sudo apt-get install -y wv
wvWare 57-火燒紅蓮寺歌.doc 
```

## 轉換了json格式

* 頭前的`出版年`、`文類`、…看語料才知影有抑無
* 一定有`資料`
* `資料`內底一定有`段`，無一定有`作者`

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
virtualenv --python python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install beautifulsoup4 lxml
python -m unittest
```