#!/bin/bash
LOG_FILE_PATH="/home/raspberrylex/Documents/project_logs/cron.log"

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/snap/bin
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus

echo "Current Date and Time: $(date)" >> "$LOG_FILE_PATH"

if nmcli -t -f DEVICE,STATE dev | grep -q "wifi:connected"; then
	echo "$(date) Wi-Fi connection is live." >>  "$LOG_FILE_PATH"
else
	echo "$(date) Wi-Fi is not connected. Attempting to reconnect..." >> "$LOG_FILE_PATH"
	
	nmcli dev wifi connect "WiFiNAME" password "PASSWORD"
	
	if [ $? -eq 0 ]; then
		echo "$(date) Successfully connected to Wi-Fi." "$LOG_FILE_PATH"
	else
		echo "$(date) Failed to connect to Wi-Fi." >> "$LOG_FILE_PATH"
	fi
fi
