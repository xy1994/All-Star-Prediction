import csv
import datetime
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from afinn import Afinn
performance = []
good = 0
for n in range(10):
    if n == 1:
        continue
    print(n)
    performance = []
    for k in range(7):
        #print(k)
        #print(k)
        file = open('text_user_dataset/stats/'+str(n)+'_'+str(k+2012)+'.csv', 'r')
        file_ = open('text_user_dataset/cleaned/'+str(n)+'.csv', 'r',encoding='utf-8')
        data = csv.reader(file,delimiter=',')
        data_ = csv.reader(file_,delimiter=',')
        data_list = []
        text_list = []
        for row in data:
            data_list.append(row)
        for row in data_:
            text_list.append(row)
        #print(text_list)
        average = []
        FGP = 0
        TRB = 0
        AST = 0
        PTS = 0
        gmsc = 0
        addminor = 0
        if len(data_list) == 1:
            continue
        for i in range(len(data_list)-1):
            if data_list[i+1][12] == "Did Not Play" or data_list[i+1][12] == "Inactive" or data_list[i+1][12] == "Did Not Dress" or data_list[i+1][12] == "Not With Team" or data_list[i+1][12] == "Player Suspended":
                continue
            if data_list[i+1][12] == "":
                data_list[i+1][12] = "0.000"
            FGP = FGP + float(data_list[i+1][12])
            TRB = TRB + int(data_list[i+1][21])
            AST = AST + int(data_list[i+1][22])
            PTS = PTS + int(data_list[i+1][27])
            gmsc = gmsc + float(data_list[i+1][28])
            addminor = addminor + int(data_list[i+1][29])
        FGP = (FGP + 0.0)/(len(data_list)-1)
        TRB = (TRB + 0.0)/(len(data_list)-1)
        AST = (AST + 0.0)/(len(data_list)-1)
        PTS = (PTS + 0.0)/(len(data_list)-1)
        gmsc = (gmsc + 0.0)/(len(data_list)-1)
        addminor = (addminor + 0.0)/(len(data_list)-1)
        average.append(FGP)
        average.append(TRB)
        average.append(AST)
        average.append(PTS)
        average.append(gmsc)
        average.append(addminor)
        for i in range(len(data_list)-1):
            if data_list[i+1][12] == "Did Not Play" or data_list[i+1][12] == "Inactive" or data_list[i+1][12] == "Did Not Dress" or data_list[i+1][12] == "Not With Team" or data_list[i+1][12] == "Player Suspended":
                continue
            count = 0
            hastext = 0
            game = []
            #game.append(data_list[i+1][2])
            text = ""
            #print(len(data_list)-1-i)
            if float(data_list[i+1][12])>average[0]:
                count = count + 2
            if int(data_list[i+1][21])>average[1]:
                count = count + 1
            if int(data_list[i+1][22])>average[2]:
                count = count + 1
            if int(data_list[i+1][27])>average[3]:
                count = count + 3
            if float(data_list[i+1][28])>average[4]:
                count = count + 2
            if int(data_list[i+1][29])>0:
                count = count + 3
            if count > 6:
                #good = good + 1
                game.append(count)
                #game.append(int(data_list[i+1][29]))
            else:
                game.append(count)
                #game.append(int(data_list[i+1][29]))
            time = data_list[i+1][2]
            year = time[0:4]
            month = time[5:7]
            date = time[8:10]
            d1 = datetime.datetime(int(year),int(month),int(date))
            for j in range(len(text_list)-1):
                #print(j)
                if len(text_list[j+1])!=0:
                    time_ = text_list[j+1][0]
                    year_ = time_[0:4]
                    month_ = time_[5:7]
                    date_ = time_[8:10]
                    d2 = datetime.datetime(int(year_),int(month_),int(date_))
                    diff = (d2-d1).days
                    if diff>=-1 and diff<1:
                        text = text + text_list[j+1][1]
                        hastext = 1
                    if diff>=1:
                        if hastext == 1:
                            game.insert(0," " + text)
                        continue
            #game.append(text)
            if hastext == 1 and len(game)==1:
                game.insert(0," " + text)
            if hastext == 1:
                if game[1] == 1:
                    good = good + 1
                performance.append(game)
    afinn = Afinn()
    sid = SIA()
    for i in range(len(performance)):
    
        #ss = sid.polarity_scores(performance[i][0])
        ss = afinn.score(performance[i][0])
        performance[i][0] = ss
        #performance[i][0] = ss["compound"]
        
    from sklearn.preprocessing import scale 
    performance = scale(performance)
    count = 0
    score1 = 0
    score2 = 0
    for i in range(len(performance)):
        score1 = score1 + performance[i][0]
        score2 = score2 + performance[i][1]
        if performance[i][0]>=0 and performance[i][1]>=0:
            count = count + 1
        elif performance[i][0]<0 and performance[i][1]<0:
            count = count + 1
    print((count+0.0)/len(performance))
    #print(score1)
    #print(score2)
