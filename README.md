batchgit
========

A shell script for maintaining git repositories system wide. The script maintains a list of git repositories on your disk, allowing you to run git status, git pull or git push in each folder at once. On initial run the script searches for all `.git` folders and asks which you want to add to the list. New repos can be added manually as they are created, repos can be deleted manually from the list manually or will be automatically deleted if they no longer exist.

##Configuration
When the script is first run it looks for a dot file called `~/.batchgitrc`. If this doesn't exist, as it won't the first time you run this script, it will search for all of the git repos on the disk and ask if you want to add them to the file or not. Repos added will be monitored, others will not be. This is useful if you used git clone to get a program or script but don't want to monitor it every time.

##How to run

###Initial run

The configuration file won't exist so the script will search for git repos across the disk. It will list each one it finds and ask if you want to track it. You can add them using Y/y, or ignore them using N/n.

###Multiple choice

        $ batchgit

This will offer a multiple choice for different options which can be selected using the numbers.

###Resetting configuration file

        $ batchgit -f
        $ batchgit -find
        $ batchgit -f /var

These will search for git repos across the whole disk. It will rewrite the configuration file, but it will save a backup to `~/.batchgitrc.bak`. By default it searches `~`, otherwise you can specify the location.

###Adding single directores manually

        $ batchgit -a ~/path/to/repo
        $ batchgit -add ~/path/to/repo
        $ batchgit -a ./
        $ batchgit -a repo 

The use of the `-a` flag will append the directory to the configuration file. This option will make the configuration file if it doesn't already exist, allowing you to manually add dirs rather than go through the setup. 

Using `./` for either of the add flags will add the current directory to the configuration file. Otherwise you can specify the sub directory using the last command, or use the entire path.

It will also check to see if the folders in the configuration file still exist, if not it will remove them to avoid issues. 

###Adding directories recursively

        $ batchgit -ar
        $ batchgit -addrecursive
        $ batchgit -ar ./
        $ batchgit -ar /path/to/master/directory

If all your repos live under one master directory, you might just want to only add subdirectories. If you `cd` into the correct master directory and then run the command alone or with `./` the script will ask you what subdirectories from the current folder you want to add. Alternatively, the last command lets you set the master directory from anywhere.

###Removing single directores manually

        $ batchgit -r ~/path/to/repo
        $ batchgit -rm ~/path/to/repo
        $ batchgit -remove ~/path/to/repo
        $ batchgit -r ./
        $ batchgit -r repo

This flag works exactly the opposite to the previous one. Instead of adding single directories it will remove them. Either the whole path can be specified, the current folder, or using the last flag, a sub directory of the current folder (useful as can use autocomplete).

###git status

        $ batchgit -status
        $ batchgit -s

The script will pull the list of git repos it's tracking from the configuration file and will list any modified, untracked or commited files in red.

###git pull

        $ batchgit -pull
        $ batchgit -d

Script will loop through git repositories and pull from remote source.

###git push

        $ batchgit -push
        $ batchgit -u

Script will loop through git repositories, pull first to avoid conflicts and then push to remote source.

        $ batchgit -pushonly
        $ batchgit -po

Script will only push rather than pull then push

###git commits

        $ batchgit -c
        $ batchgit -commit
        $ batchgit -cp

I don't massively recommend it, but if you are in a hurry you can use this flag to commit with a generic message from [what the commit](http://whatthecommit.com/) because it is more fun than a static message. The `-cp` flag will push as well after writing a commit message.

##FAQs
###Why are some of my repos not being found?
When initially run, or using the `-f` flag alone, it will only search from your home folder. To find repos in other locations you need to use a location after the `-f` or use the add recursively function. 

##TODO
2. ~~Tidy up output.~~ [ga7go8]
3. ~~Add generic commit message.~~
5. ~~Strip out # you sometimes see in git~~
8. ~~Add a `-d` flag for removing directory~~
9. ~~Add folders recursively from current location to configuration file.~~
10. ~~Handle directories that have been deleted since config file wrote~~
12. ~~Say whether one commit ahead or behind rather than just different~~
4. `cd` to places where changes have happened.
11. `git clone` using `~/.batchgitrc` file  
7. Add a secondary, larger list for less frequent monitoring or maybe just pulling
