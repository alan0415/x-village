from requests_html import HTMLSession
session = HTMLSession()
url = 'https://sirius207.github.io/course-template/2018/'
response = session.get(url)
response.html.render() # 加上這一行即可，第一次跑他會花幾分鐘的時間下載 Chromium，用來跑 Javascript
elements = response.html.find('td[data-title=Description]')
print(elements[0].text)