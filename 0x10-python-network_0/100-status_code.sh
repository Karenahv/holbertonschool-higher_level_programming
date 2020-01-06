#!/bin/bash
# takes a uRL, return status code
curl -so /dev/null -w "%{http_code}" "$1"
