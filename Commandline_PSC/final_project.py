from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

import re, string, random
import nltk
nltk.download('twitter_samples')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')

#first part of our code
def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token
def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)
        
def call(filename):

    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')
    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

    stop_words = stopwords.words('english')

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    all_pos_words = get_all_words(positive_cleaned_tokens_list)

    freq_dist_pos = FreqDist(all_pos_words)
    #print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset

    random.shuffle(dataset)

    train_data = dataset[:7000]
    test_data = dataset[7000:]

    classifier = NaiveBayesClassifier.train(train_data)

    #print("Accuracy is:", classify.accuracy(classifier, test_data))

    #print(classifier.show_most_informative_features(10))

    with open(filename, 'r') as f1:
       fread = f1.read()
       fsentece = fread.split('\n')
       for custom_tweet in fsentece:
            custom_tokens = remove_noise(word_tokenize(custom_tweet))
            print( classifier.classify(dict([token, True] for token in custom_tokens)),custom_tweet)

            
# second  part of our project

def sentiment(filename):
  with open(filename, 'r') as f1:
   fread = f1.read()
   fsentece = fread.split('\n')
   #print(fsentece)
   for ftokenized in fsentece:
    ppos = 0
    pneg = 0

    #print(pneg)

    with open("C:\\Users\\Lenovo\\projects\\Commandline_PSC\\positive.txt", 'r') as pos:
       pos_read = pos.read()

       pos_read = pos_read.split('\n')
       # print(pos_read)
       i=ftokenized
       i = i.split(' ')
       for j in i:
                if (j in pos_read):
                   # print(j,'\tpos')
                    ppos += 1
        #print(ppos)
    with open('C:\\Users\\Lenovo\\projects\\Commandline_PSC\\negative.txt','r') as neg:
     neg_read=neg.read()
     neg_read=neg_read.split('\n')
     #print(neg_read)
     i=ftokenized
     i = i.split(' ')
     #print(i)
     for j in i:
            if (j in neg_read):
                #print(j)
                if(j=='not' or j=='Not'):
                    if(ppos>0):
                        ppos-=1
                    else:
                        pneg-=2
              #  print(j,"\tneg")
                pneg += 1
    total=ppos+pneg

    if(ppos>pneg):
      print('POSITIVE',end="\t")
    elif(ppos<pneg):
      print('NEGATIVE',end="\t")
    else:
      print("NEUTRAL",end="\t")
    print(ftokenized, end="\n")
inp=input('Enter 1 for new sentiment entry ,Otherwise we will show you analysis of available data\n')
if (inp == '1'):
    with open("C:\\Users\\Lenovo\\projects\\Commandline_PSC\\file1.txt",'a') as inp:
        sentiments = input('Enter lines (Do not press unless and until your sentiment get finished)')
        inp.write("\n"+sentiments)

#path = "C:\\Users\\Lenovo\\Desktop\\project1\\file1.txt"           
print("\nStandard Method\n")

call("C:\\Users\\Lenovo\\projects\\Commandline_PSC\\file1.txt")
print("\nNormal Method\n")
sentiment('C:\\Users\\Lenovo\\projects\\Commandline_PSC\\file1.txt')
