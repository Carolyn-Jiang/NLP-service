import craper
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_comment_list(list):
    #Get 100 comments of each chosen stock from Yahoo Finance by using webcarper 
    com = []
    for ele in list:
        temp = craper.web(ele)
        comment = temp.get_comment()
        com.extend(comment)
    return com

def svm_test(X, Y):
    #Build up regression function for SVM modeling
    regr = svm.SVR()
    return(regr.fit(X, Y))

def sentiment(text):
    analyser = SentimentIntensityAnalyzer()
    def sentiment_analysis(text):
        sentiment_analysis = []
        for i in range(len(text)):
            score = analyser.polarity_scores(text[i])
            scores = sentiment_analysis.append(score)
        return sentiment_analysis
    score = sentiment_analysis(text)
    negs = []
    neus = []
    poss = []
    compounds = []
    for dict in score:
        neg = dict['neg']
        negs.append(neg)
        neu = dict['neu']
        neus.append(neu)
        pos = dict['pos']
        poss.append(pos)
        compound = dict['compound']
        compounds.append(compound)
        df = pd.DataFrame({'neg':negs, 'neu':neus, 'pos':poss, 'compound':compounds})
        train = df.values
    return(train)

if __name__ == "__main__":
    com_list5 = ['AMZN','FB','ZM','MSFT', 'AAPL']
    com_list4 = ['BBY', 'MNST', 'HLF', 'NYT', 'BAC']
    com_list3 = ['COST', 'SBUX','TIF', 'C', 'UNH']
    com_list2 = ['GS', 'LUV', 'AAL', 'ATVI', 'WEN']
    com_list1 = ['UA','TSN','UAL','UBER','HLT']
    test_company = [input('Please enter the stock code:')]
    com5 = get_comment_list(com_list5)
    com4 = get_comment_list(com_list4)
    com3 = get_comment_list(com_list3)
    com2 = get_comment_list(com_list2)
    com1 = get_comment_list(com_list1)
    com_list = com1 + com2 + com3 + com4 + com5
    list1 = [1]*len(com1)
    list2 = [2]*len(com2)
    list3 = [3]*len(com3)
    list4 = [4]*len(com4)
    list5 = [5]*len(com5)
    Y_train = list1 + list2 + list3 +list4 + list5
    t_com = get_comment_list(test_company)

if __name__ == "__main__":
    tfidf_vectorizer = TfidfVectorizer(use_idf=True, stop_words='english')
    X_train = tfidf_vectorizer.fit_transform(com_list)
    X_test = tfidf_vectorizer.transform(t_com)
    tfidf_svm = svm_test(X_train,Y_train)
    score1 = tfidf_svm.predict(X_test)
    print(np.mean(score1))
    x_train = sentiment(com_list)
    sentiment_svm = svm_test(x_train, Y_train)
    x_test = sentiment(t_com)
    score2 = sentiment_svm.predict(x_test)
    print(np.mean(score2))
