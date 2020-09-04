"""Created by Themanninblack with help from online sources and Reddit."""
from datetime import date

import numpy as np
import pandas as pd

import spotipy
import spotipy.util as util

today = str(date.today())
# Only 50 songs can be donwloaded per request. The second number should be the
# total number of songs in your library; to play it safe,
# round up to the nearest 50.
offset = np.arange(0, 1000, 50).tolist()


def liked_songs():
    """Write liked songs from Spotify to SpotifySavedSongs.csv."""
    username = 'username'
    client_id = 'numbersnletters'
    client_secret = 'secretnumbersnletters'
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'user-library-read'

    token = util.prompt_for_user_token(username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)
    sp = spotipy.Spotify(auth=token)
    df = pd.DataFrame(columns=('Title', 'Artists'))
    track_title = []
    artist = []
    album = []
    for i in offset:
        results = sp.current_user_saved_tracks(limit=50, offset=i)

        for item in results['items']:
            track = item['track']
            track['name'] + '/' + track['artists'][0]['name']
            track_title.append(track['name'])
            artist.append(track['artists'][0]['name'])
            album.append(track['album']['name'])

    df['Title'] = track_title
    df['Artists'] = artist
    df['Album'] = album

    df.to_csv(today + 'SpotifySavedSongs.csv')


if __name__ == 'main':
    liked_songs()
