#!/bin/bash
# Welcome script to display a message to users on login
# Author :@CYBERGAINT
# Date : 21-02-23
source $HOME/snippets/colors
if [ $# -lt 1 ]; then
	echo -e "${RED}Usage: $0 <name> $RESET"
	exit 1
fi
echo -e "${GREEN}Hello $1$RESET"
