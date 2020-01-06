#!/bin/bash
# takes a uRL, and displays all http methods
curl -sI "OPTIONS" "$1" | grep -i Allow | cut -d' ' -f2-
