from unittest.case import TestCase
from 詞頻doc.轉換doc import 轉換doc
from os.path import dirname, abspath, join


class doc轉html試驗(TestCase):

    def 檔案(self, 檔名):
        return join(dirname(abspath(__file__)), '檔案', 檔名)

    def test_有table(self):
        html = 轉換doc(self.檔案('57-火燒紅蓮寺歌.doc')).doc轉html().提html()
        self.assertIn('<table', html)
        self.assertIn('</table>', html)

    def test_真平11(self):
        html = (
            轉換doc(self.檔案('真平11.doc'))
            .doc轉html().提html()
        )
        self.assertIn('<table', html)
        self.assertIn('</table>', html)