#print(performance)
        #print(performance)
        #print(good)
        #print(len(performance))
#X_train = performance[:split_size]
#y_train = performance[:split_size]
#X_test  = performance[split_size:]
#y_test  = performance[split_size:]

'''
file = open('opinion-lexicon-English/negative-words.txt', 'r')
file_positive = open('opinion-lexicon-English/positive.txt', 'r')
file_negative = open('opinion-lexicon-English/negative.txt', 'r')
data_positive = file_positive.read()
data_negative = file_negative.read()
pos_features = data_positive.split("\n")
neg_features = data_negative.split("\n")
data = file.read()
word_features = data.split("\n")
from nltk.corpus import movie_reviews
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
#word_features = list(all_words)[:1000]
#print(word_features)

def document_features(document): 
    document_words = set(document) 
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features
#featuresets = [(document_features(d), c) for (d,c) in performance]
#X_train = featuresets[:split_size]
#X_test  = featuresets[split_size:]
X_train = performance[:split_size]
X_test = performance[split_size:]
'''
'''
count = 0
dict_emotion = {}
for i in range(len(performance)):
    good_word = 0
    bad_word = 0
    sentence = performance[i][0].split(' ')
    for word in sentence:
        word = word.lower()
        if word in pos_features:
            good_word = good_word + 1
            #if word in dict_emotion:
            #    dict_emotion[word]+=1
            #else:
            #    dict_emotion[word]=1
        if word in neg_features:
            bad_word = bad_word + 1
            #if word in dict_emotion:
            #    dict_emotion[word]+=1
            #else:
            #    dict_emotion[word]=1
    if good_word>bad_word:
        if performance[i][1] == 1:
            count = count + 1
    else:
        if performance[i][1] == 0:
            count = count + 1
    performance[i][0] = good_word - bad_word
print(count)
print((count+0.0)/len(performance))
#dict_emotion = sorted(dict_emotion.keys())
#print(dict_emotion)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

X = []
y = []    
for i in range(len(performance)):
    number = []
    number.append(performance[i][0])
    X.append(number)
    y.append(performance[i][1])
regr = linear_model.LinearRegression()
regr.fit(X,y)
pred = regr.predict(X)

plt.scatter(X, y,  color='black')
plt.plot(X, pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
'''


'''
print(len(performance))
g = 0
for i in range(len(performance)):
    if performance[i][1] == 1:
        g = g + 1
print(g)
print((g+0.0)/len(performance))
'''


'''
classifier = nltk.NaiveBayesClassifier.train(X_train)
#classifier = nltk.MaxentClassifier.train(X_train)
print(nltk.classify.accuracy(classifier, X_test))
classifier.show_most_informative_features(5)
''' 

'''
import textblob
from textblob.classifiers import NaiveBayesClassifier

cl = NaiveBayesClassifier(X_train)
print(cl.accuracy(X_test))
cl.show_informative_features(5)
'''