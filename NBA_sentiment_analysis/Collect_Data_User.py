# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:16:03 2018

@author: LENOVO
"""

#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = '5G2eov72WtlRhJFrD9jnGLjL4'
consumer_secret = 'vhSk1Zx4QwC4RRhu5CNyNTNTYH1GWKoZJN6fWHT2WIyPKA2dC7'
access_key = '825807186731352064-UirWk3ZQ2HXN00Ea7rvZgOtqEIrTGg6'
access_secret = 'u3TjqmK5S4drCQRj0tGyeQwvI5ROi7BPvpRdq0xSR5DGi'


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	#outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in alltweets]
	
	#write the csv	
	with open('user/%s_tweets.csv' % screen_name, 'w',encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
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
    for i in range(60):
        str_ = query_[i].split(" ")
        str_player = str_[len(str_)-1]
        str_player = str_player[2:]
        #print(str_player)
        get_all_tweets(str_player)