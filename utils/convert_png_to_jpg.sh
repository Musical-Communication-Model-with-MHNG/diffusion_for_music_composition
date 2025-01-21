#!/bin/bash

# globstarオプションを有効にする
shopt -s globstar

DIRECTORY="/raid/haruto-uenoyama/diffusion_for_music_composittion/dataset/classical/img"
echo "Searching for PNG files in $DIRECTORY"

for file in "$DIRECTORY"/**/*.png; do
  echo "Checking file: $file"
  if [ -f "$file" ]; then
    output_file="${file%.png}.jpg"
    magick convert "$file" "$output_file"
    if [ $? -eq 0 ]; then
      echo "Converted $file to $output_file"
    else
      echo "Failed to convert $file"
    fi
  else
    echo "No PNG files found in $DIRECTORY"
  fi
done