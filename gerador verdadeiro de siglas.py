import json
import logging
import random
import time
from colorama import Fore
while True:
 print(Fore.LIGHTBLUE_EX+"════════════════════════════")
 print(Fore.LIGHTBLUE_EX+"║                          ║")
 print(Fore.LIGHTBLUE_EX+"║                          ║")
 colund=Fore.LIGHTBLUE_EX+"║"
 TIT= Fore.LIGHTWHITE_EX+"           LOOK           "
 colune=Fore.LIGHTBLUE_EX+"║"
 print(f"{colund}{TIT}{colune}")
 print(Fore.LIGHTBLUE_EX+"║                          ║")
 print(Fore.LIGHTBLUE_EX+"║                          ║")
 print(Fore.LIGHTBLUE_EX+"════════════════════════════")
 print(Fore.LIGHTBLACK_EX+"════════════════════════════")
 idade=int(input(Fore.LIGHTWHITE_EX+"Escreva sua idade: "))
 if idade>=1 and idade<18:
  print(Fore.RED + "══════════════════════════════")
  print(Fore.RED + "║                            ║")
  print(Fore.RED + "║                            ║")
  s = Fore.RED + "║"
  sa = Fore.LIGHTRED_EX + "         ÉS MENOR!!!"
  SA = Fore.RED + "        ║"
  print(f"{s}{sa}{SA}")
  s2 = Fore.RED + "║"
  sa2 = Fore.LIGHTRED_EX + "         A SAIR..."
  SA2 = Fore.RED + "          ║"
  time.sleep(0.5)
  print(f"{s2}{sa2}{SA2}")
  print(Fore.RED + "║                            ║")
  print(Fore.RED + "║                            ║")
  print(Fore.RED + "══════════════════════════════")
  break
 elif idade>=18 and idade<=116:
  nome = input(Fore.LIGHTWHITE_EX + "Escreva o seu nome completo: ")
  v = len(nome)
  if v < 1:
   print(Fore.RED + "═══════════════════════════════")
   print(Fore.RED + "║                            ║")
   print(Fore.RED + "║                            ║")
   s2233 = Fore.RED + "║"
   sa2233 = Fore.LIGHTRED_EX + "      NOME INVÁLIDO!!!"
   SA2233 = Fore.RED + "      ║"
   print(f"{s2233}{sa2233}{SA2233}")
   print(Fore.RED + "║                            ║")
   print(Fore.RED + "║                            ║")
   print(Fore.RED + "═══════════════════════════════")
  elif v >= 1 and v <= 2253:
 else:
print(Fore.RED + "═══════════════════════════════")
     print(Fore.RED + "║                            ║")
     print(Fore.RED + "║                            ║")
  s22333 = Fore.RED + "'"
  sa22333 = Fore.LIGHTRED_EX + "      IDADE IMPOSSÍVEL!!!"
  SA22333 = Fore.RED + "      '"
  print(f"{s22333}{sa22333}{SA22333}")
  print(Fore.RED + "║                            ║")
  print(Fore.RED + "║                            ║")
  print(Fore.RED + "═══════════════════════════════")
