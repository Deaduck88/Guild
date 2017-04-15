#!/usr/bin/python
#-*- coding:utf-8 -*-
# Guild tool
# Ferramenta que permite a configurção de rede em sistemas UNIX
# By: Dead Duck
# Facebook: fb.com/dead.duck01
# Twitter: @Deaduck88
# Youtube Channel: https://www.youtube.com/c/DeadDuck
import platform
import os.path
import os
import time
def menu():
	if platform.system() == "Linux":
		os.system("resize -s 70 60")
	os.system("reset")
	print "---------------------------------- "
	print ""
	print "\033[01;37m  ▄████  █    ██  ██▓ ██▓    ▓█████▄ \033[0m"
	print "\033[01;37m ██▒ ▀█▒ ██  ▓██▒▓██▒▓██▒    ▒██▀ ██▌\033[0m"
	print "\033[01;37m▒██░▄▄▄░▓██  ▒██░▒██▒▒██░    ░██   █▌\033[0m"
	print "\033[01;37m░▓█  ██▓▓▓█  ░██░░██░▒██░    ░▓█▄   ▌\033[0m"
	print "\033[01;37m░▒▓███▀▒▒▒█████▓ ░██░░██████▒░▒████▓ \033[0m"
	print "\033[01;37m ░▒   ▒ ░▒▓▒ ▒ ▒ ░▓  ░ ▒░▓  ░ ▒▒▓  ▒ \033[0m"
	print "\033[01;37m  ░   ░ ░░▒░ ░ ░  ▒ ░░ ░ ▒  ░ ░ ▒  ▒ \033[0m"
	print "\033[01;37m░ ░   ░  ░░░ ░ ░  ▒ ░  ░ ░    ░ ░  ░\033[0m" 
	print "\033[01;37m      ░    ░      ░      ░  ░   ░\033[0m"    
	print "           By: Dead Duck       \033[01;37m ░ \033[0m"  
	print ""    
	print "----------------------------------"	
def cnf():
	menu()
	print ' \033[01;37ma)\033[0m \033[01;32mConfigurar Endereço IP\033[0m'
	print " \033[01;37mb)\033[0m \033[01;32mConfigurar Gateway\033[0m"
	print " \033[01;37mc)\033[0m \033[01;32mVer as configurações de rede\033[0m"
	print " \033[01;37me)\033[0m \033[01;31mSair\033[0m"
	sh = raw_input (">> ")
	if platform.system() == "Linux":
		if sh == "a" or sh == "A":
			print menu()
			print "\033[01;37ma)\033[0m \033[01;32mMANUALMENTE\033[0m"
			print "\033[01;37mb)\033[0m \033[01;32mVIA DHCP\033[0m"
			ch = raw_input (">> ")
			if ch == "A" or ch == "a":
			# IP ESTÁTICO
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m Interface de rede: (ex: wlan0,eth0)"
				inet = raw_input (">> ")
				if inet == "wlan0" or inet == "WLAN0":
					print "=> WLAN0"
				elif inet == "eth0":
					print "=> ETH0"
				else:
					print "\033[01;37m[\033[0m\033[01;31m-\033[0m\033[01;37m]\033[0m \033[01;37m Escolha apenas entre wlan0 ou eth0"
					time.sleep(2)
					return cnf()
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m Endereço IP: (ex: 192.168.1.65)"
				ip = raw_input (">> ")
				print "=> " + str(ip)
				os.system("ifconfig " + inet + " " + ip + " 255.255.255.0")
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m Deseja configurar o servidor DNS? S(sim),N(não)"
				d = raw_input (">> ")
				if d == "S" or d == "s":
					if os.path.exists("/etc/resolv.conf"):
						os.system("echo 'nameserver 8.8.8.8' >> /etc/resolv.conf ")
				elif d == "N" or d == "n":
					os.system("reset")
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[33mConfigurado com sucesso\033[0m"
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m Agora que você configurou o seu Endereço IP, é recomendado que volte a abrir"
				print "a ferramenta e selecione a opção que permite configurar o gateway . "
				time.sleep(1)
				def o():
					print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;32mDeseja voltar para o menu principal?\033[0mS(sim)/N(não)"
					ans = raw_input (">> ")
					if ans == "s" or ans == "S":
						return cnf()
					elif ans == "n" or ans == "N":
						os.system("reset")
						quit()
					else:
						print "[-] Escolha apenas uma das opções dadas"
						return o()
				o() 
			# IP DINÂMICO	
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m A configurar ..."
				os.system("dhclient")
				print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[33mConfigurado com sucesso\033[0m"
				time.sleep(1)
				return cnf()
			# GATEWAY
		elif sh == "b" or sh == "B":
			menu()
			gw = raw_input ("\033[01;37mGATEWAY:\033[0m ")
			os.system("route add default gw " + gw)
			time.sleep(1)
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[33mConfigurado com sucesso\033[0m"
			quit()
		elif sh == "c" or sh == "C":
			if os.path.exists("/usr/bin/figlet"):
				os.system("figlet Network")
				os.system("ifconfig")
				os.system("figlet ROUTER")
				os.system("route")
				time.sleep(6)
				return cnf()
		elif sh == "e" or sh == "E":
			#\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m --> [+] ([] -> branco ; + -> verde)
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;31m5\033[0m SEGUNDOS ..."
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;37mA sair\033[0m \033[01;31m5\033[0m"
			time.sleep(1)
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;37mA sair\033[0m \033[01;31m4\033[0m"
			time.sleep(1)
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;37mA sair\033[0m \033[01;31m3\033[0m"
			time.sleep(1)
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;37mA sair\033[0m \033[01;31m2\033[0m"
			time.sleep(1)
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m \033[01;37mA sair\033[0m \033[01;31m1\033[0m"
			time.sleep(1)
			os.system("reset")
			quit()
		else:
			print "[-] Escolha somente uma das opções fornecidas"
			return cnf()
	else:
		print "[-] Desculpe este script foi criado para"
		print "suportar apenas sistemas UNIX"
		quit()
try:
	cnf()
except:
	print ""
	print "\033[01;37m[\033[0m\033[01;31m-\033[0m\033[01;37m]\033[0m \033[01;33m Terminado\033[0m"
