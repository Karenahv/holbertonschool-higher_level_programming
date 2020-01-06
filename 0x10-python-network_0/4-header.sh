#!/bin/bash
# takes a uRL, sends a header
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1" 
