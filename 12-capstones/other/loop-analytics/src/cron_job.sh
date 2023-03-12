#! /bin/bash

set -e

# change context to this location
cd "${0%/*}"

# record start
date=`date +'%Y-%m-%d %H:%M:%S %Z'`
echo "${date} Start Running... $HOME/bin/run_nightly.sh;" >> $HOME/logs/run_log.txt

# Capture timing in the runlog
date=`date +'%Y%m%d_%H%M%S%Z'`
{ time sh run_nightly.sh  2>> $HOME/logs/output_${date}.log; } 2>> $HOME/logs/run_log.txt;

# Clean-up old logs
for x in `ls -tr $HOME/logs/output_* | head -n -24`; do rm ${x}; done

#record end
date=`date +'%Y-%m-%d %H:%M:%S %Z'`
echo "${date} Stop Running... $HOME/bin/run_nightly.sh;" >> $HOME/logs/run_log.txt
