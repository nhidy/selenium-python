import webui_test
from datetime import datetime
from webui_test.running.config import BrowserConfig

# t = datetime.datetime.today()
# print('Thoi gian hien tai truoc: ', t)
# future = datetime.datetime(t.year, t.month, t.day, 3, 0)
# if t.hour >= 3:
# 	future += datetime.timedelta(days=1)
# print('Thoi gian can chay: ', future)
# print('Thoi gian doi: ', (future-t).total_seconds())
# time.sleep((future-t).total_seconds())
# t2 = datetime.datetime.today()
# print('Thoi gian hien tai sau: ', t2)
browser='edge'
# browser='firefox'
# browser='chrome'
if __name__ == '__main__':
    webui_test.main(path="./test_dir/regression/test_regression_mortgage.py", browser=browser, debug=False, headless=False, report=f"test_regression_mortgage_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
