import subprocess
import time
import sys,ccxt
import os
from colorama import Style, init, Fore
init()
from exchange_config import *
sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")
print('''
                                                                                                                                                                                                                                         
                                                                                                                     ''')
print(f" \n{Fore.BLUE}{Style.BRIGHT}DEMO VERSION{Style.RESET_ALL}\n \n\nTwitter: @thebarbotine\nDiscord: https://barbotine.xyz/discord\n")
args = sys.argv
mode = args[1]
if renewal:
    balance = args[3]
    pair=args[4]
    renew=args[2]
    ex_list=args[5]
else:
    balance = args[2]
    pair=args[3]
    renew="525600"
    ex_list=args[4]
i=0
if mode!='fake-money':
    real_balance=0
    for ex_str in ex_list.split(','):
        bal = ex[ex_str].fetchBalance()
        real_balance+=float(bal[pair.split('/')[1]]['total'])
    with open(f"real_balance.txt","w") as f:
        f.write(str(real_balance))
else:
    with open(f"real_balance.txt","w") as f:
        f.write(str(balance))

while True:
    with open(f"real_balance.txt","r") as f:
        balance = str(f.read())
    if i>=1 and p.returncode==1:
        sys.exit(1)
    if mode == "fake-money":
        p=subprocess.run([python_command,"bot-fake-money.py",pair,balance,renew,pair,ex_list])
    elif mode == "real":
        p=subprocess.run([python_command,"bot.py",pair,balance,renew,pair,ex_list])
    else:
        printerror(m=f"mode input is incorrect.")
        sys.exit(1)
    i+=1
