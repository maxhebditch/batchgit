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
        $ batchgit -g /media/

These will search for git repos across the whole disk. It will rewrite the configuration file, but it will save a backup to `~/.batchgitrc.bak`. By default it searches `~`, otherwise you can specify the location using `-g`.

###Adding single directores manually

        $ batchgit -a ~/path/to/repo
        $ batchgit -a ./
        $ batchgit -a repo 

The use of the `-a` flag will append the directory to the configuration file. This option will make the configuration file if it doesn't already exist, allowing you to manually add dirs rather than go through the setup. 

Using `./` for either of the add flags will add the current directory to the configuration file. Otherwise you can specify the sub directory using the last command, or use the entire path.

It will also check to see if the folders in the configuration file still exist, if not it will remove them to avoid issues. 

###Adding directories recursively

        $ batchgit -l
        $ batchgit -l ./
        $ batchgit -l /path/to/master/directory

If all your repos live under one master directory, you might just want to only add subdirectories. If you `cd` into the correct master directory and then run the command alone or with `./` the script will ask you what subdirectories from the current folder you want to add. Alternatively, the last command lets you set the master directory from anywhere.

###Removing single directores manually

        $ batchgit -r ~/path/to/repo
        $ batchgit -r ./
        $ batchgit -r repo

This flag works exactly the opposite to the adding one. Instead of adding single directories it will remove them. Either the whole path can be specified, the current folder, or using the last flag, a sub directory of the current folder (useful as can use autocomplete).

###git status

        $ batchgit -s

The script will pull the list of git repos it's tracking from the configuration file and will list any modified, untracked or commited files in red.

###git pull

        $ batchgit -d

Script will loop through git repositories and pull from remote source.

###git push

        $ batchgit -u

Script will loop through git repositories, pull first to avoid conflicts and then push to remote source.

        $ batchgit -p

Script will only push only rather than pull then push.

###git commits

        $ batchgit -c "updated readme"

You can commit changes using `-c` and a commit message in quotes. This will apply to all files that are untracked, modified and added in all directories so it can be messy.

##Bootstrapping

###backup
The script can be used to make a backup list of all the current `git` repos on the disk. 

        $ batchgit -b

This will go through each repo asking if they should be backed up or not. At the moment the script only works with the first remote repo, if you have many you may have to change this amnually, see below. Once completed the script will create a folder at `~/batchgit-takeaway`. This should then be copied to the new machine with a copy of the `batchgit` shell script. 

###clone
Once in the new machine the script should be run as follows

        $ batchgit -n

This will then go through the files in the `~/batchgit-takeaway` folder and ask if each repo should be cloned. The way the script works is to directly mirror the filepaths the repos were in on the old system. If you want to change this you can look at the filepaths in `~/batchgit-takeaway/bootstrapdir` and adjust accordingly. The first filepath will be used for the first remote repo in `~/batchgit-takeaway/bootstraprepo`.

###wipe

The script can now also be used to wipe multiple repos from the disk

        $ batchgit -w

As usual, it will find the repos and ask you one at a time which you want to keep.

##Alternative batchgitrc file

An alternative rc file can be used as so

        $ batchgit -o /dir/to/path

This allows having multiple different sets of files. For example, work related repos, coding related repos, game related repos, or just a small subset of fast and slow repos can be made.
To write this file you need to combined the `-o` and `-f` flags

        $ batchgit -f -o /dir/to/path

and a new rc file will be written. To then use this rc file, combine it with the above flags, for example.

        $ batchgit -s -o /dir/to/path
        $ batchgit -u -o /dir/to/path
        $ batchgit -d -o /dir/to/path
        $ batchgit -p -o /dir/to/path

##FAQs
###Why are some of my repos not being found?
When initially run, or using the `-f` flag alone, it will only search from your home folder. To find repos in other locations you need to use a location after the `-g` or use the add recursively function. 

##TODO
26. Git checkout master for all repos
25. Add support for specific repos by path for pushing pulling statusing etc
13. `rm` all untracked files
14. Alphabetical printing of repo
23. Bring back arguements after the flags, hard with getopts
2. ~~Tidy up output.~~ [ga7go8]
3. ~~Add generic commit message.~~
5. ~~Strip out # you sometimes see in git~~
8. ~~Add a `-d` flag for removing directory~~
9. ~~Add folders recursively from current location to configuration file.~~
10. ~~Handle directories that have been deleted since config file wrote~~
12. ~~Say whether one commit ahead or behind rather than just different~~
17. ~~Remove `./` as its not needed~~
11. ~~`git clone` using `~/.batchgitrc` file~~
15. ~~multiple wipes~~
16. ~~Optimise loops~~
19. ~~Turn git status into a function~~
20. ~~Batchgit push single directories~~
22. ~~Update README with specific folder pushing~~
7. ~~Add a secondary, larger list for less frequent monitoring or maybe just pulling~~
18. ~~Loop for checking batchgitrc presence~~
