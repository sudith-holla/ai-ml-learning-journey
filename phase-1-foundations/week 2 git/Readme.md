Git and GITHUB notes



what is git?

version control system that keeps track of all the changes made to our files of any kind in a local computer. It also stores the history of changes.



why is it useful?

Every time we change some files of our project and then commit them, Git will store a snapshot of what all the file look like at that point in time. This is stored as a version of our project. Every time we change files and commit them, we create new versions of our project. Git stores all these versions and we can revert to any of the previous versions easily with the help of Git. Very useful when we are working on a project and keep making changes to it.



what is GitHub?

When it comes to building a software or anything big, there will be multiple teams working on it on their own computers. This is where GITHUB comes in. Everyone making changes are basically creating new versions of the project and they live in their own computers. GitHub allows people to update and push their versions of project into a central server which is accessible to everyone involved in the project. GitHub then merges everything together and creates a polished version of the project.



Three stages of GIT:

1\. Working directory: This is where we actually work on our files or project. We make changes, delete and play with the files.

2\. Staging area: This is an intermediate stage sits between commit and working directory. The  changes made to files in working directory are pushed to staging area where these files will wait to be committed. This allows users to review their changes and confirm them.

3\. commit: This creates a snapshot of the entire project. Basically saves the entire project in the repository as a version of it every time we commit.



What is repository?

Its a folder where GIT stores everything. Versions, History of changes, Who made the changes etc



There are two types of files:

1\. Tracked: These are the files that GIT already knows about from its last commit or the newly stages files.

2\. Untracked: These are newly added files or the files that we don't want git to track.



Lets get started with basic GIT commands.

To track a folder, we first need to initialize git in that folder.

Open command prompt->navigate to that folder using 'cd' command-> then use 'git init' command.

ex: cd desktop/myUser

&#x20;   git init

or

if we want to copy an existing git repository into our system we can use the command

git clone 'url'(url can be obtained from the GITHUB website)



Once we initialize git, our folder is ready to be tracked.



Now lets look at the basic functions.



##### Pushing files into staging area:



To push the files into staging area, use command

git add .

This will push all the files and folders in our current directory to staging area.\\\\

We also have 'git add -A'. This will push all the file in our working directory to staging area.

There is one more called 'git a\*'.This will stage all the files except for the deleted ones.

### 

##### Resetting staging area and un-staging files.

we can use 'git reset' to unstage the files. It only brings back the changes and not the deleted files.

Suppose we delete a file and stage it. Now if we use reset, we wont get our deleted file back in our system. we can only reset undeleted files that are staged.

In this case we need to use 'git reset --hard'. This will bring our files back in the system.



##### committing files.

use the command : git commit -m 'This is a commit message'. Here the message should describe what you are committing.

This will create a new version of the project by saving new file along with pointers to unchanged files.



##### Deleting files.

If we manually delete a file from the system, we need to stage it using the command 'git add .'

But 'git rm "file-name"' does the staging work for us.

We dont need to stage the file if we use 'git rm'.

If you modify a file and not stage it and then try to delete it using git rm command, GIT wont let you do it.

You either need to commit the changes or forcefully delete the file using 'git rm -f "filename"'



lets say you tracked a file accidentally or you want to delete a file from the staging area but keep it in the working directory. To do that you can use the command 'git rm --cached "filename"'

If you then run 'git status'. you'll see that the file you deleted from staging area is untracked now.



To delete a file along with its subfolders, use the command 'git rm -r <folder>'. If you don't remove '-r' from the command, only the folder specified will be deleted and not the file or the subfolders int it .



&#x20;

##### Undoing last commit

use the command 'git reset head\~' to undo last commit and bring everything back to the working directory.



##### GIT Branching

Branching creates a clone of whichever branch we want to work on. Its useful when multiple teams are working on the projecn  t and instead of everyone altering the files in the same branch, they can make a clone of that branch and then alter or update the files in that branch. This helps us perform tests or experiments without messing up our project.



#### GIT merging

Combines changes from two branches into one.



Creating a branch

To create a branch, use the command 'git branch "name-of-the-branch"'

to move to a branch, use the command 'git checkout "name-of-the-branch"'

When we create a branch, it inherits the exact state of the branch we are in.



#### Going back to previous versions or commits

To check the previous commits, use the command 'git log --oneline', this gives a list of all the previous commits with their hash value.

To go to one of the previous commits, use the command 'git checkout "hash value"'. 



#### Comparing two commits

To compare between two versions, simply get the hash value for the versions you wanna compare and then use the command 'git diff "hash-value-1" "hash-value-2"'

Here the order of hash values matter.



#### Push, pull and fetch

To push the changes or changes made locally into the remote server, use the command 'git push origin "branch-name"'

To push all the branches into remote server, use 'git push'

'git fetch' fetches the changes made in the remote server but doesn't merge it with the working directory in local computer.

'git pull' fetches and merges the changes with the working directory in the local computer at the same time. 



#### GIT RESTORE

Suppose i make a lot of changes in my working directory to build a new feature, but then i realize that the new feature is unnecessary. In this situation, deleting the newly made changes from all the files manually would be tedious and inefficient. This is where 'git restore' comment comes in. It brings the file/s to the exact state it was in the current commit. 



The difference between git reset head\~ and git restore is that git reset moves the head to the previous commit completely changing the history of the project and deleting the current directory, whereas git restore brings the files to the state from current commit. 



#### GIT Stash

Git doesn't allow us to switch between branches without committing the changes made in a particular branch. If we are not yet ready to commit changes in a branch but need to go to a different branch but not lose our unfinished work, we can use 'git stash'.

This command stashes all the uncommitted changes in the memory. When we run this command, the uncommitted changes will disappear but wont be lost. We can later come back to our branch and work on our changes and commit them when we are ready. 



So, how can get the changes that are stashed somewhere?

There are two different ways to get the changes.

1. Use the command 'git stash pop', this removes the recently added change from the stash list and applies it to the working directory. The changes wont be any longer in the stash list. 
2. If we dont use to remove the changes from the stash list but keep it there for future use and apply the changes into the working directory, use the command 'git stash apply' 

each stashed change has an id and we can apply specific changes in the stash by mentioning their id after the commands above. 

#### 

#### GIT Revert

This brings a file/directory or the whole repository to one of the previous commits without actually erasing commits up until the current commit from that specific commit. 

How? By creating a new commit which would be an exact copy of one of previous commits and adding this into the commit history. Commit history isn't changed but a new commit is added. 



Command: 'git revert "commit-id"'

Here the commit id is the version that needs to be reverted to the one before it and not the version that we want.



#### Pull Request

This is useful when we are working with multiple collaborators. 

We cant just merge branches in someone else's repository without their permission. So Pull request also called as PR is a request that we make to the repository owner and asking them to review the changes we made and to allow us to merge branches. 



&#x20;







