hashcat -t 32 -m 1700 -a 0 ../Test/Dict/12k-300s/sha512.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=300 --machine-readable
