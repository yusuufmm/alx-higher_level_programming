#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request and display the size of the response body in bytes
curl -s "$1" | wc -c

