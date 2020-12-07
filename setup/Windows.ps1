# get the ffmpeg archive file
set -Name wget_url -Value "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
wget $wget_url -UseBasicParsing -o ffmpeg.7z
# extract the ffmpeg archive
7z x ./ffmpeg.7z
# remove the ffmpeg archive file
rm ./ffmpeg.7z
# add ffmpeg binaries to Path variable

PAUSE
