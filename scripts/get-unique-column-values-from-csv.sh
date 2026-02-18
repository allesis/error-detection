#!/usr/bin/env bash

# Thanks: https://gist.github.com/thomas-optimove/2616bd242be059fb2ec7cd1762946b15
# Check for the correct number of arguments
if [[ $# -ne 2 ]]; then
	echo "Usage: $0 <csv_file> <column_number>"
	exit 1
fi

# Arguments
CSV_FILE="$1"
COLUMN_NUMBER="$2"

# Check if the file exists
if [[ ! -f "$CSV_FILE" ]]; then
	echo "Error: File '$CSV_FILE' not found!"
	exit 1
fi

# Check if the column number is valid (greater than 0)
if [[ ! "$COLUMN_NUMBER" =~ ^[0-9]+$ ]] || [[ "$COLUMN_NUMBER" -lt 1 ]]; then
	echo "Error: Column number must be a positive integer."
	exit 1
fi

# Extract the specified column, remove the header, and get unique values
awk -F, -v column_number="$COLUMN_NUMBER" '
NR == 1 {
	# Ensure the column number is valid by checking the number of fields
	if (column_number > NF) {
		print "Error: Column number " column_number " is out of range."
		exit 1
	}
	next
}
{
	print $column_number
}' "$CSV_FILE" | sort | uniq
