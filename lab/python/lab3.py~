# -*- coding: latin-1 -*-

#IS-105 LAB3

import sys
import os
import subprocess
import re

#gruppe = { 'student1': 'Tor Arne Bang', \
#	'student2': 'Simen stromland', \
#}

#Oppgave 1 | Kaller inn 3 andre script og returnerer dem
def lab3_scripts():
    subprocess.call(["../scripts/test1.sh"])
    subprocess.call(["../scripts/test1.pl"])
    subprocess.call(["../scripts/test1.py"])

#Oppgave 2 | skriver ut systeminformasjon til pcen den kjøres på.
def min_sys_info():
    """
    Her er mitt resultat av kjøringen av denne funksjonen:
	byteorder: little
	os data: 
	('Linux', 'localhost.localdomain', '2.6.32-431.3.1.el6.i686', '#1 	  SMP Fri Jan 3 18:53:30 UTC 2014', 'i686')
	os brukere: centos

    """
    print "byteorder: " + sys.byteorder
    print "os data: "
    print os.uname()
    print "os brukere: " + os.getlogin()

#Oppgave 3 |
def initialer(navn):
    fornavn = navn[0]
    m = navn.find (" ")
    etternavn = navn[m + 1] 
    fulltnavn = fornavn + "." + etternavn + "."
    print fulltnavn

#Oppgave 4 |
def infix_to_prefix(infix):
    regexp1 = r"[0-9]+" #finner tall  
    regexp2 = r"[*+-/]+"# finner +-*/
    operands = re.findall(regexp1, infix) # [2, 3]
    operator = re.findall(regexp2, infix) # [+]
    mongo = operator + operands
    result = ' '.join(mongo)
    print result


lab3_scripts()
min_sys_info()
initialer("Tor Arne")
infix_to_prefix("2+3")
