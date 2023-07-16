import requests
import time

# GitHub API 请求头部信息，需要替换为您自己的访问令牌（Token）
headers = {
    'Authorization': 'Bearer your_github_pat'
}

# 要 fork 的企业组织和新的企业租户名称
org_name = 'supabase'
new_org_name = 'openmodels'

# 获取企业组织的仓库列表
page = 1
repos = []

while True:
    repo_url = f'https://api.github.com/orgs/{org_name}/repos?page={page}'
    response = requests.get(repo_url, headers=headers)

    if response.status_code != 200:
        print(f'Failed to fetch repositories. Status code: {response.status_code}, Message: {response.text}')
        break

    page_repos = response.json()

    if not page_repos:  # If no more repositories
        break

    repos.extend(page_repos)
    page += 1

# 批量 fork 仓库到新的企业租户
for repo in repos:
    # Check if the repository has already been forked in the new organization
    fork_check_url = f'https://api.github.com/repos/{new_org_name}/{repo["name"]}'
    fork_check_response = requests.get(fork_check_url, headers=headers)

    if fork_check_response.status_code == 200:
        print(f'Repository already forked: {repo["name"]}. Skipping...')
        continue

    fork_url = f'https://api.github.com/repos/{org_name}/{repo["name"]}/forks'
    fork_data = {'organization': new_org_name}
    response = requests.post(fork_url, headers=headers, json=fork_data)

    if response.status_code == 202:
        print(f'Successfully forked: {repo["name"]}')
    elif response.status_code == 403:
        print(f'Rate limit hit. Sleeping for a bit...')
        time.sleep(600)  # wait for 10 minutes
    else:
        print(f'Failed to fork: {repo["name"]}. Status code: {response.status_code}, Message: {response.text}')
