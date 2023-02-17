from huggingface_hub import hf_hub_download
from huggingface_hub import snapshot_download

#download files 
def download_file(repo_name, filename, revision='main',repo_type='model'):
    
    file_location = hf_hub_download(repo_id=repo_name, filename=filename,revision=revision, repo_type=repo_type)
    return file_location

#download a folder
def download_folder(repo_name, revision='main'):
    
    folder_location = snapshot_download(repo_id=repo_name, revision=revision)

    return folder_location


 