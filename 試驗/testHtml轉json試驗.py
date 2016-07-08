from unittest.case import TestCase
from 詞頻doc.轉換doc import 轉換doc
from os.path import dirname, abspath, join


class html轉json試驗(TestCase):

    def 檔案(self, 檔名):
        return join(dirname(abspath(__file__)), '檔案', 檔名)

    def test_有分類(self):
        json = 轉換doc(self.檔案('57-火燒紅蓮寺歌.doc')).doc轉html().html轉json().提json()
        self.assertIn(['文類', '歌仔冊'], json)

    def test_有段(self):
        json = 轉換doc(self.檔案('57-火燒紅蓮寺歌.doc')).doc轉html().html轉json().提json()
        self.assertIn([
            '段',
            '下集工夫即卜展，兩平五路請劍仙，[門@丨]着紅姑即無變，桂武逍遙力做前。',
            'E7-chip8 kang-hu chiah beh tian2, nng7-peng5 ngou2-lou7 chhiann2 kiam3-sian, tu2 tioh8 Ang5-kou chiah bo5 pian3, Kui3-bu2 Siau-iau5 liah8 cho3-chian5.'
        ], json)

    def test_數量著(self):
        json = 轉換doc(self.檔案('57-火燒紅蓮寺歌.doc')).doc轉html().html轉json().提json()
        self.assertEqual(len(json), 295)
