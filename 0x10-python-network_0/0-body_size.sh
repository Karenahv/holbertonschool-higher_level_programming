#!/bin/bash
# takes a uRL, sends a request and displays the size of the body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
