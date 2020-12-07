#!/bin/bash

sudo apt install ffmpeg
if (( $?==0 )); then exit 0 ; fi;
sudo dnf install ffmpeg
if (( $?==0 )); then exit 0; fi;
sudo pacman -S ffmpeg
if (( $?==0 )); then exit 0 ; fi;

echo "distribuzione linux non identificata, installazione di ffmpeg manuale richiesta."
exit 255;
