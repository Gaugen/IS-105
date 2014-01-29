#IS-105 LAB2
import sys
#Gruppemedlemmene 
#gruppe = { 'student1': 'Tor Arne Bang', \
#	'student2': 'Simen Stromland', \
#}

#Oppgave 1 | Printer ut fugl naar man kalle fuksjon.
def ascii_fugl():
    print """ 
                  \/_ 
             \,   /( ,/
              \\\' ///
               \_ /_/
               (./
                '`
    """
#oppgave 2 | Finner bitAnd av x og y
def bitAnd(x, y):
    return x&y
#Oppgave 4 | Finner bitXor av x og y
def bitXor (x, y):
    return x^y
#Oppgave 5 | Finner bitOr av x og y
def bitOr (x, y):
    return x|y
#Oppgave 6 | Finner bitkodent til bokstaven 
def ascii8Bin(x):
    print '{0:08b}'.format(ord (x))
   
#Oppgave 7 |  finner bitkoden til tekststreng
def transferBin(x):
    l = list(x)
    for c in l:
        ascii8Bin(c)
#Oppgaver 8 | gjor om desimalverdien av bokstaver om til et tall, tar saa aa #finner bitverdien til det tallet 
def asciiHexBin (x):
    print '{0:08x}'.format(ord (x))
#Oppgave 8 | Finner hexaverdien til tekst stringen.
def transferHex(x):
    l = list(x)
    for c in l:
	asciiHexBin(c)
# svar
print transferBin ('Tulling')
print transferHex ('Hi')
