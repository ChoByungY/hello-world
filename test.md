# Test for git command

## Text file sub line

1. write command line
2. working test

## Working history

1. add text file into remote repository
2. and add and commit and after then
3. Create LocalTest_V1.1 branch
   * git branch LocalTest_V1.1
   * git checkout LocalTest_V1.1
4. Make another feature or git test in this branch
   * git mv test.txt to test.md
5. Edit some change in test.md file
6. commit the change into LocalTest_V1.1
   * git commit -am "rename test.md & modify test.md"
7. Remote add the branch
   * git push --set-upstream origin LocalTest_V1.1
8. Pull request handling in gitHub
9. Merge in local branch
   * git checkout master
   * git merge LocalTest_V1.1
   * git -d LocalTest_V1.1
