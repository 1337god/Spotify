import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import tweepy

from TwitterCredentials import *
from SpotifyCredentials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
try:
	token = util.prompt_for_user_token(username,
								scope,
								client_id=CLIENT_ID,
								client_secret=CLIENT_SECRET,
								redirect_uri=redirect_uri)


	spotify = spotipy.Spotify(auth=token)
except spotipy.client.SpotifyException:
	main.refresh_token()

while True:
	try:
		current_track = spotify.current_user_playing_track()
		current_album_id = current_track['item']['album']['id']
		current_track_id = current_track['item']['id']

		if current_track_id != None and current_album_id != None:
			api.update_status("Currently playing: " + '\n' + current_track['item']['album']['artists'][0]['name'] + " - " + current_track['item']['name'] + '\n' +  str(current_track['item']['external_urls']['spotify']) + '\n' + "#" + str(current_track['item']['album']['artists'][0]['name']).replace(" ",""))
			break
		else:
			continue
	except (tweepy.TweepError, TypeError) as e:
		pass


while True:
	try:
		current_track1 = spotify.current_user_playing_track()

		if current_track_id != None and current_album_id != None:
			if (current_track1['item']['id'] != current_track_id or current_track1['item']['album']['id'] != current_album_id):
				api.update_status("Currently playing: " + '\n' + current_track1['item']['album']['artists'][0]['name'] + " - " + current_track1['item']['name'] + '\n' +  str(current_track1['item']['external_urls']['spotify']) + '\n' + "#" + str(current_track1['item']['album']['artists'][0]['name']).replace(" ",""))
				current_album_id = current_track1['item']['album']['id']
				current_track_id = current_track1['item']['id']
		else:
			continue
	except (tweepy.TweepError, TypeError) as e:
		pass


		


	
		

	






