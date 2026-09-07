# 🌱 graph-greener (GitHub Graph Fix)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Status](https://img.shields.io/badge/status-active-success.svg)]()

> **"Transform your contribution graph with precision, automation, and full transparency."**

---

## 🔍 Transparency Message & Disclaimer

Before using this repository, I want to maintain complete **transparency** regarding what this script does and why it was created:

- **What it is:** `graph-greener` is a utility tool written in Python that automates the process of making historical or custom-range commits locally within a Git repository and pushes them to your remote branch (`main`).
- **Why it was created:** As developers, we sometimes miss tracking consistency due to personal projects, offline coding sessions, or experimentation across systems where commits didn't sync properly to our main profile. This tool serves as a personal management script to organize, backfill, or simulate consistent activity ranges for local testing and portfolio visualization.
- **Responsible Use:** Contribution graphs are meant to reflect coding activity. While this tool gives you technical control over Git environment variables (`GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`), please use it ethically and responsibly. Overusing automated commit generators to artificially bloat activity can misrepresent actual project work. Transparency matters in the developer community—use this tool mindfully!

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

## 📋 Prerequisites

Make sure you have the following installed on your machine before running the script:

- **Python 3.x** (Download from [python.org](https://www.python.org/))
- **Git** installed and configured with your GitHub account credentials (SSH keys or Personal Access Token set up for pushing).

---

## 🚀 Installation & Setup Guide

If you want to use this tool on your own PC, follow these simple terminal/command line steps:

### Step 1: Clone the Repository

Open your terminal (Git Bash, Command Prompt, or VS Code terminal) and run the following command to clone this repository to your local machine:

```bash
git clone [https://github.com/amirsohail100/github-graph-fix.git](https://github.com/amirsohail100/github-graph-fix.git)
```
