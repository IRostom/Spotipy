# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 19:19:26 2019

@author: IRostom
"""

#import os
#import sys
import csv
#import json
import spotipy
#import webbrowser
import spotipy.util as util
#import pandas as pd
#from json.decoder import JSONDecodeError

# Get the username from terminal
username = '6iuco7tfzqz12mumxcly3lgok'
scope = 'user-library-read user-follow-read'

#  prompt for user permission
token = util.prompt_for_user_token(username,scope,client_id='569a9627ae844e7094ddafba2031c673',client_secret='1f8ea26f61284c02b40403eed0f8474b',redirect_uri='https://www.google.com/') # add scope

# Create our spotify object with permissions
spotifyObject = spotipy.Spotify(auth=token)

# User information
user = spotifyObject.current_user()
displayName = user['display_name']
followers = user['followers']['total']
#followed = spotifyObject.current_user_followed_artists()
#albums = spotifyObject.current_user_saved_albums()
usertracks = spotifyObject.current_user_saved_tracks(limit=50)
#print(json.dumps(followed, sort_keys=True, indent=4))
#print(json.dumps(albums, sort_keys=True, indent=4))

#Create a csv file to save the user's favourite tracks' data in it
def create_favorites():
    with open('Favorite_Tracks.csv', 'w') as Tracks_csv:
        writer = csv.writer(Tracks_csv)
        writer.writerow(['Track name', 'Artist', 'Popularity', 'Explicit', 'Track id', 'Duration', 'Album name', 'Album Type', 'danceability',
                         'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
                         'time_signature'])
    Tracks_csv.close()

#Fetch Tracks data from your favourite songs and save it to a CSV file
def update_favorites():
    create_favorites()
    tracks = usertracks['items']
    count = 0
    for track in tracks:
        with open('Favorite_Tracks.csv', 'a') as Tracks_csv:
            # Get track details
            trackname = track['track']['name']
            artist = track['track']['artists'][0]['name']
            popularity = track['track']['popularity']
            explicit = track['track']['explicit']
            trackid = track['track']['id']
            duration = track['track']['duration_ms']
            album = track['track']['album']['name']
            albumtype = track['track']['album']['type']
            # Get track features
            feature = spotifyObject.audio_features(tracks = trackid)
            danceability = feature[0]['danceability']
            energy = feature[0]['energy']
            key = feature[0]['key']
            loudness = feature[0]['loudness']
            mode = feature[0]['mode']
            speechiness = feature[0]['speechiness']
            acousticness = feature[0]['acousticness']
            instrumentalness = feature[0]['instrumentalness']
            liveness = feature[0]['liveness']
            valence = feature[0]['valence']
            tempo = feature[0]['tempo']
            time_signature = feature[0]['time_signature']
            #Save track data
            data = [trackname, artist, popularity, explicit, trackid, duration, album, albumtype,
                    danceability,energy, key, loudness, mode, speechiness, acousticness, instrumentalness,
                    liveness, valence, tempo, time_signature]
            writer = csv.writer(Tracks_csv)
            writer.writerow(data)
        Tracks_csv.close()
        count = count + 1
        print("Track #" + str(count) + ": " + str(trackname) + " Artist : " + str(artist))    
#analysis = spotifyObject.audio_analysis(trackids[0])
#print(json.dumps(analysis, sort_keys=True, indent=4))
#with open('audio features.json', 'x') as json_file:  
#    json.dump(analysis, json_file)

## Loop
while True:
    # Main Menu
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Update favorites list")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    if choice == "0":
        update_favorites()

    if choice == "1":
        break