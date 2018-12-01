# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:11:28 2018

@author: LENOVO
"""

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

partial_names = []

for i in range(60):
    string = players[i].split(" ")
    partial_names.append(string[0].lower())
    partial_names.append(string[2].lower())
#print(partial_names)
stopword_1 = []
with open('stopword_list.txt', 'r',encoding="utf-8") as f:
    wordlist = f.readlines()
    for line in wordlist:
        stopword_1.append(line.strip('\n'))
        
#print(stopword_1)
    
import csv
import nltk
import string
with open('text_large_dataset/most_frequent_1000_dict.csv', 'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    my_dict = list(reader)
stopword_2 = nltk.corpus.stopwords.words("english")
stop = ["@","#","http"]
cleaned_wordlist = []
for i in range(1000):
    newword = []
    word = my_dict[i*2]
    if (word[0].isalpha()) and (word[0].lower() not in stopword_2) and (word[0].lower() not in partial_names) and (word[0].lower() not in stopword_1):
        flag = 0
        for j in range(len(stop)):
            if word[0].startswith(stop[j])==True:
                flag = 1
                break
        if flag == 0:
            translator=str.maketrans('','',string.punctuation)
            newstr=word[0].translate(translator)
            if len(newstr)!=0:
                newword.append(word[0])
                newword.append(word[1])
                cleaned_wordlist.append(newword)
                
print(cleaned_wordlist)
print(len(cleaned_wordlist))

with open("text_large_dataset/"+"cleaned_dict"+".csv","w",encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerows(cleaned_wordlist)


            