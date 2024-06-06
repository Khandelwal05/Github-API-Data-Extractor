import requests
import json
import sqlite3
import webbrowser
import os


def fetch_user_details(url,headers,queruy_params):
    res=requests.get(url,headers=headers,params=query_params)
    if (res.status_code==200):
        # print(res.status_code)
        # print(res.json())
        data=res.json()
        # with open('data.json', 'w') as data_file:
        #     json.dump(data,data_file, indent=4)
        print("Name of the user is: ",data['name'])
        print("Id: ",data['id'])
        print("Email: ",data['email'])
        print("No. of Public Repositories are: ",data['public_repos'])
        print("No. of followers are: ",data['followers'])
        print("No of following are: ",data['following'])
        print("Id created on: ",data['created_at'])
        print("Id updates on: ",data['updated_at'])
    else :    
        print(("Error Occured, may be u inputed wrong user name"))
        username=input("Enter the username here")
        url=f'https://api.github.com/users/{username}'
        fetch_user_details(url,headers,queruy_params)
    return data


def image(username):
    avatar_url = data.get('avatar_url')
    if avatar_url:
        avatar_res = requests.get(avatar_url)
        if avatar_res.status_code == 200:
            with open("profile.png", 'wb') as f:
                f.write(avatar_res.content)
            print("Profile picture saved as profile.png")
        else:
            print("Error fetching profile picture")
    else:
        print("No avatar URL found")


        # Fetch and save the trophy image
    trophy_url = f'https://github-profile-trophy.vercel.app/?username={username}&theme=onedark'
    trophy_res = requests.get(trophy_url)
    if trophy_res.status_code == 200:
        with open("trophy.svg", 'wb') as f:
            f.write(trophy_res.content)
        print("Trophy image saved as trophy.svg")
        # file_path = os.path.abspath("trophy.svg")
        # webbrowser.open(f'file://{file_path}')
    else:
        print("Error fetching trophy image")


    stats_url = f'https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=onedark'
    stats_res = requests.get(stats_url)
    if stats_res.status_code == 200:
        with open("stats.svg", 'wb') as f:
            f.write(stats_res.content)
        print("GitHub stats image saved as stats.svg")
        # file_path = os.path.abspath("stats.svg")
        # webbrowser.open(f'file://{file_path}')
    else:
        print("Error fetching GitHub stats image")

    
    languages_url = f'https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=onedark'
    languages_res = requests.get(languages_url)
    if languages_res.status_code == 200:
        with open("top-languages.svg", 'wb') as f:
            f.write(languages_res.content)
        print("Top languages image saved as top-languages.svg")
        file_path = os.path.abspath("top-languages.svg")
        webbrowser.open(f'file://{file_path}')
    else:
        print("Error fetching top languages image")


    streak_url = f'https://github-readme-streak-stats.herokuapp.com/?user={username}'
    streak_res = requests.get(streak_url)
    if streak_res.status_code == 200:
        with open("streak.svg", 'wb') as f:
            f.write(streak_res.content)
        print("GitHub streak stats image saved as streak.svg")
        file_path = os.path.abspath("streak.svg")
        webbrowser.open(f'file://{file_path}')
    else:
        print("Error fetching GitHub streak stats image")
    

def print_repo_list(username):
    print("\n\n\n\nAbout Repositories")

    repos_url= f'https://api.github.com/users/{username}/repos'
    repo_res=requests.get(repos_url,headers=headers)
    if (repo_res.status_code==200):
        repos=repo_res.json()
        # with open('user.json', 'w') as user_file:
        #     json.dump(repos,user_file, indent=4)
    else :
        print("Error in repository")

    repos_lst=[]
    for repo in repos:
        repos_lst.append(repo['name'])
    print("Repositories are:", repos_lst)


