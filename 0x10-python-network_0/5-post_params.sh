#!/bin/bash
# takes a uRL, method POST
curl -sd "emaiL=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X "POST" "$1" 
