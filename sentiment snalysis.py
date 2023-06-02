# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:25:42 2023

@author: ayesh
"""

import pandas as pd
import os
import numpy as np
os.chdir("C:/Users/ayesh/Documents/twitter dataset")
mydata=pd.read_csv("twitter_training.csv")
mydata.head()
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer
senti_analysis=SentimentIntensityAnalyzer()
senti_analysis.polarity_scores(mydata.iloc[50,1])
print(mydata.iloc[50,1])
mydata["score"]=mydata["Borderlands"].apply(lambda x:senti_analysis.polarity_scores(x))
mydata["compound_score"] = mydata["score"].apply(lambda x: x["compound"])
mydata
mydata["positive_negative"]=mydata["compound_score"].apply(lambda x:np.where(x>0,"Positive","Negative"))
mydata["positive_negative"].value_counts()
positive_data=mydata.query("positive_negative=='positive'")
positive = 10
print(positive)

