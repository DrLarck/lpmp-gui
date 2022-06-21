#!bin/bash
directories=("bin")

for dir in "${directories[@]}"
do
    # if the directory doesn't exist
    if [ ! -d $dir ]; then
        echo "Creating directory \"$dir\""
        mkdir $dir
    fi
done
