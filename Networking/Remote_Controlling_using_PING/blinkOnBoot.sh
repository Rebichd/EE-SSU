#!/bin/bash
gpio -g mode 17 out #BCM mode
while true
do
        echo LED on
        gpio -g write 17 1
        sleep 0.5
        echo LED off
        gpio -g write 17 0
        sleep 0.5
done
