import time
from flask import Flask, request, redirect, session, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'
app.secret_key = 'nheVscB52730-HBg^&cjn$cjs-0299jusdHmkH4'

CLIENT_ID = '################################'
CLIENT_SECRET = '################################'
REDIRECT_URI = 'http://localhost:5000/callback'


def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope='user-top-read playlist-modify-public playlist-modify-private',
        cache_path=".spotify_caches",
        show_dialog=True
    )



@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('most_played_songs'))

@app.route('/most-played-songs')
def most_played_songs():
    session['token_info'], authorized = get_token(session)
    session.modified = True
    if not authorized:
        return redirect('/')
    
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    
    top_tracks = sp.current_user_top_tracks(time_range='short_term', limit=20)
    playlists = sp.current_user_playlists()
    playlist_id = None
    for playlist in playlists['items']:
        if playlist['name'] == 'most played songs':
            playlist_id = playlist['id']
            break
        if not playlist_id:
            user_id = sp.current_user()['id']
            playlist = sp.user_playlist_create(user=user_id, name='most played songs', public=False)
            playlist_id = playlist['id']
            
        existing_tracks = sp.playlist_tracks(playlist_id)
        existing_track_ids = {item['track']['id'] for item in existing_tracks['items']}
        
        new_tracks = [track['id'] for track in top_tracks['items'] if track['id'] not in existing_track_ids]
        if new_tracks:
            sp.playlist_add_items(playlist_id, new_tracks)
            
        return 'Most played songs playlist has been updated!'
    
def get_token(session):
    token_valid = False
    token_info = session.get('token_info', {})
    
    if not (session.get('token_info', False)):
        token_info = create_spotify_oauth().get_cached_token()
        
    if token_info:
        now = int(time.time())
        is_expired = token_info['expires_at'] - now < 60
        if is_expired:
            sp_oauth = create_spotify_oauth()
            token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

    token_valid = True
    return token_info, token_valid

if __name__ == '__main__':
    app.run(debug=True)
