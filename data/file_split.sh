#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 filename N"
    exit 1
fi

filename="$1"
N="$2"

# Extract the base name and extension
base_name=$(basename "$filename" | sed 's/\(.*\)\..*/\1/')
extension="${filename##*.}"

# Calculate the total number of lines
total_lines=$(wc -l < "$filename")
lines_per_file=$(( (total_lines + N - 1) / N ))

# Split the file
split -d -l "$lines_per_file" "$filename" "${base_name}_"

# Rename files to the desired format
counter=0
for file in ${base_name}_*; do
    mv "$file" "${base_name}_${counter}.$extension"
    counter=$((counter + 1))
done
