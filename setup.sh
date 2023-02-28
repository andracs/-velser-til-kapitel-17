sudo systemctl start httpd
sudo systemctl start mariadb
sudo systemctl start vsftpd
#echo "Zealand Yellow hat service" | sudo nc -nlvk -e './banner.sh' 172.31.4.42 21 &
echo "Magic Server" | sudo nc -nlvk -e './banner.sh' 172.31.4.42 25 &
echo "Noobserver" | sudo nc -nlvk -e './banner.sh' 172.31.4.42 180 &
echo "Flagserver" | sudo nc -nlvk -e './banner.sh' 172.31.4.42 1781 &
echo "Du har fundet jackpot" | sudo nc -nlvk -e './banner.sh' 172.31.4.42 8788 &
ps aux | egrep 'nc|httpd|mariadb|vsftpd'
