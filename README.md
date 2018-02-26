# Brutal_SSH
SSH brute force tool
d3vilbug# python brutal_SSH.py -h
 
 ____             _        _     ____ ____  _   _ 
| __ ) _ __ _   _| |_ __ _| |   / ___/ ___|| | | |
|  _ \| '__| | | | __/ _` | |  	\___ \___ \| |_| |
| |_) | |  | |_| | || (_| | |  	 ___) |__) |  _  |
|____/|_|   \__,_|\__\__,_|_|   |____/____/|_| |_| @d3vilbug v1.0

			
[$] python brutal_ssh.py -i Host [OPTION]

Basic Help Menu:
  -h, --help            show this help message and exit
  -i HOST_IP, --ip HOST_IP
                        Target IP Address
  -p HOST_PORT, --port HOST_PORT
                        Target Port Number (Default 22)
  -u USER, --user USER  SSH User name (Default root)
  -U USERSFILE, --usersfile USERSFILE
                        Usernames File Path
  -P PASSWORDSFILE, --passowrdsfile PASSWORDSFILE
                        Passwords File Path
  -t THREADS, --threads THREADS
                        No of threads (Default 4)
  -T TIMEOUT, --timeout TIMEOUT
                        Request timeout (Default 5)
