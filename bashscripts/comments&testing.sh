# file management
chmod scope +ACTION script_file.sh
chown newuser script_file.sh

# hosts files are located in etc/hosts 

# processes
kill PID
ps, top 
cat proc/PID/status # -> Where process are stored


# compression and decompression
tar cf output_file.tar file1 file 2
tar xf output_file.tar file1 file 2

# pckt management  
# low level pckt management, robin
dpkg for ubuntu/debian distros &  rpm for RedHat
dpkg -i some_packages.deb      &  rpm -i some_packages.rpm     # ->  install 
dpkg -r some_packages.deb      &  rpm -e some_packages.rpm     # -> remove/erase
dpkg -l                        &  rpm -qa                      # -> list

# high level pckt management, batman
apt for ubuntu/debian distros &   yum for RedHat
apt install some_package      &   yum install some_package     # -> install
apt remove some_package       &   yum erase some_package       # -> remove/erase
apt update/upgrade            &   yum update                   # -> update package repositories
apt show some_package         &   yum info some_package        # -> list