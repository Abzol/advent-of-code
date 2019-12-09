#!/bin/bash

max=0

while read p; do
    IFS=', ' read -r -a arr <<< "$p"
    cur=0
    for i in "${arr[@]}"; do
        cur=$(./7.py "$i" "$cur" input)
    done
    if [ "$cur" -gt "$max" ]
    then
        max="$cur"
    fi
done <permutations
echo "$max"
