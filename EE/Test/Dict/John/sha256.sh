hashcat -m 1400 -t 32 -a 0 ../Test/Dict/John/sha256.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=120 --machine-readable
