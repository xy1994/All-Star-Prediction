import json
import csv

players = ["Lebron AND James -@KingJames","Kawhi AND Leonard -@kawhileonard",
          "Kevin AND Durant -@KDTrey5","James AND Harden -@JHarden13",
          "Russell AND Westbrook -@russwest44","Stephen AND Curry -@StephenCurry30",
          "Giannis AND Antetokounmpo -@Giannis_An34","Chris AND Paul -@CP3",
          "Jimmy AND Butler -@JimmyButler","Anthony AND Davis -@AntDavis23",
          "Draymond AND Green -@Money23Green","John AND Wall -@JohnWall",
          "Paul AND George -@Yg_Trece","Gordon AND Hayward -@gordonhayward",
          "Kyle AND Lowry -@Klow7","Demarcus AND Cousins -@boogiecousins",
          "Rudy AND Gobert -@rudygobert27","Mike AND Conley -@mconley11",
          "Kyrie AND Irving -@KyrieIrving","Klay AND Thompson -@KlayThompson",
          "Isaiah AND Thomas -@isaiahthomas","Damian AND Lillard -@Dame_Lillard",
          "Lamarcus AND Aldridge -@aldridge_12","Demar AND DeRozan -@DeMar_DeRozan",
          "Blake AND Griffin -@blakegriffin32","Kemba AND Walker -@KembaWalker",
          "AL AND Horford -@Al_Horford","DeAndre AND Jordan -@DeAndre",
          "Marc AND Gasol -@MarcGasol","Karl-Anthony AND Towns -@KarlTowns",
          "Nikola AND Jokic -@JokicNikola15","Khris AND Middleton -@Khris22m",
            "Kevin AND Love -@kevinlove","CJ AND McCollum -@CJMcCollum",
            "Kristaps AND Porzingis -@kporzee","Carmelo AND Anthony -@carmeloanthony",
            "Hassan AND Whiteside -@youngwhiteside","Bradley AND Beal -@RealDealBeal23",
            "Steven AND Adams -@RealStevenAdams","Andre AND Drummond -@AndreDrummond",
            "Brook AND Lopez -@RealBrookLopez","Derrick AND Favors -@dfavors14",
            "Paul AND Millsap -@Paulmillsap4","Andrew AND Wiggins -@22wiggins",
            "Joel AND Embiid -@JoelEmbiid","Devin AND Booker -@DevinBook",
            "Eric AND Bledsoe -@EBled2","Goran AND Dragic -@Goran_Dragic",
            "Miles AND Turner -@milesturner19","Ricky AND Rubio -@rickyrubio9",
            "Lonzo AND Ball -@ZO2_","Ben AND Simmons -@BenSimmons25",
            "Jayson AND Tatum -@jaytatum0","Enes AND Kanter -@Enes_Kanter",
            "Victor AND Oladipo -@VicOladipo","Dwyane AND Wade -@DwyaneWade",
            "Jaylen AND Brown -@FCHWPO","Kyle AND Kuzma -@kylekuzma",
            "Manu AND Ginobili -@manuginobili","Dirk AND Nowitzki -@swish41"]

'''
count = 0
file = open('text_large_dataset/merged.txt','w',encoding='utf-8')

for i in range(60):
    print("processing "+str(i)+"th player")
    data = open("text_large_dataset/"+str(i)+".txt",'r',encoding='utf-8').read()
    data = data.split("\n////\n")
    for j in range(len(data)):
        text = data[j]
        count = count + 1
        file.write(text)
        file.write("\n")
        file.write("///")
        file.write("\n")
file.close()
print(count)
'''

