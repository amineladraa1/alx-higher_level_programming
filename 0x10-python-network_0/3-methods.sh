#!/bin/bash
# Display all HTTP methods the
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
