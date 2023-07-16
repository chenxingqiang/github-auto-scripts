# GitHub Auto-Scripts Repository

Welcome to the GitHub Auto-Scripts repository. This repository contains a collection of Python scripts for automating common tasks on GitHub using the GitHub REST API. 

The script included in this repository is a perfect starting point for automating bulk actions on GitHub, such as forking repositories from one organization to another. 

## Description

The script in this repository performs the following tasks:

1. Fetches all repositories from a specified GitHub organization.
2. Checks whether each repository has already been forked to a target organization.
3. If not already forked, forks the repository to the target organization.
4. After forking, the script renames the forked repository by adding a prefix.

These scripts are useful in scenarios where you want to create a backup of an organization's repositories or create a subset of an organization's repositories in another organization.

## Usage

To use the scripts in this repository, you will need a GitHub Personal Access Token (PAT) with appropriate permissions (e.g., `repo` and `delete_repo` scopes for the forking and renaming script).

You will also need to install the `requests` Python library, which you can do with the command `pip install requests`.

The scripts are designed to be modified for your specific use-case. For example, you can adjust the source and target organizations, the prefix for the forked repositories, or the Personal Access Token.

Remember to handle your GitHub PAT with care, as it provides access to your GitHub account. Do not share it or publish it publicly.

## Contributions

Contributions to the GitHub Auto-Scripts repository are welcome. If you have a script you'd like to share or a suggestion for improving the existing scripts, please feel free to open a pull request or an issue.



Creating scripts for all possible batch operations in GitHub would be a vast undertaking, as there are many different actions you could perform. Instead, I can certainly provide you with some examples of scripts for common batch operations. Please adjust these scripts to suit your own needs.

1. **Forking repositories to an organization:** The script provided in the previous responses already covers this operation. It fetches all repositories from a specified GitHub organization, checks whether each repository has already been forked to the target organization, and if not, forks the repository to the target organization.

2. **Deleting all repositories in an organization:** This script fetches all repositories from a specified organization and deletes them. Please use it with caution.
   ```python
   import requests

   # GitHub API 请求头部信息，需要替换为您自己的访问令牌（Token）
   headers = {
       'Authorization': 'Bearer your_github_pat'
   }

   # 要删除的企业组织名称
   org_name = 'org_to_delete_repos'

   # 获取企业组织的仓库列表
   repo_url = f'https://api.github.com/orgs/{org_name}/repos'
   response = requests.get(repo_url, headers=headers)
   repos = response.json()

   # 批量删除仓库
   for repo in repos:
       delete_url = f'https://api.github.com/repos/{org_name}/{repo["name"]}'
       response = requests.delete(delete_url, headers=headers)
       if response.status_code == 204:
           print(f'Successfully deleted: {repo["name"]}')
       else:
           print(f'Failed to delete: {repo["name"]}')
   ```

3. **Adding a collaborator to all repositories in an organization:** This script adds a specified user as a collaborator to all repositories in a specified organization.
   ```python
   import requests

   # GitHub API 请求头部信息，需要替换为您自己的访问令牌（Token）
   headers = {
       'Authorization': 'Bearer your_github_pat'
   }

   # 要添加协作者的企业组织名称
   org_name = 'org_to_add_collaborator'
   # 要添加的协作者用户名
   collaborator = 'username_to_add'

   # 获取企业组织的仓库列表
   repo_url = f'https://api.github.com/orgs/{org_name}/repos'
   response = requests.get(repo_url, headers=headers)
   repos = response.json()

   # 批量添加协作者
   for repo in repos:
       collab_url = f'https://api.github.com/repos/{org_name}/{repo["name"]}/collaborators/{collaborator}'
       response = requests.put(collab_url, headers=headers)
       if response.status_code == 201:
           print(f'Successfully added collaborator to: {repo["name"]}')
       else:
           print(f'Failed to add collaborator to: {repo["name"]}')
   ```

Each of these scripts can be adapted for other purposes as well. For example, the script for adding a collaborator could be modified to remove a collaborator, or to change a collaborator's permissions. Remember to replace `'your_github_pat'` with your actual GitHub PAT and adjust the organization names and usernames as needed.

Also, please be aware of GitHub API rate limits. For authenticated requests, you can make up to 5,000 requests per hour. If you're working with a large number of repositories, you might need to add some logic to your scripts to handle the rate limit.
