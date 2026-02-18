#!/usr/bin/env bash
# Thanks: https://www.datafix.com.au/BASHing/2021-10-13.html
set -eu
awk -v FS="\t" -v OFS="," '{for (i=1;i<=NF;i++) {x=gensub(/"/,"\"\"","g",$i); if (x ~ /"/ || x ~ /,/) $i="\""x"\""; else $i=$i}} 1' "$1" | sed "s/\r$//" > "$(echo "$1" | xargs -n 1 basename | sed "s/\..*//")".csv
