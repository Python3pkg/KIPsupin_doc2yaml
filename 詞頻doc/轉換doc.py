
from subprocess import Popen, PIPE

class 轉換doc:
    @classmethod
    def doc轉html(cls,檔名):
        程序 = Popen(['wvWare',檔名], stdin=None, stdout=PIPE, stderr=PIPE)
        輸出資訊, _錯誤輸出資訊 = 程序.communicate()
        return 輸出資訊.decode('utf-8')