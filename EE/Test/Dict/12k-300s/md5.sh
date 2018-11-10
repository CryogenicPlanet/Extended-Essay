hashcat -t 32 -a 0 ../Test/Dict/12k-300s/md5.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=300 --machine-readable
