### PERSONAL PROJECT NO 2 
# SPOTIFY PROJECT

# Aim and Task:
The goal of the project is to develop and implement a full-fledged software solution that interacts with Spotify's developer API.

#### This project provides for:
1. Learning API integration: Learn how to use the Spotify API to perform various functions such as creating playlists, searching for music, retrieving user data, and implementing playback control functionality.
2. Reading and Understanding Documentation: Develop skills in reading and understanding API documentation in order to effectively use available methods and tools. It also includes an understanding of the authentication and authorization processes required to work with the Spotify API.
3. Front-end and back-end development: Learn to build both client-side and server-side components. This includes designing and developing the user interface, as well as creating the server logic for processing data and making API requests.
4. Authentication and Authorization Methods: Learn how to implement the OAuth 2.0 authentication process to ensure secure access to user data and API functionality.
5. Data processing and analysis: Develop skills to process and analyze data obtained from the Spotify API, such as analysis of users' playback history, to offer personalized recommendations and other useful functionality.
6. Project management and version control: Learn to use project management tools and version control systems (such as Git) to effectively organize the development process, track changes, and ensure code quality.
7. Code Quality and Testing: Develop skills to write clean, maintainable code and implement unit tests and integration tests to ensure software reliability and stability.

#### Most Important Technologies Used:

- Python
- Flask
- Requests library for HTTP requests
- Spotify Web API

The end result of the project will be a Spotify clone application with my interpretation, which will demonstrate not only my ability to use the Spotify API, but also all the skills and knowledge mentioned above. This project will serve as an excellent example of my abilities in programming and software development.

This project is a personal project made for the development of personal growth. In the beginning, this kind of coding will be introduced in general, slowly advancing my little tasks until I can make a self-interpreted Spotify clone application. For each small file, a small description will be given for understanding the purpose and task. In this folder you can see the learning and development process, but the final result (or the cloned application) will be published as a separate project.


> [!IMPORTANT]
> In the published code, my created dashboard spotify app client_id and client_secret will be replaced with "##..." for safety reasons!


# File 1: top_songs_from_artists
Through this project, I learned how to access the Spotify API to develop a program. I gained knowledge on obtaining my Spotify access token and utilizing it to interact with various endpoints, enabling me to create my own code using data from Spotify. This code is the basic code that will help with the execution of future files and tasks. Various learning resources were used to develop this code, from spotify developer tutorials to developer group chats, suggestions and conversations. In general, this file shows how to access the token, find what is needed (in this case, a specific artist and its most popular songs in a specific country), and itmes are grabbed in results, then I run code and cleaned up the results. In this project .env file was used. 

### Overview
This Python script interacts with the Spotify API to perform the following tasks:

1. Authenticate with the Spotify API using client credentials.
2. Search for an artist by name.
3. Retrieve the top tracks of the artist.

### Dependencies
- dotenv: To load environment variables from a .env file.
- os: To access environment variables.
- base64: To encode the client credentials.
- requests: To make HTTP requests to the Spotify API.
- json: To handle JSON data.

### Environment Variables
The script expects the following environment variables to be set in a .env file:
- CLIENT_ID: Spotify API client ID.
- CLIENT_SECRET: Spotify API client secret.

### Functions
1. #### load_dotenv()
    - Loads environment variables from a .env file.

2. #### get_token()
    - Purpose: Retrieves an access token from the Spotify API.
    - Process:
        - Combines client_id and client_secret into a base64-encoded string.
        - Sends a POST request to the Spotify token endpoint.
        - Parses the JSON response to extract the access token.
        - Returns: The access token as a string.

3. #### get_auth_header(token)
    - Purpose: Generates the authorization header for API requests.
    - Parameters: 'token' (the access token).
    - Returns: A dictionary with the authorization header.

