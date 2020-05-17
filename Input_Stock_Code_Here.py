import craper
import numpy as np
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# craper is a Class in craper.py used to download comments of stocks in
# YahooFinance.

def get_comment_list(list):
    com = []
    # read comments from webscraper using selenium
    for ele in list:
        temp = craper.web(ele)
        comment = temp.get_comment()
        # save comment in list
        com.extend(comment)
    return com


def sentiment_analysis(text):
    analyser = SentimentIntensityAnalyzer()
    sentiment_analysis = []
    # import the package
    for i in range(len(text)):
        score = analyser.polarity_scores(text[i])
        temp = score['compound']
        # save compound score in a list
        sentiment_analysis.append(temp)
    return sentiment_analysis


def mean_cal(score, n):
    # score is output of predict by sklearn
    # n is the average of score range
    # n = 3 for score range (1,5)
    # n = 0 for score range (-1,1) in Sentiment Analyser
    count1 = 0
    count2 = 0
    high_score = []
    low_score = []
    for i in score:
        if i < n:
            # save score under average to a indivdual list1
            # and count times
            count1 += 1
            low_score.append(i)
        elif i > n:
            # save score above average to a indivdual list1
            # and count times
            count2 += 1
            high_score.append(i)

    mean_score = 0
    if count1 > count2:
        # if there is more low score, then calulate the mean of
        # low score only and delete score above average
        mean_score = np.mean(low_score)
    elif count1 < count2:
        # if there is more high score, then calulate the mean of
        # high score only and delete score under average
        mean_score = np.mean(high_score)
    elif count1 == count2:
        # if above average and under average have same number
        # get mean of all the scores
        mean_score = np.mean(score)

    return mean_score


def get_score(X_train,y_train,X_test):
    # build the regressor model
    regr = svm.SVR()
    # train it
    regr.fit(X_train, y_train)
    # get predict value of X_test
    score = regr.predict(X_test)
    return score


if __name__ == "__main__":
    # these are stocks label to score = 5
    # because their stock price increased a lot
    com_list5 = ['AMZN','FB','ZM','MSFT', 'AAPL']
    # these are stocks label to score = 4
    # because their price has some Increase
    com_list4 = ['BBY', 'MNST', 'HLF', 'NYT', 'BAC']
    # these are stocks label to score = 3
    # because their price barely change
    com_list3 = ['COST', 'SBUX','TIF', 'C', 'UNH']
    # these are stocks label to score = 2
    # because their price has some decrease
    com_list2 = ['GS', 'LUV', 'AAL', 'ATVI', 'WEN']
    # these are stocks label to score = 1
    # because they have huge decrease in price
    com_list1 = ['UA','TSN','UAL','UBER','HLT']
    # this is the input box, input the code of stock need to be tested
    test_company = [input('Please enter the stock code:')]
    # get comments of all the stocks
    com5 = get_comment_list(com_list5)
    com4 = get_comment_list(com_list4)
    com3 = get_comment_list(com_list3)
    com2 = get_comment_list(com_list2)
    com1 = get_comment_list(com_list1)
    # combine to one list
    com_list = com1 + com2 + com3 + com4 + com5
    # build the corresponding y_train list
    list1 = [1]*len(com1)
    list2 = [2]*len(com2)
    list3 = [3]*len(com3)
    list4 = [4]*len(com4)
    list5 = [5]*len(com5)
    y_train = list1 + list2 + list3 +list4 + list5

    # download the comments of the stock being tested
    t_com = get_comment_list(test_company)

    # Using tfidf vectoizer to change text to matrix
    tfidf_vectorizer = TfidfVectorizer(use_idf=True, stop_words='english')
    # X_train is the matrix list of 25 companies comments,
    # 100 comments each company
    X_train = tfidf_vectorizer.fit_transform(com_list)
    # X_test is the matrix of 100 comments of the test company
    X_test = tfidf_vectorizer.transform(t_com)
    # use sentiment_analysis function to get sentiment score of comments
    y_senti = sentiment_analysis(com_list)

    # get predict score of X_test by score range(1-5) method
    score_1 = get_score(X_train, y_train, X_test)
    # calculate the weighted mean, with middle of range(1,5) = 3
    final_score_id = mean_cal(score_1, 3)

    # get predict score of X_test by sentiment analyzer
    score_senti = get_score(X_train, y_senti, X_test)
    # calculate the weighted mean, with middle of range(-1,1) = 0
    final_score_senti = mean_cal(score_senti, 0)

    # print out the weighted mean value of each method
    print('Sentiment analyzer give score of %f'%final_score_senti)
    print('Increase/decrease analyzere give score of %f'%final_score_id)
