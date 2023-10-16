#!/bin/bash
#Author: Daniel Rebich
#Sept. 14, 2023 - Version 1
#----------------------------
for((i=1; i<1000+1; i++));do
	echo $i >> ourTest_1.txt;
done

tail -10 ourTest_1.txt > ourTest_2.txt;
