#!/bin/bash

# Check if a URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Use curl to send a request and get the size of the response body
response_size=$(curl -s "$url" | wc -c)

# Display the response size in bytes
echo "Response size: ${response_size} bytes"

