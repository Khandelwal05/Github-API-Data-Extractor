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

![image](https://github.com/Khandelwal05/Github-API-Data-Extractor/assets/114740796/a0903b8f-e66b-44bc-b475-3497cc87b706)

Most Languages Used<br/>

![image](https://github.com/Khandelwal05/Github-API-Data-Extractor/assets/114740796/43c4f2f1-a89c-4ca0-8834-b4073a28f656)

Streak <br/>
![image](https://github.com/Khandelwal05/Github-API-Data-Extractor/assets/114740796/220aa399-69e1-4734-8c3d-8887a914c214)

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.
