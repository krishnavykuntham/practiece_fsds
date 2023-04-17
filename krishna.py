import os
from git import Repo

# Clone the GitHub repository to a local folder
repo_url = "https://github.com/krishnavykuntham/practiece_fsds.git"
local_folder = "C:\Users\Administrator\Desktop\GIT"
branch = "main"
if not os.path.isdir(local_folder):
    repo = Repo.clone_from(repo_url, local_folder, branch=branch)
else:
    repo = Repo(local_folder)
    repo.remotes.origin.pull()

# Run the Python script from the cloned repository
script_name = "test_krishna.py"
script_path = os.path.join(local_folder, script_name)
os.system(f"python {script_path}")
