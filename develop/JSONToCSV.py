__author__ = 'Shashank'
import json
tweets = []

for line in open('ProjectData.txt'):
  try:
    tweets.append(json.loads(line))
  except:
    pass

print len(tweets)

tweet = tweets[0]

print tweet.keys()

ids = [tweet['id_str'] for tweet in tweets]
texts = [tweet['text'] for tweet in tweets]
times = [tweet['created_at'] for tweet in tweets]

print tweet['user'].keys()

screen_names = [tweet['user']['screen_name'] for tweet in tweets]
names = [tweet['user']['name'] for tweet in tweets]

print tweet['entities']

for tweet in tweets:
  if tweet['entities']['user_mentions']:
    print tweet['entities']['user_mentions']
    break

mentions1 = [(T['entities']['user_mentions'][0]['screen_name'] if len(T['entities']['user_mentions']) >= 1 else None) for T in tweets]
mentions2 = [(T['entities']['user_mentions'][1]['screen_name'] if len(T['entities']['user_mentions']) >= 2 else None) for T in tweets]
mentions3 = [(T['entities']['user_mentions'][2]['screen_name'] if len(T['entities']['user_mentions']) >= 3 else None) for T in tweets]
hashtags1 = [(T['entities']['hashtags'][0]['text'] if len(T['entities']['hashtags']) >= 1 else None) for T in tweets]
hashtags2 = [(T['entities']['hashtags'][1]['text'] if len(T['entities']['hashtags']) >= 2 else None) for T in tweets]
hashtags3 = [(T['entities']['hashtags'][2]['text'] if len(T['entities']['hashtags']) >= 3 else None) for T in tweets]
urls1 = [(T['entities']['urls'][0]['expanded_url'] if len(T['entities']['urls']) >= 1 else None) for T in tweets]
urls2 = [(T['entities']['urls'][1]['expanded_url'] if len(T['entities']['urls']) >= 2 else None) for T in tweets]

print tweet['geo']

lats = [(T['geo']['coordinates'][0] if T['geo'] else None) for T in tweets]
lons = [(T['geo']['coordinates'][1] if T['geo'] else None) for T in tweets]

print tweet['place']
place_names = [(T['place']['full_name'] if T['place'] else None) for T in tweets]
place_types = [(T['place']['place_type'] if T['place'] else None) for T in tweets]


out = open('D:\\tweets.csv', 'w')
print >> out, 'id,created,text,screen_name,name,mention_1,mention_2,mention_3, hashtag_1,hashtag_2, hashtag_3, url 1,url 2,lat,lon,place name,place type'
rows = zip(ids, times, texts, screen_names, names, mentions1, mentions2, mentions3, hashtags1, hashtags2, hashtags3, urls1, urls2, lats, lons, place_names, place_types)

from csv import writer
csv = writer(out)

for row in rows:
    values = [(value.encode('utf8') if hasattr(value, 'encode') else value) for value in row]
    csv.writerow(values)

out.close()

print tweet.keys()