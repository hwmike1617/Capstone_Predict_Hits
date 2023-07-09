from dotenv import load_dotenv
import os
import base64
import requests
from requests import post, get
import json
import pandas as pd

load_dotenv()

df = pd.read_csv('unseen3_data.csv', encoding='utf-8')

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

# Define artists as an empty list
artists = []

def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        'Content-Type': "application/x-www-form-urlencoded"
    }
    data = {'grant_type': "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}

def search_for_artist(token, artist_name):
    # Set base URL and headers
    base_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    # Set query parameters for artist search
    params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 1
    }

    # Send GET request to Spotify API for artist search
    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  # Raise error if response is not successful
        data = response.json()
        if 'artists' in data and 'items' in data['artists']:
            artists = data['artists']['items']
            if len(artists) > 0:
                return artists[0]  # Return first artist found
    except requests.exceptions.RequestException as e:
        print(f'Request Exception: {e}')
    except KeyError as e:
        print(f'KeyError: {e}')
    except Exception as e:
        print(f'Error: {e}')

    return None  # Return None if no artist found or error occurred


def get_track_id(token, track_name, artist_id):
    url = f"https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f'?q={track_name}&type=track&limit=1&market=US'
    query_url = url + query
    result = get(query_url, headers=headers)
    try:
        json_result = json.loads(result.content)["tracks"]["items"]
    except KeyError:
        print(f'No track with this name: "{track_name}"')
        return None
    if len(json_result) == 0:
        print(f'No track with this name: "{track_name}"')
        return None
    for track in json_result:
        if track["artists"][0]["id"] == artist_id:
            return track["id"]
    return None
'''
def get_audio_features(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result
'''
def get_audio_features(token, track_id):
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    if result.ok:
        try:
            json_result = json.loads(result.content)
            return json_result
        except json.JSONDecodeError as e:
            print(f'Error decoding JSON: {e}')
    elif result.status_code == 404:
        print(f'Track not found: {track_id}')
    else:
        print(f'Response error: {result.status_code}')
    return None

token = get_token()

# Loop through DataFrame rows
for index, row in df.iterrows():
    # Get artist name and search for artist
    artist_name = row['Artist(s)']
    result = search_for_artist(token, artist_name)
    # Append artist result to artists list
    artists.append(result)
    if result:
        artist_id = result['id']
        # Get track name and search for track using artist_id
        track_name = row['Single']
        track_id = get_track_id(token, track_name, artist_id)
        if track_id:
            print(f'{track_name} by {artist_name} is found')  # Added line to print track found message
            # Get audio features
            audio_features_dict = get_audio_features(token, track_id)  # Pass token and track_id to function

            # Check if audio_features_dict is not None
            if audio_features_dict is not None:
                # Iterate over audio_features_dict items
                for key, value in audio_features_dict.items():
                    column_name = key
                    df.at[index, column_name] = value
        
                    print(f'Audio features parsed for "{track_name}" by {artist_name}: {audio_features_dict}')
        else:
            print(f'No track ID found for "{track_name}" by {artist_name}')

# Save updated DataFrame to CSV
df.to_csv('unseen3post_data.csv', encoding='utf-8', index=False)
