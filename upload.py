from huggingface_hub import login
from huggingface_hub import HfApi
from huggingface_hub import Repository

#not that when passing a file path with "-" in the name add double slashes so it's accpeted by Python

def push_code(dir_path, commit_message):
    repo = Repository(local_dir=dir_path)
    repo.git_pull()
    repo.push_to_hub(commit_message=commit_message)


def upload_file(token, local_path, repo_path, repo_id, repo_type):
    
    #Whenever you want to upload files to the Hub, you need to log in to your Hugging Face account
    login(token=token)

    api = HfApi()

    api.upload_file(
    path_or_fileobj=local_path,
    path_in_repo=repo_path,
    repo_id=repo_id,
    repo_type=repo_type,
    )

def upload_folder(token, local_path, repo_path, repo_id, repo_type,ignore_patterns):
    
    #Whenever you want to upload files to the Hub, you need to log in to your Hugging Face account
    login(token=token)

    api = HfApi()

    api.upload_folder(
    folder_path=local_path,
    path_in_repo=repo_path,
    repo_id=repo_id,
    repo_type=repo_type,
    ignore_patterns=ignore_patterns,
    )

