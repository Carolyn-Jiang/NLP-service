import craper
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def get_comment_list(list):
    # Get 100 comments of each chosen stock from Yahoo Finance by using webcarper
    com = []
    for ele in list:
        temp = craper.web(ele)
        comment = temp.get_comment()
        com.extend(comment)
    return com


def sentiment_analysis(text):
    analyser = SentimentIntensityAnalyzer()
    sentiment_analysis = []
    for i in range(len(text)):
        score = analyser.polarity_scores(text[i])
        sentiment_analysis.append(score)
    return sentiment_analysis


def sentiment(text):
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


def mean_cal(score, n):
    count1 = 0
    count2 = 0
    high_score = []
    low_score = []
    for i in score:
        if i < n:
            count1 += 1
            low_score.append(i)
        elif i > n:
            count2 += 1
            high_score.append(i)

    mean_score = 0
    if count1 > count2:
        mean_score = np.mean(low_score)
    elif count1 < count2:
        mean_score = np.mean(high_score)
    elif count1 == count2:
        mean_score = np.mean(score)

    return mean_score


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
    regr = svm.SVR()
    regr.fit(X_train, Y_train)
    score1 = regr.predict(X_test)
    final_score_id = mean_cal(score1, 3)
    print(final_score_id)
    y_train = sentiment(com_list)
    sentiment_svm = svm.SVR()
    sentiment_svm.fit(X_train, y_train)
    score2 = sentiment_svm.predict(X_test)
    final_score_senti = mean_cal(score2, 0)
    print(final_score_senti)
