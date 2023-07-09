import pandas as pd
import lyricsgenius

# Load the dataset
df = pd.read_csv('unseen3post_data.csv')

# Initialize Genius API
genius = lyricsgenius.Genius('P68M9tK2zDbkgno9LgA_8nAUgYCBxK7G9C-LtElWR9g1BGYDgFcjCPezEZo4b2vP', timeout=10)

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Extract song and artist names
    song_name = row['Single']
    artist_name = row['Artist(s)']
    
    # Search for the song on Genius
    try:
        song = genius.search_song(song_name, artist_name)
        if song is not None:
            # Get the lyrics and add it to the dataframe
            df.at[index, 'Lyrics'] = song.lyrics
        else:
            df.at[index, 'Lyrics'] = 'Lyrics not found'
    except Exception as e:
        print(f'Error occurred for song: {song_name} by {artist_name}')
        print(e)

# Save the dataframe with lyrics to a new CSV file
df.to_csv('unseen3_df.csv', encoding='utf-8', index=False)
