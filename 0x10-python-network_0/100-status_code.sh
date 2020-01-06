#!/bin/bash
# takes a uRL, return status code
curl -o /dev/null -s -w "%{http_code}\n" "$1"
