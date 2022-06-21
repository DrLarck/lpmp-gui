#!/usr/bin/bash

# const
SRC="src"
BIN="bin"
MAIN="$SRC/main.py"
target_name="lpmp-gui"

# color
blue="\033[1;34m"
purple="\033[0;35m"
green="\033[1;32m"
nc="\033[0m"

function init_message() {
    echo -e -n "${blue}$1${nc} ${purple}$2${nc} ..."
}

function done_message() {
    echo -e "... ${green}DONE${nc}"
}

function init() {
    init_message "init" "directories"
    bash init.sh
    done_message
}

function clear_bin() {
    init_message "cleaning" "bin"
    rm -r bin/*
    done_message
}

function build_exec() {
    init
    clear_bin

    init_message "building" "executable"

    cxfreeze \
        --target-name=$target_name \
        --target-dir=$BIN \
        --silent \
        $MAIN

    done_message
}

build_exec
