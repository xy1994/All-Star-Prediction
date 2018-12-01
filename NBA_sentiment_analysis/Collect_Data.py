# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:01:11 2018

@author: LENOVO
"""

import tweepy
import json
import time
from tweepy import OAuthHandler
 
consumer_key = '5G2eov72WtlRhJFrD9jnGLjL4'
consumer_secret = 'vhSk1Zx4QwC4RRhu5CNyNTNTYH1GWKoZJN6fWHT2WIyPKA2dC7'
access_token = '825807186731352064-UirWk3ZQ2HXN00Ea7rvZgOtqEIrTGg6'
access_secret = 'u3TjqmK5S4drCQRj0tGyeQwvI5ROi7BPvpRdq0xSR5DGi'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
query = (["Lebron AND James -@KingJames","Kawhi AND Leonard -@kawhileonard",
          "Kevin AND Durant -@KDTrey5","James AND Harden -@JHarden13",
          "Russell AND Westbrook -@russwest44","Stephen AND Curry -@StephenCurry30",
          "Giannis Antetokounmpo -@Giannis_An34","Chris AND Paul -@CP3",
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
          "Marc AND Gasol -@MarcGasol","Karl-Anthony AND Towns -@KarlTowns"])
query_1 = (["Nikola AND Jokic -@JokicNikola15","Khris AND Middleton -@Khris22m",
            "Kevin AND Love -@kevinlove","CJ AND McCollum -@CJMcCollum",
            "Kristaps AND Porzingis -@kporzee","Carmelo AND Anthony -@carmeloanthony",
            "Hassan AND Whiteside -@youngwhiteside","Bradley AND Beal -@RealDealBeal23",
            "Steven AND Adams -@RealStevenAdams","Andre AND Drummond -@AndreDrummond",
            "Brook AND Lopez -@RealBrookLopez","Derrick AND Favors -@dfavors14",
            "Paul AND Millsap -@Paulmillsap4","Andrew AND Wiggins -@22wiggins",
            "Joel AND Embiid -@JoelEmbiid","Devin AND Booker -@DevinBook",
            "Eric AND Bledsoe -@EBled2","Goran AND Dragic -@Goran_Dragic",
            "Miles AND Turner -@milesturner19","Ricky AND Rubio -@rickyrubio9"])
query_2 = (["Lonzo AND Ball -@ZO2_","Ben AND Simmons -@BenSimmons25",
            "Jayson AND Tatum -@jaytatum0","Enes AND Kanter -@Enes_Kanter",
            "Victor AND Oladipo -@VicOladipo","Dwyane AND Wade -@DwyaneWade",
            "Jaylen AND Brown -@FCHWPO","Kyle AND Kuzma -@kylekuzma",
            "Manu AND Ginobili -@manuginobili","Dirk AND Nowitzki -@swish41"])

query_ = (["Lebron AND James -@KingJames","Kawhi AND Leonard -@kawhileonard",
          "Kevin AND Durant -@KDTrey5","James AND Harden -@JHarden13",
          "Russell AND Westbrook -@russwest44","Stephen AND Curry -@StephenCurry30",
          "Giannis Antetokounmpo -@Giannis_An34","Chris AND Paul -@CP3",
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
            "Manu AND Ginobili -@manuginobili","Dirk AND Nowitzki -@swish41"])
query_partial = (["James -@KingJames -Lebron -Harden","Leonard -@kawhileonard -Kawhi",
          "Durant -@KDTrey5 -Kevin","Harden -@JHarden13 -James",
          "Westbrook -@russwest44 -Russell","Curry -@StephenCurry30 -Stephen",
          "Antetokounmpo -@Giannis_An34 -Giannis","Paul -@CP3 -Chris -Millsap -George",
          "Butler -@JimmyButler -Jimmy","Davis -@AntDavis23 -Anthony",
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
            "Manu AND Ginobili -@manuginobili","Nowitzki -@swish41 -Dirk"])

import csv
basketball_dict = []
with open('text_large_dataset/core_dict.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    the_dict = list(reader)
    for element in the_dict:
        basketball_dict.append(element[0])
#print(basketball_dict)

filter_query = "("
for i in range(len(basketball_dict)):
    filter_query = filter_query + basketball_dict[i]
    if i!=len(basketball_dict)-1:
        filter_query = filter_query + " OR "
filter_query = filter_query + ")"
#print(filter_query)
#print(len(basketball_dict))
#st = query_partial[59] +" "+filter_query
#print(st)
#st = "(Nowitzki) (game OR NBA) -@swish41 -Dirk"



api = tweepy.API(auth)
count = 0
query_3 = ["Manu AND Ginobili"]
for i in range(10):
    path = "text_large_dataset_2/" + str(i+21) + ".txt"
    st = query_[i+21] #+" "+filter_query #+ " -#NBAVote -filter:retweets"
    with open(path, 'w',encoding='utf-8') as outfile1:
        for tweet in tweepy.Cursor(api.search,q=st,since="2018-02-10",until="2018-02-17",result_type='recent',include_entities=True,wait_on_rate_limit=True,wait_on_rate_limit_notify=True,lang="en").items():
    # Process a single status
            '''
            text = tweet._json["text"]
            text_word = text.split(" ")
            for word in text_word:
                if word in basketball_dict:
            '''
                    #outfile1.write(tweet._json["text"])
            outfile1.write(tweet._json["text"])
            outfile1.write("\n")
            outfile1.write("////")
            outfile1.write("\n")
            count = count + 1
            if(count%100==0):
                print(count)
    outfile1.close()