'''
import math
word_frequency = []
word_inverse = []
with open('text_large_dataset/cleaned_dict.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    word_frequency = list(reader)

with open('text_large_dataset/cleaned_dict_tfidf.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    word_inverse = list(reader)
#print(word_frequency)
#print(word_inverse)
tf_idf = []
for i in range(344):
    new_word = []
    tf = (float(word_frequency[i*2][1])+1.0)/10183141
    idf = math.log10(585240.0/(float(word_inverse[i*2][1])+1.0))
    new_word.append(word_frequency[i*2][0])
    new_word.append(tf*idf)
    tf_idf.append(new_word)
from operator import itemgetter, attrgetter
tf_idf = sorted(tf_idf, key=itemgetter(1, 0))
print(tf_idf)
'''
'''
basketball_dict = []
with open('text_large_dataset/basketball_dict.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    the_dict = list(reader)
    for element in the_dict:
        basketball_dict.append(element[0])
#print(basketball_dict)
for i in range(60):
    data = open('text_cleaned_dataset/'+str(i)+'.txt','r',encoding='utf-8').read()
    data = data.split("\n////\n")
    #count = 0
    print(i)
    file1 = open('text_cleaned_dataset/basketball_related/'+str(i)+'.txt','w',encoding='utf-8')
    file2 = open('text_cleaned_dataset/basketball_unrelated/'+str(i)+'.txt','w',encoding='utf-8')
    for j in range(len(data)):
        text = data[j].split(" ")
        flag = 0
        for word in text:
            if word in basketball_dict:
                file1.write(data[j])
                file1.write("\n")
                file1.write("///")
                file1.write("\n")
                flag = 1
                break
        if flag == 0:
            file2.write(data[j])
            file2.write("\n")
            file2.write("///")
            file2.write("\n")
'''
'''

import preprocessor as p
import string
p.set_options(p.OPT.URL, p.OPT.MENTION,p.OPT.HASHTAG,p.OPT.RESERVED,p.OPT.EMOJI,p.OPT.NUMBER)

for i in range(60):
    print(i)
    data = open('text_cleaned_dataset/basketball_related/cleaned/'+str(i)+'.txt','r',encoding='utf-8').read()
    data = data.split("\n///\n")
    file = open('text_cleaned_dataset/basketball_related/cleaned_/'+str(i)+'.txt','w',encoding='utf-8')
    for j in range(len(data)):
        str_ = data[j]
        #str_ = p.clean(str_)
        #for s in string.punctuation:
        #    str_ = str_.replace(s,'')
        the_str = ""
        str_array = str_.split(" ")
        player_array = players[i].split(" ")
        for j in range(len(player_array)):
            player_array[j] = player_array[j].lower()
        for word in str_array:
            if word.lower() not in player_array:
                the_str = the_str + word.lower()
                the_str = the_str + " "
        file.write(the_str)
        file.write("\n")
        file.write("///")
        file.write("\n")
'''


'''
for i in range(60):
    print(i)
    player = players[i].split(" ")[3][2:]
    f = open('user/'+player+'_tweets.csv','r',encoding='utf-8')
    file = open('user/cleaned/'+str(i)+'.csv', 'w',encoding='utf-8')
    reader = csv.reader(f)
    writer = csv.writer(file)
    writer.writerow(["created_at","text"])
    for row in reader:
        if len(row)>0 and row[2]!="text":
            time = row[1]
            str_ = row[2][2:]
            str_ = str_.encode('utf-8').decode('utf-8')
            str_ = p.clean(str_)
            for s in string.punctuation:
                str_ = str_.replace(s,'')
            new_data = [time,str_]
            writer.writerow(new_data)
'''      
    
        
#print(data[400])
#str_ = p.clean(data[400])

#import string
#for s in string.punctuation:
#  str_ = str_.replace(s,'')
        

'''
data = open("text_large_dataset/"+"59"+".txt",'r',encoding='utf-8').read()
data = data.split("\n////\n")
print(len(data))
count = 0
for text in data:
    text = text.split(" ")
    for word in text:
        if word in basketball_dict:
            count = count + 1
            break
print(count)
'''
        

'''
file = open('whole_emotion_dict.txt',encoding='utf-8').read() 
words = file.split("\n")
count = 0
for i in range(11135):
    text = data[i]["text"]
    sentence = text.split(" ")
    for word in sentence:
        if word in words:
            count = count + 1
            break
print(count)



file = open('testfile.txt','w',encoding='utf-8') 
for i in range(11135):
    text = data[i]['text']
    sentence = text.split(" ")
    towrite = ""
    for word in sentence:
        if word in words:
            towrite = towrite + word + " "
    file.write(towrite)
    #print(text)
file.close()
'''
'''
str_tomerged = ""
for i in range(60):
    path = "text_cleaned_dataset/" + str(i) + ".txt"
    data = open("text_large_dataset/"+str(i)+".txt",'r',encoding='utf-8').read()
    documents = data.split("\n////\n")
    print(i)
    with open(path, 'w',encoding='utf-8') as outfile1:
        for j in range(len(documents)):
            doc = documents[j].split(" ")
            if doc[0]!="rt" and doc[0]!="RT":
                outfile1.write(documents[j])
                outfile1.write("\n")
                outfile1.write("////")
                outfile1.write("\n")
#print(str_tomerged)
'''

