hashcat -m -t 32 -a 0 ../Test/Dict/John/Md5.hash ../rockyou.txt -r ./rules/dive.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=120 --machine-readable
