# Test for git command

## Text files

1. Use CLI(command line interface) or VSCODE commands
2. working test

## Working scenario

1. Create LocalTest_Vx.x branch
   * git checkout -b LocalTest_Vx.x
2. Add and modify some files into local repository
3. and staging and commit them
   * git commit -am "Some comments on commit"
7. Remote add the branch
   * git push --set-upstream origin LocalTest_Vx.x
8. Pull request handling in gitHub
9. Merge in local branch
   * git checkout master
   * git pull
   * git branch -d LocalTest_Vx.x