4. #### search_for_artist(token, artist_name)
    - Purpose: Searches for an artist by name using the Spotify API.
    - Parameters:
        - 'token' (the access token).
        - 'artist_name' (the name of the artist to search for).
    - Process:
        - Constructs the search query URL.
        - Sends a GET request to the Spotify search endpoint.
        - Parses the JSON response to find the artist.
        - If no artist is found, prints a message and returns None.
    - Returns: A dictionary with artist information if found, otherwise None.

5. #### get_songs_by_artist(token, artist_id)
    - Purpose: Retrieves the top tracks of an artist by their Spotify ID.
    - Parameters:
        - 'token' (the access token).
        - 'artist_id' (the Spotify ID of the artist).
    - Process:
        - Constructs the URL to get the artist's top tracks.
        - Sends a GET request to the Spotify API.
        - Parses the JSON response to extract the tracks.
    - Returns: A list of dictionaries, each containing information about a track.

### Main Execution Flow
1. Get the Access Token:
    - Calls get_token() to obtain the access token.
2. Search for Artist:
    - Calls search_for_artist(token, "TravisScott") to find the artist Travis Scott.
    - Retrieves the artist ID from the search result.
3. Get Artist's Top Tracks:
    - Calls get_songs_by_artist(token, artist_id) using the retrieved artist ID.
    - Prints the names of the top tracks.

### Example Output
The script will output the top tracks of the specified artist (e.g., Travis Scott) in the following format:
> 1. FE!N (feat. Playboi Carti)
> 2. Type Sh*t
> 3. goosebumps
> 4. I KNOW ?
> 5. BUTTERFLY EFFECT
> 6. Cinderella
> 7. MY EYES
> 8. Open Arms (feat. Travis Scott)
> 9. Trance (with Travis Scott & Young Thug)
> 10. HIGHEST IN THE ROOM

This script is useful for querying Spotify's database for artist information and their popular songs, providing a simple command-line interface for interacting with the Spotify API.

# File 2: save_weekly_playlist
This Flask application allows users to save their "Discover Weekly" songs from Spotify into a separate "Saved Weekly" playlist. It leverages the Spotipy library for Spotify API interactions and uses Flask to manage web routes and user sessions. The application uses waitress as a production-ready server.As part of this project, I Iearned how to integrate Spotify OAuth into my project and automate saving the Discover Weekly playlist using the Spotify API. I learned how to authenticate with Spotify, get an access token, and use it to retrieve information about the user's playlists and tracks. Also understood the code for saving the Discover Weekly playlist automatically. In this project the wsgi.py file was used. For coding this project I used online materials to understand the basis of this system.

### Overview
This Python web application uses Flask to create a web interface that allows users to log in with their Spotify account, retrieve their Discover Weekly playlist, and save its songs to a separate "Saved Weekly" playlist. The application uses the Spotipy library for Spotify API interactions and Spotify OAuth for authentication.

### Dependencies
- spotipy: For interacting with the Spotify API.
- flask: For creating the web application.
- time: For handling token expiration.

### Environment Setup
Flask session configuration:
- SESSION_COOKIE_NAME: Set to 'Spotify Cookie'.
- secret_key: A string used for securing session data.

### Constants
TOKEN_INFO: Key used to store token information in the session.

### Routes
1. #### / (login)
    - Purpose: Initiates the Spotify OAuth login process.
    - Process:
        - Calls create_spotify_oauth() to generate an OAuth object.
        - Redirects the user to the Spotify authorization URL.

2. #### /redirect (redirect_page)
    - Purpose: Handles the redirect from Spotify after user authorization.
    - Process:
        - Clears the session.
        - Retrieves the authorization code from the request.
        - Exchanges the authorization code for an access token.
        - Stores the token information in the session.
        - Redirects to the save_discover_weekly route.

