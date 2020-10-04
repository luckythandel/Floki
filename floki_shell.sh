#!/bin/bash

read -p "File Path: " FILE
read -p "Outcome Length: " NUM
read -p "Mode[0,1,2]: " MODE
read -p "Output File: " OUTPUT_FILE

if [ -f "$FILE" ]; then
	echo "Working on It\n"
	CONS=0
	while IFS= read -r LINE
	do
		python3 main.py $LINE $NUM -m $MODE -o $OUTPUT_FILE 
		echo "Line $CONS Completed"
		CONS=`expr "$CONS" + 1`	
	done < $FILE

	
fi
