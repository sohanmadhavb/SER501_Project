__author__ = 'Shashank'
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API
consumer = "tQDPQOVYSvYqrabR9cwra8i4e"
consumer_secret = "pdKdSdsC2den5atlWZYV738yl1h7OAw7M0fJLlJwQUfMN5woJW"

access = "3664606998-kYHoaNnteB4SRwe92NzQdo0okUPfayxoEIKsLjG"
access_secret = "h2MPDg6n4FjD5Bv49Jjj0E1igBL34XVx25liRAif7yyx5"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer, consumer_secret)
    auth.set_access_token(access, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['El Capitan', 'Windows 10'])