3. #### /saveDiscoverWeekly (save_discover_weekly)
    - Purpose: Saves the songs from the Discover Weekly playlist to a Saved Weekly playlist.
    - Process:
        - Retrieves the token information using get_token().
        - Initializes the Spotipy client with the access token.
        - Retrieves the current user's ID.
        - Searches for "Discover Weekly" and "Saved Weekly" playlists.
        - If "Saved Weekly" does not exist, creates it.
        - Retrieves songs from "Discover Weekly" and adds them to "Saved Weekly".
        - Returns a success message if songs are added.

### Helper Functions

1. ### get_token()
    - Purpose: Retrieves and refreshes the access token if needed.
    - Process:
        - Checks if the token information is stored in the session.
        - Checks if the token is expired.
        - If expired, refreshes the token using the refresh token.
    - Returns: The token information.

2. #### create_spotify_oauth()
    - Purpose: Creates a SpotifyOAuth object configured with client credentials and required scopes.
    - Returns: A configured SpotifyOAuth object.

### Configuration
Spotify API Credentials:
- client_id: Spotify API client ID.
- client_secret: Spotify API client secret.
- redirect_uri: URL to redirect to after authentication.
- scope: Required scopes for accessing user library and modifying playlists.

### Execution
The application is run in debug mode by calling app.run(debug=True).

### Example Usage
1. User navigates to the root URL (/).
2. User is redirected to Spotify for authentication.
3. After authentication, user is redirected back to the application (/redirect).
4. The application saves the user's Discover Weekly songs to the Saved Weekly playlist.
5. A success message is displayed.

This application allows users to easily back up their Discover Weekly playlist into a custom playlist on their Spotify account, ensuring they do not lose track of songs they liked from the curated Discover Weekly playlist.

# File 3: get_user_playlists
This Flask application enables users to log in with their Spotify accounts, retrieve their playlists, and manage access tokens. The app uses OAuth 2.0 for authentication and authorization.

### Configuration:
- CLIENT_ID: The client ID provided by Spotify for the application.
- CLIENT_SECRET: The client secret provided by Spotify for the application.
- REDIRECT_URI: The URI to redirect to after Spotify authentication. This should be configured in the Spotify Developer Dashboard.

### Routes:
1. #### Home Route (/)
- Method: GET
- Description: Displays a welcome message with a link to log in with Spotify.
- Response: HTML content with a login link.

2. #### Login Route (/login)
- Method: GET
- Description: Redirects the user to the Spotify authorization page.
- Spotify Scopes:
user-read-private
user-read-email
- Response: Redirects to the Spotify authorization URL.

3. #### Callback Route (/callback)
- Method: GET
- Description: Handles the callback from Spotify after user authentication.
- Parameters:
  -  code: Authorization code returned by Spotify.
  -  error (optional): Error code returned by Spotify if the authorization failed.
- Response: 
  - On success -> Exchanges the authorization code for an access token and refresh token, then redirects to the /playlists route. 
  - On error -> Returns a JSON response with the error message.

4. #### Playlists Route (/playlists)
- Method: GET
- Description: Retrieves and displays the user's playlists from Spotify.
- Authorization: Requires a valid access token. If the token is expired, it redirects to the /refresh-token route.
- Response: JSON response containing the user's playlists.

5. #### Refresh Token Route (/refresh-token)
- Method: GET
- Description: Refreshes the access token using the refresh token.
- Response:
  - On success -> Updates the session with a new access token and redirects to the /playlists route.
  - On failure -> Redirects to the /login route.

### Session Management:
- Access Token (session['access_token']): The token used to authenticate API requests to Spotify.
- Refresh Token (session['refresh_token']): The token used to obtain a new access token when the current one expires.
- Expiration Time (session['expires_at']): The timestamp when the access token will expire.

### OAuth 2.0 Flow:
- Authorization Request: User is redirected to Spotify to authorize the app.
- Authorization Callback: Spotify redirects back to the app with an authorization code.
- Token Exchange: The app exchanges the authorization code for an access token and refresh token.
- Access Token Usage: The access token is used to make authorized API requests to Spotify.
- Token Refresh: When the access token expires, the app uses the refresh token to obtain a new access token.

