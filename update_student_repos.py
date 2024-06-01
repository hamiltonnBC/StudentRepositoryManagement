import os
import subprocess

# Prompt the user for the directory containing student repositories
hw_submissions_dir = input(
    "Enter the directory containing student repositories (e.g., /Users/hamiltonn/hw08-assignment-name-submissions): ")

# Iterate over each directory in the hw_submissions_dir
for repo_dir in os.listdir(hw_submissions_dir):
    repo_path = os.path.join(hw_submissions_dir, repo_dir)
    if os.path.isdir(repo_path):
        print(f"Checking repository in {repo_path}")

        # Change to the repository directory
        os.chdir(repo_path)

        # Fetch all branches
        subprocess.run(["git", "fetch", "--all"])

        # Determine the branch with the latest commit and trim whitespace
        latest_branch = subprocess.check_output(["git", "branch", "-r", "--sort=-committerdate"]).decode().split("\n")[
            0].replace("origin/", "").strip()

        # Checkout the branch with the latest commit
        subprocess.run(["git", "checkout", latest_branch])

        # Update the branch to the latest version from the remote
        subprocess.run(["git", "pull", "origin", latest_branch])

        # Change back to the hw_submissions_dir before processing the next repository
        os.chdir(hw_submissions_dir)

print("All repositories have been updated to the latest branch.")