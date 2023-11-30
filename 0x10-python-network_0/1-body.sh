#!/bin/bash
#count
v=0; rep=$(curl -s "$1"); for ((i = 0; i < ${#rep}; i++)); do v=$((v+1)); done; echo "${v}"
