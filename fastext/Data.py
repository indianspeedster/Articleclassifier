def inp(url):
    c = []
    from newspaper import Article
    for ur in url:
        article = Article(ur)
        article.download()
        article.parse()
        c.append(article.text.replace('\n','').split('. '))
    return c


def to_txt(c,path):
    file1 = open(path,"a")
    for fil in c:
        for text in fil:
            file1.write('__label__cv'+' '+text+'\n')
    file1.close()
def to_txtnp(c,path):
    file1 = open(path,"a")
    for fil in c:
        for text in fil:
            file1.write('__label__nlp'+' '+text+'\n')
    file1.close()
if  __name__ == "__main__":
    url = ['https://www.sciencedirect.com/science/article/pii/S1077314219301183','https://www.sciencedirect.com/science/article/pii/S1077314216300339','https://www.sciencedirect.com/science/article/pii/S1077314219300025','https://www.sciencedirect.com/science/article/pii/S1077314217300620']
    a = inp(url)
    to_txt(a,'data.txt')
    url2 = ['https://www.datasciencecentral.com/profiles/blogs/5-easy-steps-to-structure-highly-unstructured-big-data','https://www.datasciencecentral.com/profiles/blogs/your-guide-to-natural-language-processing-nlp']
    b = inp(url2)
    to_txtnp(b,'data.txt')