import newspaper
bbc_paper = newspaper.build('https://www.reuters.com')
#sina_paper = newspaper.build('http://www.sina.com.cn/', language='zh')

for category in bbc_paper.category_urls():
     print(category)
# for article in bbc_paper.articles:
#     print(article.url)
#     #article.download()
#     # article.parse()
#     # print(article.text)