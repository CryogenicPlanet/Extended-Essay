hashcat -t 32 -m 1400 -a 0 ../Test/Dict/12k-300s/sha256.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=300 --machine-readable
