# coding=utf-8

from features import isMonth
from features import isSrSra

## To print the first sentence of the corpus.
# print(train_sents[0])
def word2features(sent, i):
   word = sent[i][0]
   postag = sent[i][1]
   features = [
       'bias',
       'word=%s' % word,##
       ##'word.isalnum=%s' % word.isalnum(),##
       ##'word.isalpha=%s' % word.isalpha(),##
       ##'word.islower=%s' % word.islower(),##
       ##'word.isspace=%s' % word.isspace(),##
       'word.len=%s' % len(word), ##,
       'word.lower=' + word.lower(),
       'word[-3:]=' + word[-3:],
       'word[-2:]=' + word[-2:],
       'word.isupper=%s' % word.isupper(),
       'word.istitle=%s' % word.istitle(),
       'word.isdigit=%s' % word.isdigit(),
       'word.issrsra=%s' % isSrSra(word),
       'postag=' + postag,
       'postag[:2]=' + postag[:2],
   ]
   if i > 0:
       word1 = sent[i-1][0]
       postag1 = sent[i-1][1]
       features.extend([
           '-1:word=%s' % word1, ##
           ##'-1:word.isalnum=%s' % word.isalnum(),##
           ##'-1:word.isalpha=%s' % word.isalpha(),##
           ##'-1:word.islower=%s' % word.islower(),##
           ##'-1:word.isspace=%s' % word.isspace(),##
           '-1:word.len=%s' % len(word1), ##,
           '-1:word.lower=' + word1.lower(),
           '-1:word.istitle=%s' % word1.istitle(),
           '-1:word.isupper=%s' % word1.isupper(),
           '-1:word.issrsra=%s' % isSrSra(word1),
           '-1:postag=' + postag1,
           '-1:postag[:2]=' + postag1[:2],
       ])
       ##if (word1 == "en") and (word.istitle()):
       ##    features.extend([
       ##        'word=True'
       ##    ])
   else:
       features.append('BOS')

   if i < len(sent)-1:
       word1 = sent[i+1][0]
       postag1 = sent[i+1][1]
       features.extend([
           '+1:word.lower=' + word1.lower(),
           '+1:word.istitle=%s' % word1.istitle(),
           '+1:word.isupper=%s' % word1.isupper(),
           '+1:postag=' + postag1,
           '+1:postag[:2]=' + postag1[:2],
       ])
   else:
       features.append('EOS')

   return features
