#!/bin/bash
# takes a uRL, method POST
curl -s -X POST -d @"$2" -H "Accept: application/json" -H "Content-Type: application/json" "$1"
