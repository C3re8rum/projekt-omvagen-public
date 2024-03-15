import subprocess
import os

from dotenv import load_dotenv

def get_git_token() -> str:
    load_dotenv()
    return os.getenv('GITHUBTOKEN')


def curl_request(url):
    # Define the command to execute using curl
    command = ['curl', '-H', f'Authorization: token {get_git_token()}','-H', '-O', '-L', url]

    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Return the stdout of the curl command
    return result.stdout