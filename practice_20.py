#控制 datetime model 輸出明天的日期
import datetime
def print_next_day():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days = 1)
    print(tomorrow.isoformat())

print_next_day()