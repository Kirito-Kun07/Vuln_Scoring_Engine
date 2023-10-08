#!/bin/bash

# Download the updated file
wget https://raw.githubusercontent.com/Kirito-Kun07/Vuln_Scoring_Engine/main/past_images/50-vuln-image/DONT_TOUCH_ME.py

# Sleep for a short duration to ensure the download is complete
sleep 1s

# Make the downloaded file executable
chmod +x DONT_TOUCH_ME.py

# Define the destination directory
destination_dir="/opt/Vuln_Scoring_Engine/"

# Remove the existing 'DONT_TOUCH_ME.py' file in the destination directory
rm "${destination_dir}DONT_TOUCH_ME.py"

# Sleep for a short duration
sleep 1s

# Move the downloaded file to the destination directory
mv -f DONT_TOUCH_ME.py "${destination_dir}"
