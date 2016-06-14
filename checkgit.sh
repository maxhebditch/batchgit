#!/bin/bash
# PATH=/opt/someApp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

batchgit=$(/home/max/github/batchgit/batchgit -q)

if [[ "$batchgit" =~ "Changes" ]]; then
        commit=TRUE
        nochanges=FALSE
fi
if [[ "$batchgit" =~ "Push" ]]; then
        push=TRUE
        nochanges=FALSE
fi
if [[ "$batchgit" =~ "Pull" ]]; then
        pull=TRUE
        nochanges=FALSE
fi
if [[ "$nochanges" != "FALSE" ]]; then
        nochanges=TRUE
fi

if [[ $nochanges == "TRUE" ]]; then
        echo "" > ~/.batchgitquery
        exit
else
        if [[ $commit ]]; then
                echo "making commit"
                commitlogo=""
        else
                commitlogo=""
        fi
        if [[ $push ]]; then
                echo "making push"
                pushlogo=""
        else
                pushlogo=""
        fi
        if [[ $pull ]]; then
                echo "making pull"
                pulllogo=""
        else
                pulllogo=""
        fi
        echo " $commitlogo $pushlogo $pulllogo" > ~/.batchgitquery
fi
