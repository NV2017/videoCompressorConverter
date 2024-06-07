# main.py

# The Goal of this program is:
# 1. to convert and compress videos
# 2. convert to libx265 for compression
# 3. covert to .mp4, as many apps play it directly sans downloading into the device
# 4. If subtitle, hard-sub it
# 5. In future, develop a UI front-end

from imports import *

def main():
    utcTimezone = pytz.utc
    timeStart = dt.datetime.now(utcTimezone)
    print("Program {0} started at: {1}".format(__name__, 
                                        timeStart.strftime("%y-%m-%d %H:%M:%S")))

    videoConvertorCompressor()
    
    timeEnd = dt.datetime.now(utcTimezone)
    print("Program {0} ended at: {1}, in {2} seconds".format(   __name__, 
                                                                timeEnd.strftime("%y-%m-%d %H:%M:%S"),
                                                                (timeEnd-timeStart).total_seconds()))
    del([utcTimezone,timeStart,timeEnd])
# End of 'def main():'

if __name__ == "__main__":
    main()
# End of 'if __name__ == "__main__":'