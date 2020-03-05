import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import tweepy
import time

from TwitterCredentials import *
from SpotifyCredentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri)


spotify = spotipy.Spotify(auth=token)

while True:
	try:
		current_track = spotify.current_user_playing_track()
		current_album_id = current_track['item']['album']['id']
		current_track_id = current_track['item']['id']
		if current_track_id != None and current_album_id != None:
			api.update_status("#NowListening to " + current_track['item']['name'] + " by " + current_track['item']['album']['artists'][0]['name'] + '\n' +  str(current_track['item']['external_urls']['spotify']))
			break
		else:
			print("Same song is playing ", current_track['item']['name'])
			time.sleep(30)
			continue
	except spotipy.client.SpotifyException:
		token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri)
		spotify = spotipy.Spotify(auth=token)
		continue
	except (tweepy.TweepError, TypeError) as e:
		if e.api_code == 187:
			print("There's a duplicate message on Twitter.")
		else:
			raise error
			pass
	except:
		print("No Song is playing.")
		time.sleep(30)
		continue


while True:
	try:
		new_track = spotify.current_user_playing_track()
		if current_track_id != None and current_album_id != None:
			if (new_track['item']['id'] != current_track_id or new_track['item']['album']['id'] != current_album_id):
				api.update_status("#NowListening to " + current_track['item']['name'] + " by " + current_track['item']['album']['artists'][0]['name'] + '\n' +  str(current_track['item']['external_urls']['spotify']))
				current_album_id = new_track['item']['album']['id']
				current_track_id = new_track['item']['id']
		else:
			print("Same song is playing ", current_track['item']['name'])
			time.sleep(30)
			continue
	except spotipy.client.SpotifyException:
		token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri)
		spotify = spotipy.Spotify(auth=token)
		continue
	except (tweepy.TweepError, TypeError) as e:
		if error.api_code == 187:
			print("There's a duplicate message on Twitter.")
		else:
			raise error
			pass
	except:
		print("No Song is playing.")
		time.sleep(30)
		continue
