# -*- coding: latin-1 -*-

#  IS-105 LAB4

import sys
import os
import subprocess
import re
import psutil # Kan installeres med "pip2.7 install psutil"

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
#gruppe = {  'student1': 'Tor Arne Bang', \
#			'student2': 'Simen Strømland', \
#}

# Oppgave 1
# 	Funksjonen lager en strukturert utskrift av resultater fra
#   kallet psutil.cpu_times(). 
#	Modulen psutil må være installert.
#
#   Utskriften skal være følgende (verdiene skal selvsagt være forskjellige):
#		user = 3088.16
#		nice = 0.99
#		system = 897.37
#		idle = 72353.81
#		iowait = 19.29
#		irq = 6.82
#		softirq = 3.07
#		steal = 0.00
#		guest = 0.00
#
def psutils_use():	
    name = psutil.cpu_times()._fields
    value = tuple(psutil.cpu_times())
    psutils = zip( name, value)
    for name, value in psutils:
	print name, " = ", value
psutils_use()


"cputimes(user=25.71, nice=0.0, system=109.07, idle=969.55, iowait=77.03, irq=9.25, softirq=2.76, steal=0.0, guest=0.0)"



# Oppgave 2
#	Gitt følgende liste (inn-data):
# 	proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
#
#	skal funksjonen produsere følgende ut-data:
#
#		C ble startet 1969 av Dennis Ritchie.
#		C++ ble startet 1979 av Bjarne Stroustrup.
#		Perl ble startet 1987 av Larry Wall.
#		Python ble startet 1989 av Guido van Rossum.
#		Java/Oak ble startet 1991 av James Gosling.
#		Ruby ble startet 1991 av Yukihiro "Matz" Matsumoto.
#		Go/golang ble startet 2007 av Robert Griesemer, Rob Pike, and Ken Thompson.
#		
def print_history(proglangs):
    tupled = tuple(proglangs)
    sortert = sorted(tupled, key=lambda year: year[1]) #sort by year
    setning = [lang + " ble startet " + year + " av " + name + " . "
    for lang, year, name in sortert]
    for c in setning:
	print c
    
proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')] 

    
print_history(proglangs)

