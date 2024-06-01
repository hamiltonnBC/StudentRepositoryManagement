# StudentRepositoryManagement

This Python script helps you update multiple student repositories to their latest branches. It is particularly useful for grading purposes, allowing you to easily fetch the latest version of each student's repository.

Author: Nicholas Hamilton

Formatting and error handling were adjusted with the help of various Stack overflow posts, and formatting was adjusted with AI.

This script was designed to speed up the grading process for CSC 226 at Berea College.

## Prerequisites

- Python 3.x installed on your system
- Git installed on your system

## Installation

1. Clone this repository or download the `update_student_repos.py` script.

2. Ensure that you have the necessary dependencies installed. This script does not require any additional dependencies beyond the Python standard library.

## Usage

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to store the student repositories (or stay at home).

3. Clone all the student repositories using the following command:

gh classroom clone student-repos -a 555555

Replace `555555` with the appropriate assignment identifier (this can be found in GitHub Classroom).

This command will clone all the student repositories into a folder in your current directory.

4. Run the `update_student_repos.py` script by either using the Run feature in your IDE or using the following command:

python update_student_repos.py

5. When prompted, enter the directory path containing the student repositories. For example:

Enter the directory containing student repositories (e.g., /Users/hamiltonn/hw01-assignment-name-submissions):

6. The script will iterate over each repository in the specified directory, fetch all branches, determine the branch with the latest commit, check out that branch, and update it to the latest version from the remote.

7. Once the script finishes executing, it will display a summary of the update process:
   - If all repositories were updated successfully, it will display a message indicating so.
   - If there were any issues with specific repositories, it will display a list of those repositories along with a description of the issue encountered.

## Error Handling

The script now includes error handling to address different scenarios that may occur during the update process:

- If a directory is not a valid git repository, it will be skipped, and an appropriate message will be logged.
- If the script fails to determine the latest branch for a repository, it will skip that repository and log an error message.
- If the specified branch does not exist in a repository, it will skip that repository and log an error message.
- If any other error occurs during the execution of git commands, it will be caught, and an error message will be logged.

At the end of the script, a summary of repositories with issues will be displayed, including the repository name and the corresponding issue.

## Notes

- Make sure you have the necessary permissions to access and modify the student repositories in the specified directory.
- The script assumes that the student repositories are organized in separate directories within the specified directory.
- If you encounter any issues or have questions, please contact me through email - hamiltonn428@gmail.com

Happy grading!