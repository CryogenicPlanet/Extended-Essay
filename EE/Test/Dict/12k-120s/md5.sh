hashcat -t 32 -a 0 ../Test/Dict/12k-120s/md5.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=120 --machine-readable
