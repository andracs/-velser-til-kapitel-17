sudo killall -9 nc
sudo systemctl stop httpd
sudo systemctl stop mariadb
sudo systemctl stop vsftpd
ps aux | egrep 'nc|httpd|mariadb|vsftpd'
