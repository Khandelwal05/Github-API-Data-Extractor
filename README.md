# Github-API-Data-Extractor
## Overview
GitHub API Data Extractor is a Python application designed to fetch and display detailed information about a GitHub user, their repositories, and provide visual statistics. The tool also allows users to save feedback on repositories and stores user data in a SQLite database.

## Features
+ Fetch and display user details including name, ID, email, public repositories, followers, following, and account creation and update dates.
+ Save the user's profile picture, trophy, stats, top languages, and streak statistics as images.
+ List all repositories of a user and provide detailed information on each repository.
+ Gather and save user feedback for specific repositories.
+ Store fetched user data in a SQLite database.

## Requirements
+ Python 3.x
+ `requests` library
+ `sqlite3` library
+ `webbrowser` library
+ GitHub Personal Access Token (for authenticated API requests)

## Installation
Clone the repository:
```
git clone https://github.com/yourusername/Github-API-Data-Extractor.git
```
```
cd Github-API-Data-Extractor
```
Install the required Python libraries:
```
pip install requests
```

### Set up your GitHub Personal Access Token:
  Generate a token from GitHub Settings.
  Replace the placeholder in the script with your token:
python
```
headers={
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer YOUR_GITHUB_TOKEN',
    'X-GitHub-Api-Version': '2022-11-28'
}
```

## Usage
-> Run the script <br/>
-> Enter the GitHub username when prompted.<br/>
-> The script will fetch and display the user's details, save profile images, list repositories, and provide options to view detailed repository information and save feedback.

## Functions
+ fetch_user_details(url, headers, query_params): Fetches and displays user details.
+ image(username): Fetches and saves profile images and statistics.
+ print_repo_list(username): Lists all repositories of the user.
+ repo_details(username): Provides detailed information about a specific repository.
+ get_feedback(username, repo_name): Collects and saves user feedback for a repository.
+ database(data): Stores fetched user data in a SQLite database.

## Sample Images that will be generated 
Github Trophies of user

![Screenshot 2024-06-06 091554](https://github.com/Khandelwal05/Github-API-Data-Extractor/assets/114740796/8b1e46fb-c158-4055-b6f8-3c9ae1bdd495)

Most Languages Used<br/>

![Screenshot 2024-06-06 091632](https://github.com/Khandelwal05/Github-API-Data-Extractor/assets/114740796/40c6087c-33a3-47de-a99a-a1d141b8403e)

Streak <br/>
![image](https://github.com/Khandelwal05/Github-API-Data-Extractor/assets/114740796/053e18b8-7bb9-4694-b095-977541a60080)

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
