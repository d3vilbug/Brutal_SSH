# Brutal_SSH
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![python](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/)
[![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=1.0&x2=0)](http://badge.fury.io/gh/boennemann%2Fbadges)

**Brutal SSH -> SSH Login brute force, scan for vulnerable version and 0 day exploit**

<img src="https://i.imgur.com/DoIksgM.png" />

#### Output

<img src="https://i.imgur.com/GcIBpFZ.png" />

<img src="https://i.imgur.com/VF7C9bp.png" />

### Requirements

- Python (2.7.*)
- Python `pip`
- Python module `colorama`
- Python module `argparse`
- Python module `paramiko`
- Python module `threading`
- Python module `logging`

### Install modules

	pip install -r requirements.txt

### Tested on

- Kali linux

### Download Brutal_SSH

	git clone https://github.com/d3vilbug/Brutal_SSH


### Usage

	python brutal_SSH.py -h

***Brute force password of single user***
	
	python brutal_SSH.py -i 192.168.7.128 -u msfadmin -P wordlist/passfile.txt

***Brute force user and password***
	
	python brutal_SSH.py -i 192.168.7.128 -U wordlist/userfile.txt -P wordlist/passfile.txt

