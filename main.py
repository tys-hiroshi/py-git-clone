import git
from app.utils.config_util import ConfigUtil
from pprint import pprint
import os

def get_repository_name(url: str):
    splitted_array = url.split("/")
    git_name = splitted_array[len(splitted_array) - 1]
    return git_name.replace(".git", "")

def clone_repository(clone_url: str, cloneDestinationDirPath: str, branch:str="master"):
    try:
        git.Repo.clone_from(url,
                        cloneDestinationDirPath,
                        branch=branch)
    except Exception as e:
        pprint(e)


ymlFilePath = "app_base.yml"
configUtil = ConfigUtil()
config = configUtil.read_yaml_file(ymlFilePath)

pprint(config)

cloneDistinationBaseDirPath = config["CloneDestinationBaseDirPath"]

for url in config["CloneRepositoryList"]:
    pprint(f"clone url; {url}")
    repo_name = get_repository_name(url)
    cloneDistinationDirPath = os.path.join(cloneDistinationBaseDirPath, repo_name)
    clone_repository(url, cloneDistinationDirPath, "master")
