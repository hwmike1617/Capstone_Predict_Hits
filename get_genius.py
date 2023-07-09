import pandas as pd
import lyricsgenius

# Initialize Genius API
genius = lyricsgenius.Genius('P68M9tK2zDbkgno9LgA_8nAUgYCBxK7G9C-LtElWR9g1BGYDgFcjCPezEZo4b2vP', timeout=10)

song_name='Gone'
artist_name="'NSYNC"

song = genius.search_song(song_name, artist_name)

print(song)