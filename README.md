# Spotify Tweet Bot
This is a Spotify Tweet Bot which gets your currently playing song from Spotify and tweets it to your Twitter account.

# Installation
Clone this repository or download the .zip file.
Once it has downloaded you will need to add your own authentication keys and tokens to the SpotifyCredentials.py and TwitterCredentials.py files

The authentication tokens and keys for Spotify can be found when you create an app on https://developer.spotify.com/

The authetication tokens and keys for Twitter can be found when you create an app on https://developer.twitter.com/

You will need to import [Tweepy](https://www.tweepy.org/) and [Spotipy](https://spotipy.readthedocs.io/en/latest/#installation) to run this program.

As there is a problem with the current build of spotipy you will also need to run this command to get the latest build:

pip install git+https://github.com/plamere/spotipy.git --upgrade

This will eliminate any attribute errors when getting the user playback.

# Running the program

To run this program simply type in the terminal: python SpotifyTweet.py

If you are python3 (which you should be) execute with: python3 SpotifyTweet.py


## Author

* **Haran Lakha** - [GitHub](https://github.com/Haran43) - [Twitter](https://twitter.com/haranlakha)
