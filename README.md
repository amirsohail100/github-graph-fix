## ✨ Key Features

- **Custom Date Ranges:** Specify exact start and end dates (`YYYY-MM-DD`) to target specific gaps in your timeline.
- **Randomized Commit Density:** Define minimum and maximum commits per day to make the generated graph look organic rather than robotic.
- **Smart Time Distribution:** Automatically randomizes commit hours between 9:00 AM and 9:59 PM to simulate natural working patterns.
- **Git Environment Override:** Safely alters `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` without messing up your system's actual clock.
- **Automated Remote Sync:** Automatically pushes the generated commits to your `origin main` branch upon completion.
- **Interactive CLI Prompts:** Safe fallback defaults for every single input prompt so you can hit Enter to proceed quickly.

---

## 🛠️ How It Works Under the Hood

The script relies on Python's built-in `subprocess` module to interact directly with your local Git repository.

1. It targets a designated text file (`data.txt` by default) inside your repository.
2. For every day within your chosen date range, it generates a random number of commits between your specified bounds.
3. It appends a timestamp string to the file, stages it using `git add`, and executes `git commit` while injecting custom environment variables for the commit date.
4. Finally, it triggers a background push to your remote repository.
