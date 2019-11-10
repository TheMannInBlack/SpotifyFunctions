'''Created by Themanninblack with help from online sources and Reddit'''
import spotipy
import spotipy.util as util
import sys
import pandas as pd
import numpy as np

Offset = np.arange(0,1000, 50).tolist()

def Liked_Songs():
    username = 'username'
    client_id = 'numbersnletters'
    client_secret = 'secretnumbersnletters'
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'user-library-read'
    
    token = util.prompt_for_user_token(username, scope = scope, client_id = client_id, client_secret = client_secret, redirect_uri = redirect_uri)
    sp = spotipy.Spotify(auth=token)
    df = pd.DataFrame(columns = ('Title', 'Artists'))
    T = []
    A = []
    for i in Offset:
        results = sp.current_user_saved_tracks(limit = 50, offset = i)
        
        for item in results['items']:
                track = item['track']
                track['name'] + '/' + track['artists'][0]['name']
                T.append(track['name'])
                A.append(track['artists'][0]['name'])
    df['Title'] = T
    df['Artists'] = A
    df.to_csv('Finally.csv') 
Liked_Songs()


