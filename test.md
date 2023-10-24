# Test for git command

## Text files

1. Use CLI(command line interface) or VSCODE commands
2. working test

## Working scenario

1. Create develop branch
   * git switch -c develop
2. Use develop branch at nomal developing
3. Add and modify some files into local repository
4. and staging and commit them
   * git commit -am "Some comments on commit"
5. Remote add the branch
   * git push --set-upstream origin develop
6. Pull request handling in gitHub
7. Merge in local branch
   * git switch master
   * git merge origin develop
   * git push origin
   * git switch develop
8. Again running 2 to 7
