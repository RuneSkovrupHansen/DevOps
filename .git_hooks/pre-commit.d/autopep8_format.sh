#!/bin/bash
# Script automatically clang formats any files which are not formatted.

files=$(git diff --name-only --cached)
for file in $files
do
    # Skip deleted files
    if [[ ! -f "$file" ]]
    then
        continue
    fi

    # Skip non-py files.
    if [[ ! "$file" =~ \.py$ ]] 
    then
        continue
    fi

    # Arguments for autopep8
    args="--max-line-length 999"

    # The arguments should be synced with vsc. There
    # are some issues with config files which prevents
    # their use in this case. 

    # Check for differences, discard output.
    diff=$(autopep8 --diff $args "$file")

    # Skip files without format differences, if diff size is 0.
    if [[ ${#diff} == 0 ]]
    then
        continue
    fi

    echo "Auto formatting '$file'"
    autopep8 -i $args "$file"
    git add "$file"

done

exit 0
