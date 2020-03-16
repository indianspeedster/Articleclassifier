def inpurl(url1):
    c = []
    from newspaper import Article
    article = Article(url1)
    article.download()
    article.parse()
    c.append(article.text.replace('\n','').split('. '))
    return c
def run_model(url2):
    import fasttext
    model = fasttext.load_model("article_classifier.bin")
    c = inpurl(url2)
    d = []
    for text in c:
        d.append(list(model.predict(text)[0]))
    
    cv_count = d[0].count(['__label__cv'])
    nlp_count = d[0].count(['__label__nlp'])
    if cv_count > nlp_count:
        return ('cv article')
    else:
        return ('nlp article')
if  __name__ == "__main__":
    url2 = 'https://www.datasciencecentral.com/profiles/blogs/your-guide-to-natural-language-processing-nlp'
    print(run_model(url2))