'''
from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

r = Rake('english') # To use it in a specific language supported by nltk.

# If you want to provide your own set of stop words and punctuations to
# r = Rake(<list of stopwords>, <string of puntuations to ignore>)

r.extract_keywords_from_text(str_tomerged)

print(r.get_ranked_phrases_with_scores()) # To get keyword phrases ranked highest to lowest.
'''
'''
words = []
with open("text_large_dataset/"+"cleaned_dict"+".csv",'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    r = list(reader)
    for word in r:
        if len(word)>1:
            words.append(word[0])
#print(words)
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
word_count = 0
document_count = []
for i in range(344):
    document_count.append(0)
for i in range(len(documents)):
    print("processing "+str(i)+" document")
    clean_text = tknzr.tokenize(documents[i])
    word_count = word_count + len(clean_text)
    for j in range(344):
        if words[j] in clean_text:
            document_count[j] = document_count[j] + 1
print(word_count)
tf_idf = []
for i in range(344):
    new_word = []
    new_word.append(words[i])
    new_word.append(document_count[i])
    tf_idf.append(new_word)
with open("text_large_dataset/"+"cleaned_dict_tfidf"+".csv", 'w',encoding='utf-8') as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(tf_idf)
'''


sentiment = []
votes = []
vote = 0
number = 0
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
sid = SIA()
for i in range(60):
    print("processing "+str(0)+"th player")
    
    data = open("text_cleaned_dataset/basketball_related/cleaned_/"+str(i)+".txt",'r',encoding='utf-8').read()
    data = data.split("\n///\n")
    #text = data[0]
    #print(players[10])
    count = 0
    nega = 0
    count_ = 0
    for j in range(len(data)):
        text = data[j]
        ss = sid.polarity_scores(text)
        if ss["compound"] > 0:
            count = count + 1
            count_ = count_ + ss["compound"]
        if ss["compound"] < 0:
            nega = nega + 1
            count_ = count_ + ss["compound"]
            #print(text)
    #print(len(data))
    #print(count)
    #print(nega)
    #print((count+0.0)/len(data))
    #print((count+0.0)/(count+nega))
    sentiment.append((count_+0.0)/len(data))
    #sentiment.append(len(data))
    votes.append(len(data))
    #vote = vote + len(data)
    number = number + len(data)
for i in range(60):
   sentiment[i] = (sentiment[i]*0.3 + ((votes[i]+0.0)/number)*0.7)/2
#print(sentiment)
    
import numpy as np
dictionary = dict(zip(sentiment, players))
dictionary_ = dict(zip(votes, players))
sentiment.sort()
votes.sort()
for i in range(60):
    #print(dictionary.get(sentiment[i]) + " " + str(sentiment[i]))
    print(dictionary.get(sentiment[i]) + " " + str(sentiment[i]))
#print(vote)



'''
import nltk
from nltk.tokenize import TweetTokenizer
stopword = nltk.corpus.stopwords.words("english")
print(stopword)
tknzr = TweetTokenizer()
clean_text = tknzr.tokenize(data)
#print(nltk.pos_tag(clean_text))
fdist1 = nltk.FreqDist(clean_text)
elements = fdist1.most_common(1000)
import csv

with open("text_large_dataset/"+"most_frequent_1000_dict"+".csv","w",encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerows(elements)
'''



'''
import numpy as np
dictionary = dict(zip(sentiment, players))
dictionary_ = dict(zip(votes, players))
sentiment.sort()
votes.sort()
for i in range(60):
    #print(dictionary.get(sentiment[i]) + " " + str(sentiment[i]))
    print(dictionary_.get(votes[i]) + " " + str(votes[i]))
print(vote)
  '''  


'''
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'testfile.txt'),encoding='utf-8').read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")


# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
'''