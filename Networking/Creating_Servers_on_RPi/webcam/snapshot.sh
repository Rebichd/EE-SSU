#!/bin/bash

for i in {1..10};
do
        DATE=$(date +"%F_%H%M%S");
        echo "Welcome $i times";
        sleep 5; #waits 5 seconds
        fswebcam -r 1280x720 --no-banner $DATE.jpg;
done
