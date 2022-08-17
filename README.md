# warn-me-lol

## Description

Simple python script that warns you by playing some <strong>alarming</strong> audio whenever it detects "LeagueClient" (or any other related process) running.

The sound I that used can be found at [freesoundslibrary.com](https://www.freesoundslibrary.com/extreme-alarm-sound/), it was submitted by "SPANAC" but you can change it (mp3 files are recommended).

***
## Requiriments

Requires Python3.x and pip. It has been tested on Windows 11 and Linux (Manjaro)

playsound and psutil libraries are also needed, they can be downloaded via pip:

`python3 -m pip install playsound psutil` or `py -m pip install playsound psutil`
***

### Note

It doesn't check for Riot Games Services so you are free to play Valorant, LoR, etc.
