hashcat -t 32 -a 0 ../500dict/12000MD5.hash ../rockyou.txt -r ./rules/rockyou-30000.rule -w 4 --potfile-disable --quiet --status-timer=1 --status --runtime=120 --machine-readable