### Error Handling:
- If there is an error during the OAuth flow (e.g., user denies authorization), the error is captured and returned as a JSON response.
- If the access token is missing or expired, the user is redirected to the login or token refresh routes as appropriate.

### Security Considerations for Future:
- The client_secret should be kept confidential and not exposed in the client-side code.
- HTTPS should be used for the REDIRECT_URI in production to ensure secure transmission of tokens.
- Session management should ensure tokens are securely stored and accessed.

### Example Usage:
- User navigates to the home page and clicks the "Login with Spotify" link.
- User is redirected to Spotify to authorize the app.
- After authorization, Spotify redirects the user back to the callback URL.
- The app exchanges the authorization code for an access token and retrieves the user's playlists.
- If the access token expires, the app automatically refreshes it using the refresh token.

The Flask application provides a seamless integration with the Spotify API, ensuring a secure and user-friendly experience for accessing and managing Spotify data.

# File 4: most_played_songs
This Flask application allows users to log in with their Spotify account, retrieve their most played songs, and update a playlist with these songs. The app utilizes the Spotipy library to interact with the Spotify Web API.

### Dependencies:
 - Flask: A micro web framework for Python.
 - Spotipy: A lightweight Python library for the Spotify Web API.

### Environment Configuration:
 - SESSION_COOKIE_NAME: Name for the session cookie.
 - secret_key: Secret key for session management.
 - Spotify API credentials:
    - CLIENT_ID: The client ID provided by Spotify for the application.
    - CLIENT_SECRET: The client secret provided by Spotify for the application.
    - REDIRECT_URI: The URI to redirect to after Spotify authentication. This should be configured in the Spotify Developer Dashboard.

### Component create_spotify_oauth():
- Configures and returns a SpotifyOAuth object with the necessary client credentials, redirect URI, and scopes (user-top-read, playlist-modify-public, playlist-modify-private).
- Uses .spotify_caches to cache the tokens.
- show_dialog=True ensures the user is always prompted to authorize.

### Components routes:
1. #### login ("/"):
    - Initiates the Spotify OAuth flow by redirecting the user to the Spotify authorization URL.

2. #### callback ("/callback"):
    - Handles the callback from Spotify after user authorization.
    - Retrieves the authorization code from the URL, exchanges it for an access token, and stores the token in the session.
    - Redirects to the most_played_songs route.

3. #### most_played_songs ("/most-played-songs")
    - Retrieves and refreshes the access token if necessary.
    - Fetches the user's top tracks from the last 4 weeks.
    - Checks if a playlist named "most played songs" exists; if not, creates it.
    - Adds new top tracks to the playlist if they are not already present.
    - Returns a message confirming the playlist update.

### Component get_token(session):
- Validates and refreshes the access token if it is expired.
- Retrieves the token from the session or cache.
- Refreshes the token if it is expired and returns the token along with its validity status.

### Execution: 
The application runs on the local server (localhost:5000) in debug mode.

### Error Handling:
1. #### Token Expiration:
    - Refreshes the token if it has expired.
    - Redirects the user to the login route if token retrieval fails.

2. #### Playlist and Track Operations:
    - Checks if the playlist exists before attempting to create it.
    - Ensures that new tracks are only added if they are not already in the playlist.

### Setup and Installation:
    pip install Flask spotipy

### Future Enhancements:
- User Feedback: Provide more detailed feedback to the user on the web pages.
- Error Pages: Create custom error pages for different HTTP status codes (e.g., 404, 500).
- Logging: Implement logging to track application activity and errors.
- Testing: Write unit and integration tests for the application.

This setup ensures that users can log in with their Spotify account, fetch their most played tracks, and maintain a playlist with their most played songs, updating it with any new top tracks.