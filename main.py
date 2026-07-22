import os
import random
import subprocess
from datetime import datetime, timedelta

def get_date_input(prompt, default_date_str):
    while True:
        user_input = input(f"{prompt} (YYYY-MM-DD) [Default: {default_date_str}]: ")
        if not user_input.strip():
            return datetime.strptime(default_date_str, "%Y-%m-%d")
        try:
            return datetime.strptime(user_input.strip(), "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_positive_int(prompt, default):
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_repo_path(prompt, default="."):
    while True:
        user_input = input(f"{prompt} (default current directory): ")
        if not user_input.strip():
            return default
        if os.path.isdir(user_input):
            return user_input
        else:
            print("Directory does not exist. Please enter a valid path.")

def get_filename(prompt, default="data.txt"):
    user_input = input(f"{prompt} (default {default}): ")
    if not user_input.strip():
        return default
    return user_input

def make_commit(date, repo_path, filename, message="graph-greener!"):
    filepath = os.path.join(repo_path, filename)
    with open(filepath, "a") as f:
        f.write(f"Commit at {date.isoformat()}\n")
    subprocess.run(["git", "add", filename], cwd=repo_path, stdout=subprocess.DEVNULL)
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env, stdout=subprocess.DEVNULL)

def main():
    print("="*60)
    print("🌱 Welcome to graph-greener - Custom Range Commit Generator 🌱")
    print("="*60)

    # 1. Repo Path aur Filename input lena
    repo_path = get_repo_path("Enter the path to your local git repository", ".")
    filename = get_filename("Enter the filename to modify for commits", "data.txt")

    # 2. Custom Date Range input lena
    today_str = datetime.now().strftime("%Y-%m-%d")
    start_date = get_date_input("Enter START date", today_str)
    end_date = get_date_input("Enter END date", today_str)

    if start_date > end_date:
        print("❌ Error: Start date cannot be after End date!")
        return

    # 3. Min aur Max commits per day input lena
    print("\n--- Commit Range Per Day ---")
    min_commits = get_positive_int("Enter MINIMUM commits per day", 2)
    max_commits = get_positive_int("Enter MAXIMUM commits per day", 5)

    if min_commits > max_commits:
        print("❌ Error: Minimum commits cannot be greater than Maximum commits!")
        return

    print(f"\n🚀 Processing commits from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}...")
    
    current_date = start_date
    total_commits_made = 0

    # Date loop
    while current_date <= end_date:
        commits_today = random.randint(min_commits, max_commits)
        
        if commits_today > 0:
            print(f"📅 {current_date.strftime('%Y-%m-%d')}: Making {commits_today} random commits...")
            
            for i in range(commits_today):
                random_hours = random.randint(9, 21) # Subah 9 se Raat 9 ke beech
                random_minutes = random.randint(0, 59)
                random_seconds = random.randint(0, 59)
                
                commit_date = current_date.replace(hour=random_hours, minute=random_minutes, second=random_seconds)
                make_commit(commit_date, repo_path, filename)
                total_commits_made += 1
        else:
            print(f"📅 {current_date.strftime('%Y-%m-%d')}: Skipping (0 commits)")

        current_date += timedelta(days=1)

    print(f"\n✅ All done! Locally total {total_commits_made} commits ban gaye hain.")
    print("🔄 Pushing commits to your remote repository...")
    
    # 🎯 Yeh line direct remote repository ki main branch par push karegi
    subprocess.run(["git", "push", "origin", "main"], cwd=repo_path)
    
    print("🎉 Graph update check karein thodi der mein!")

if __name__ == "__main__":
    main()