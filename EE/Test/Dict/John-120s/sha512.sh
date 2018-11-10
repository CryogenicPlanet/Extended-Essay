hashcat -m 1700 -t 32 -a 0 ../Test/Dict/John/sha512.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=120 --machine-readable
