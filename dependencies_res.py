# Run this script where you want to install simple_ehm

import platform
import subprocess

sys = platform.system()

if sys == 'Linux':
    # install ffmpeg into the system from apt
    '''cmd_apt = ['sudo', 'apt', 'install', 'ffmpeg']
    subprocess.Popen(cmd_apt, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()'''
    subprocess.Popen('./setup/Linux.sh', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
elif sys == 'Windows':
    # get the ffmpeg archive file
    '''wget_url = 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z'
    cmd_wget = ['wget', wget_url, '-UseBasicParsing', '-o', 'ffmpeg.7z']
    subprocess.Popen(cmd_wget, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    # extract the ffmpeg archive
    cmd_7z = ['7z', 'x', './ffmpeg.7z']
    subprocess.Popen(cmd_7z, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    # remove the ffmpeg archive file
    cmd_7z = ['rm', './ffmpeg.7z']
    subprocess.Popen(cmd_7z, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()'''
    # add ffmpeg binaries to Path variable
    # TODO
    # setx path "%path%;D:\Dario\Download\ffmpeg-4.3.1-2020-11-19-full_build\bin"
else:
    print("OS not supported at the moment.")
    exit(1)

pip install matplotlib numpy seaborn tensorflow tqdm psutil opencv-python
