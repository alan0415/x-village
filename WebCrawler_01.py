from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://www.imdb.com/title/tt4073790/')
element = response.html.find('.credit_summary_item').find('.itemprop[itemprop=name]')
print(element.txt)