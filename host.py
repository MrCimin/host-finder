import json, socket, sys, os
from time import sleep

try:
  import requests
except ImportError:
  os.system('pip install requests')
  os.system('python subdomain.py')

banner = """

\033[1;33m          /\        
\033[1;33m          \\ \       
\033[1;33m         \ \\ /      
\033[1;33m        / \/ / /     
\033[1;33m       / /   \//\    
\033[1;33m       \//\   / /    \033[1;32m[\033[1;30m#\033[1;32m] \033[1;31mSubdomain \033[1;37mFinder \033[1;32m[\033[1;30m#\033[1;32m]
\033[1;33m        / / /\ /     
\033[1;33m         / \\ \      
\033[1;33m          \ \\       
\033[1;33m           \/        

"""

'''
 Author : MrCimin
 Github : https://github.com/MrCimin
 Instagram : https://instagram.com/z3r0_ID
 Facebook : https://www.facebook.com/Davit.ex.1238
 =================================================
 Thanks To : Indoxploit
'''

os.system('clear')
print(banner)
if len(sys.argv) < 2:
  print(f'\033[1;37m-\033[0;35mUsage \033[1;37m: \033[1;36mpython {sys.argv[0]} <hostname>\n         python {sys.argv[0]} ruangguru.com\n')
  
else:
  mrA = 'https://api.indoxploit.or.id/domain/'
  mrB = sys.argv[1]
  mrC = requests.get(mrA+mrB)
  mrD = json.loads(mrC.text)
  mrE = 0
  
  for i in "\|/-\|/-\|/-":
    print('\r\033[1;32m[\033[1;36m?\033[1;32m] \033[1;34mSearching \033[1;31m['+i+'\033[1;31m] ',end="",flush=True)
    sleep(0.5)
  os.system('clear')
  print(banner)
  print('\033[1;37m[\033[1;31m!\033[1;37m] \033[1;32mFound')
  sleep(0.7)
  os.system('clear')
  print(banner)
  try:
    for i in mrD["data"]["subdomains"]:
      mrE +=1
      try:
        mrF = socket.gethostbyname(i)
        print(f'\033[1;37m{str(mrE)}}} \033[1;34m{str(i)} \033[1;33m{str(mrF)}')
      except socket.gaierror:
        print(f'\033[1;37m{str(mrE)}}} \033[1;31m{str(i)}')
        
  except TypeError:
    try:
      mrF = socket.gethostnameby(mrB)
      print(f'\033[1;37m1}} \033[1;34m{str(mrB)} \033[1;32m{str(mrF)}\n')
    except socket.gaierror:
      print(f'\033[1;37m1}} \033[1;36m{str(mrB)}')
