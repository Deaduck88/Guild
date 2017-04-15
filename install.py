#!/usr/bin/python
#-*- coding:utf-8 -*-
import os.path
import os
import platform
def mn():
	print "\033[01;35m╦┌┐┌┌─┐┌┬┐┌─┐┬  ┬    ╔╦╗╔╦╗\033[0m"
	print "\033[01;35m║│││└─┐ │ ├─┤│  │     ║║ ║║\033[0m"
	print "\033[01;35m╩┘└┘└─┘ ┴ ┴ ┴┴─┘┴─┘  ═╩╝═╩╝\033[0m"
	print "                   \033[01;37mDead Duck\033[0m "
	print ""
def ins():
	mn()
	if os.path.basename(os.getcwd()) == 'Guild':
		if os.path.exists('/usr/bin'):
			os.system("cp guild.py /usr/bin")
			if os.path.exists('/usr/bin/guild'):
				os.rename('/usr/bin/guild.py','guild')
				os.system("chmod 777 /usr/bin/guild")
			print "100% feito"
			print "\033[01;37m[\033[0m\033[01;32m+\033[0m\033[01;37m]\033[0m Instalado com sucesso"
		else:
			print "\033[01;37m[\033[0m\033[01;31m-\033[0m\033[01;37m]\033[0m Directório \033[01;38m/usr/bin\033[01;0m não existe"
			quit()
try:
	if platform.system() == "Linux":
		ins()
except:
	print ""