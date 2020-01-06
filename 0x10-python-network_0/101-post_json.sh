#!/bin/bash
# takes a uRL, method POST
curl -s -X POST -d @"$2" "Content-Type: application/json" "$1"
