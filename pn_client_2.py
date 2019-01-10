from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os

pnconfig = PNConfiguration()

pnconfig.publish_key = 'enter your pubnub publish key here'
pnconfig.subscribe_key = 'enter your pubnub subscribe key here'
pnconfig.ssl = True

pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass
    def status(self, pubnub, status):
        pass
    def message(self, pubnub, message):
        print "from device 1: " + message.message

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()

## publish a message
while True:
    msg = raw_input("Input a message to publish: ")
    if msg == 'exit': os._exit(1)
    pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)
