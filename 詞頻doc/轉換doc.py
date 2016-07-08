
from subprocess import Popen, PIPE
from bs4 import BeautifulSoup


class 轉換doc:
    def __init__(self, 檔名):
        self.檔名=檔名
    def doc轉html(self):
        程序 = Popen(['wvWare', self.檔名], stdin=None, stdout=PIPE, stderr=PIPE)
        輸出資訊, _錯誤輸出資訊 = 程序.communicate()
        self.html=輸出資訊.decode('utf-8')
        return self
    def 提html(self):
        return self.html
    def html轉json(self):
        bs=BeautifulSoup(self.html, "lxml")
        table=bs.table
        全部資料=[]
        for tr in table.find_all('tr'):
            一逝資料=[]
            for td in tr.find_all('td'):
                一逝資料.append(td.get_text("",strip=True))
            全部資料.append(一逝資料)
        self.json=全部資料
        return self
    def 提json(self):
        return self.json