#!/bin/bash
# takes a uRL, method POST
curl -sd "emaiL=hr@holbertonschool.com&subject=I will always be here for PLD" -X "POST" "$1" 
