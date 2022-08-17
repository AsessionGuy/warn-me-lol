import sys
try:
    import psutil
except ModuleNotFoundError:
    sys.exit("Could not find psutil module")
try:
    import playsound
except ModuleNotFoundError:
    sys.exit("Could not find playsound module")
import threading
import zipfile
import time
import os
import urllib.request

PLATFORM = sys.platform

if not os.path.exists("./extreme-alarm-sound.mp3"):
    URL = "https://www.freesoundslibrary.com/wp-content/uploads/2019/11/extreme-alarm-sound.zip"
    HEADERS = ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [HEADERS]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(URL,"./alarm.zip")
    with zipfile.ZipFile("./alarm.zip", "r") as zip:
        zip.extractall()
        
while True:
    for process in psutil.process_iter():
        if process.name()[0:12] == "LeagueClient":
            t_end = time.time() + 30
            while time.time() < t_end:
                threading.Thread(playsound.playsound(os.path.abspath("./extreme-alarm-sound.mp3")))
            break
    time.sleep(10)

