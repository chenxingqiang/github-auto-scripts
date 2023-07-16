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
