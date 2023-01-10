//For example, to halt the system at 10pm, type:
sudo shutdown --halt 22:00

//For example, to halt the system after a five-minute delay, type:
sudo shutdown --halt +5

//You can append a message to all users by entering it after the time specification, like this:
sudo shutdown --halt +5 “Attention. The system is going down in five minutes.”

//Cancel a timed shutdown by using the -c option:
sudo shutdown -c

//However, sometimes a restart is inevitable. The option for restarting the system immediately with the shutdown command is -r, so it looks like this:
sudo shutdown -r now

//You can also use systemctl to reboot the device by typing:
sudo systemctl reboot

//You can also suspend and hibernate the system by using the systemctl command. The commands are exactly what you'd expect:
sudo systemctl suspend

sudo systemctl hibernate

sudo systemctl hybrid-sleep
