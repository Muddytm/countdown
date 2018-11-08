import time

# Change these to whatever you want :)
minutes = 5
seconds = 0

while minutes >= 0 and seconds >= 0:
    with open("timefile.txt", "w") as f:
        if seconds < 10:
            f.write(str(minutes) + ":0" + str(seconds))
            #print (str(minutes) + ":0" + str(seconds))
        else:
            f.write(str(minutes) + ":" + str(seconds))
            #print (str(minutes) + ":" + str(seconds))

    if seconds == 0:
        minutes -= 1
        seconds = 59
    else:
        seconds -= 1

    time.sleep(1)
