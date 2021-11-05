import pymysql
import time

class Database:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='mrchoidb', password='mrchoihandsome', db='thiefcam')
        self.cur = self.db.cursor()
        print("good")

    def selectAllJson(self):
        sql = "select * from pics;"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def insertJson(self, hum, temper):
        tm = time.localtime()
        yeardate = "{0}-{1:02d}-{2:02d}".format(tm.tm_year, tm.tm_mon, tm.tm_mday)
        nowtime = "{0:02d}:{1:02d}:{2:02d}".format(tm.tm_hour, tm.tm_min, tm.tm_sec)
        sql = "insert into recorddht(data) values(%s);"
        val = ('{{"yeardate":"{}", "time":"{}"}}'.format(yeardate, nowtime))
        self.cur.execute(sql, val)
        self.db.commit()
        return "good"
