import datetime
import json
class Util:
    def __init__(self, args, kwargs):
        pass
    def getStrDate(self):
        d1 = datetime.datetime.now()
        return d1.strftime("%Y-%m-%d %H:%M:%S")
    def parseDate(self,date):
         return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    def caculateDays(self,strBefore,strNow):
        d1 = self.parseDate(strBefore)
        d2 = self.parseDate(strNow)
        return (d2-d1).days
    def
