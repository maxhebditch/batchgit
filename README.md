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
        $ batchgit -s ./
        $ batchgit -s repo1 repo2 repo3

The script will pull the list of git repos it's tracking from the configuration file and will list any modified, untracked or commited files in red. Alternatively just current or a list of specific ones. The specific repos, `repo1`, `repo2`, and `repo3` in the above example, have to be in your `~/.batchgitrc` file.

###git pull

        $ batchgit -pull
        $ batchgit -d
        $ batchgit -d ./
        $ batchgit -d repo1 repo2 repo3

Script will loop through git repositories and pull from remote source. Or just specific ones or current.

###git push

        $ batchgit -push
        $ batchgit -u
        $ batchgit -u ./
        $ batchgit -u repo1 repo2 repo3

Script will loop through git repositories, pull first to avoid conflicts and then push to remote source. Can be done on all repos or just specific pnes.

        $ batchgit -pushonly
        $ batchgit -po
        $ batchgit -po ./
        $ batchgit -po repo1 repo2 repo3

Script will only push rather than pull then push.

###git commits

        $ batchgit -c "updated readme"
        $ batchgit -commit
        $ batchgit -cp

You can commit changes using `-c` or `-commit` and a commit message in quotes. If you don't provide a message, I don't massively recommend it, but if you are in a hurry you can use a generic message from [what the commit](http://whatthecommit.com/) because it is more fun than a static message. The `-cp` flag will push as well after writing a commit message.

##Bootstrapping

###backup
The script can be used to make a backup list of all the current `git` repos on the disk. 

        $ batchgit --backup

This will go through each repo asking if they should be backed up or not. At the moment the script only works with the first remote repo, if you have many you may have to change this amnually, see below. Once completed the script will create a folder at `~/batchgit-takeaway`. This should then be copied to the new machine with a copy of the `batchgit` shell script. 

###clone
Once in the new machine the script should be run as follows

        $ batchgit --clone

This will then go through the files in the `~/batchgit-takeaway` folder and ask if each repo should be cloned. The way the script works is to directly mirror the filepaths the repos were in on the old system. If you want to change this you can look at the filepaths in `~/batchgit-takeaway/bootstrapdir` and adjust accordingly. The first filepath will be used for the first remote repo in `~/batchgit-takeaway/bootstraprepo`.

###wipe

The script can now also be used to wipe multiple repos at once using

        $ batchgit --wipe

As usual, it will find the repos and ask you one at a time which you want to keep. Or singular repos as so

        $ batchgit --wipe ./
        $ batchgit --wipe repo1 repo2 repo3

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
11. ~~`git clone` using `~/.batchgitrc` file~~
7. Add a secondary, larger list for less frequent monitoring or maybe just pulling
13. `rm` all untracked files
14. Alphabetical printing of repo
15. ~~multiple wipes~~
16. ~~Optimise loops~~
17. Remove `./` as its not needed
18. Loop for checking batchgitrc presence
19. ~~Turn git status into a function~~
20. ~~Batchgit push single directories~~
21. Offer alternative to whatthecommit message
22. ~~Update README with specific folder pushing~~
23. Add multiple repos to batchgit -remove
24. Think about nomenclature
25. Add support for specific repos by path for pushing pulling statusing etc
