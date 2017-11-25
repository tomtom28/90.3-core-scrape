import requests as req

import config


# Import API Keys
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
SPOTIFY_USER_ID = config.SPOTIFY_USER_ID
SPOTIFY_PLAYLIST_ID = config.SPOTIFY_PLAYLIST_ID


# test data
track_id = '6QgjcU0zLnzq5OrUoSZ3OK'
artist = 'STRFKR'
song='Never Ever'


# Push to Playlist
def push_track_to_spotify(track_id):
    pass



# Search Song & Artist for Track ID
def get_spotify_track_id(artist,song):
    print(artist)
    print(song)
    url = "https://api.spotify.com/v1/search?q=" + "artist:" + artist + "%20" + "track:" + song + "&type=track"
    res = req.get(url)
    print(res)




get_spotify_track_id(artist,song)
