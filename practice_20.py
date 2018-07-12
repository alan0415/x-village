#控制 datetime model 輸出明天的日期
import datetime

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
print(tomorrow.isoformat())