def repo_details(username):
    repo_name=input("Enter Repo name here correctly")

    print("\n\n\nAbout Repository ",repo_name)
    reponame_url=f'https://api.github.com/repos/{username}/{repo_name}'
    reponame_res=requests.get(reponame_url, headers=headers)
    if reponame_res.status_code==200:
        repo_data=reponame_res.json()
        print(f"Description: {repo_data.get('description', 'No description')}")
        print(f"Stars: {repo_data.get('stargazers_count', 0)}")
        print(f"Forks: {repo_data.get('forks_count', 0)}")
        print(f"Open Issues: {repo_data.get('open_issues_count', 0)}")
        print(f"Last Push Date: {repo_data.get('pushed_at', 'N/A')}")
        print(f"Created At: {repo_data.get('created_at', 'N/A')}")
        print(f"Updated At: {repo_data.get('updated_at', 'N/A')}")
        # print(f"License: {repo_data.get('license', {}).get('name', 'No license')}")
        # for repo_input in repo:
        commits_url=f'https://api.github.com/repos/{username}/{repo_name}/commits'
        commits_res=requests.get(commits_url, headers=headers)
        commit=commits_res.json()
        print("No of commits are ",len(commit))


        languages_url = repo_data['languages_url']
        languages_res = requests.get(languages_url, headers=headers)
        if languages_res.status_code == 200:
            languages = languages_res.json()
            print("Languages Used:", ', '.join(languages.keys()))
        else:
            print("Error fetching languages")
        
        merges_url= f'https://api.github.com/repos/{username}/{repo_name}/merges'
        merges_res=requests.get(merges_url, headers=headers)
        merges=merges_res.json()
        print("No of merges are: ",len(merges))

        pulls_url= f'https://api.github.com/repos/{username}/{repo_name}/pulls'
        pulls_res=requests.get(pulls_url, headers=headers)
        pulls=pulls_res.json()
        print("No of pulls are: ",len(pulls))

        issues_url= f'https://api.github.com/repos/{username}/{repo_name}/issues'
        issues_res=requests.get(issues_url, headers=headers)
        issues=issues_res.json()
        print("No of issues are: ",len(issues))

        contributors_url = repo_data['contributors_url']
        contributors_res = requests.get(contributors_url, headers=headers)
        if contributors_res.status_code == 200:
            contributors = contributors_res.json()
            print(f"No. of Contributors: {len(contributors)}")
            see_contributors = input("Do you want to see the contributors' details? (yes/no): ")
            if see_contributors.lower() == 'yes':
                for contributor in contributors:
                    print(f"Contributor: {contributor.get('login', 'N/A')}")
                    print(f"Contributions: {contributor.get('contributions', 'N/A')}")
                    print(f"Profile URL: {contributor.get('html_url', 'N/A')}")
                    print("-" * 20)
        else:
            print("Error fetching contributors")


        # feedback = input("Please provide your feedback for this repository: ")
        # with open(f"{repo_name}_feedback.txt", "a") as f:
        #     f.write(f"Feedback for {repo_name}: {feedback}\n")
        # print("Thank you for your feedback!")
        get_feedback(username, repo_name)

    
    else:
        print("Error fetching repository details")

def get_feedback(username, repo_name):
    # Ask the user if they want to provide feedback
    provide_feedback = input(f"do you want to provide feedback for the repository '{repo_name}'? (yes/no): ").strip().lower()
    
    if provide_feedback == 'yes':
        # Get feedback and rating from the user
        feedback = input(f"Please provide your feedback for the repository '{repo_name}': ")
        rating = input("How much would you rate this repository out of 5? ")
        
        # Create a directory for the user if it doesn't exist
        user_dir = f"feedback_{username}"
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        
        # Save the feedback in a text file specific to the user and repository
        feedback_file = os.path.join(user_dir, f"{repo_name}_feedback.txt")
        with open(feedback_file, "a") as f:
            f.write(f"Feedback for {repo_name}:\n")
            f.write(f"Rating: {rating}/5\n")
            f.write(f"Feedback: {feedback}\n\n")
        
        print("Thank you for your feedback!")
    else:
        print("Feedback not provided.")

def database(data):

    conn = sqlite3.connect('github_users.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            
            id INTEGER PRIMARY KEY,
            name TEXT,
            company TEXT,
            email TEXT,
            public_repos INTEGER,
            followers INTEGER,
            following INTEGER,
            created_at TEXT,
            updated_at TEXT
        )
    ''')

    # Insert data into the table
    user_data = (
        data.get('id'),
        data.get('name'),
        data.get('company'),
        data.get('email'),
        data.get('public_repos'),
        data.get('followers'),
        data.get('following'),
        data.get('created_at'),
        data.get('updated_at')
    )

    c.execute('''
        INSERT OR REPLACE INTO users (id, name, company, email, public_repos, followers, following, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', user_data)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()

    print("Data stored in database")

# main
    
username=input("Enter the username here")
url=f'https://api.github.com/users/{username}'

per_page = 20
page=1
headers={
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer YOUR_GITHUB_TOKEN',
    'X-GitHub-Api-Version': '2022-11-28'
}

query_params={'perpage':per_page,
               'page':page}

data=fetch_user_details( url,headers, query_params)
image(username)
print_repo_list(username)
repo_details(username)
while True:
    ask=input("Enter here Do you want to search for any other repository?(yes/no)")
    if (ask.lower()=='yes'):
        repo_details(username)
    else :
        print("Thank You")
        break

database(data)

