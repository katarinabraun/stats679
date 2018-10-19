# kristin's notes on using git

## useful commands

- `git status`: checks status of tracked files
- `git log`: look at repository history
  - `git log --abbrev-commit --pretty=oneline`: succint history
- `git show`: shows last commit
- `git diff`: differences between working and staging
  - `git diff --staged`: differences between
  staging and last commit

## how to: initalize a repo on your local machine

- `git init`
- `git add filenames`
- `git commit -m "message"`

## important reminders

- use git to mv and rm files! this is the easiest
  way to track them efficiently

## how to: track/share in github repository

- add new repository on github, can add .gitignore 
  and readme at this point
- `git remote add git@github.com...`
- `git remote -v`: to check it is set up correctly
- `git branch`: check branch name
- `git push origin master`: push local repo to github
  