# Delay for tests if infiniteLoop is active
infiniteLoopTime = 20 # Seconds

import sys
import time
from datetime import datetime

import speedtest
speedtester = speedtest.Speedtest()

download = False
upload = False
ping = False
infiniteLoop = False

if "d" in sys.argv:
    download = True
if "u" in sys.argv:
    upload = True
if "p" in sys.argv:
    ping = True
if "i" in sys.argv:
    infiniteLoop = True
if (not download and not upload and not ping):
        download = True
        upload = True

def test():
    speedtester.get_best_server()
    if(download):
        speedtester.download()
    if(upload):
        speedtester.upload(pre_allocate=False)
    results = speedtester.results.dict()
    print("\n[%s] Test completed, results:" % datetime.now().strftime("%H:%M:%S"))
    if(download):
        print("Download: %s Mbps" % str(round(float(results["download"]) / 1000000, 2)))
    if(upload):
        print("Upload: %s Mbps" % str(round(float(results["upload"]) / 1000000, 2) ))
    if(ping):
        print("Ping: %s ms" % str(round(results["ping"], 2)))

def main():
    test()
    while(infiniteLoop):
        time.sleep(infiniteLoopTime)
        test()

if __name__ == "__main__":
    main()
