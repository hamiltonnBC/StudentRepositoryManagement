import os
import subprocess

# Prompt the user for the directory containing student repositories
hw_submissions_dir = input(
    "Enter the directory containing student repositories (e.g., /Users/hamiltonn/assignment-name-submissions): ")

# Initialize a dictionary to store repositories with issues
repo_issues = {}

# Iterate over each directory in the hw_submissions_dir
for repo_dir in os.listdir(hw_submissions_dir):
    repo_path = os.path.join(hw_submissions_dir, repo_dir)
    if os.path.isdir(repo_path):
        print(f"Checking repository in {repo_path}")

        try:
            # Change to the repository directory
            os.chdir(repo_path)

            # Check if the directory is a valid git repository
            if not os.path.exists(".git"):
                repo_issues[repo_dir] = "Not a valid git repository"
                continue

            # Fetch all branches
            subprocess.run(["git", "fetch", "--all"], check=True)

            # Determine the branch with the latest commit and trim whitespace
            try:
                latest_branch = \
                    subprocess.check_output(["git", "branch", "-r", "--sort=-committerdate"]).decode().split("\n")[
                        0].replace("HEAD -> ", "").replace("origin/", "").strip()
            except subprocess.CalledProcessError:
                repo_issues[repo_dir] = "Failed to determine the latest branch"
                continue

            # Checkout the branch with the latest commit
            try:
                subprocess.run(["git", "checkout", latest_branch], check=True)
            except subprocess.CalledProcessError:
                repo_issues[repo_dir] = f"Branch '{latest_branch}' does not exist"
                continue

            # Update the branch to the latest version from the remote
            subprocess.run(
                ["git", "pull", "origin", latest_branch], check=True)

        except subprocess.CalledProcessError as e:
            repo_issues[repo_dir] = f"Error: {str(e)}"

        finally:
            # Change back to the hw_submissions_dir before processing the next repository
            os.chdir(hw_submissions_dir)

# Print the summary of repositories with issues
if repo_issues:
    print("\nRepositories with issues:")
    for repo, issue in repo_issues.items():
        print(f"{repo}: {issue}")
else:
    print("\nAll repositories have been updated successfully.")
