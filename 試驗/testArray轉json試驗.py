from unittest.case import TestCase
from 詞頻doc.轉換doc import 轉換doc
from os.path import dirname, abspath, join


class array轉json試驗(TestCase):

    def 檔案(self, 檔名):
        return join(dirname(abspath(__file__)), '檔案', 檔名)

    def test_有資料來源(self):
        json = (
            轉換doc(self.檔案('57-火燒紅蓮寺歌.doc'))
            .doc轉html().html轉array().array轉json()
            .提json()
        )
        self.assertIn('文類', json)
        self.assertIn('書名', json)
        self.assertIn('出版者', json)
        self.assertIn('書寫系統', json)
        self.assertIn('作者', json)
        self.assertIn('出版年', json)

    def test_一個檔案一篇(self):
        json = (
            轉換doc(self.檔案('57-火燒紅蓮寺歌.doc'))
            .doc轉html().html轉array().array轉json()
            .提json()
        )
        self.assertEqual(len(json['資料']), 1)
        self.assertIn('篇名', json['資料'][0])
        self.assertIn('段', json['資料'][0])

    def test_一個檔案濟篇(self):
        json = (
            轉換doc(self.檔案('真平10.doc'))
            .doc轉html().html轉array().array轉json()
            .提json()
        )
        self.assertEqual(len(json['資料']), 5)
