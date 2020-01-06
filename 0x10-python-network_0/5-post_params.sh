#!/bin/bash
# takes a uRL, method POST
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
