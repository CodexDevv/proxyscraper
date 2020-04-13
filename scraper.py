#CODED BY STEFAN20
#CODED BY STEFAN20
#CODED BY STEFAN20

import requests
import os

os.system("title Proxy Scraper by Stefan20")

titlu = """
    ____  ____  ____ _  ____  __   _____ __________  ___    ____  ____________ 
   / __ \/ __ \/ __ \ |/ /\ \/ /  / ___// ____/ __ \/   |  / __ \/ ____/ __  /
  / /_/ / /_/ / / / /   /  \  /   \__ \/ /   / /_/ / /| | / /_/ / __/ / /_/ /
 / ____/ _, _/ /_/ /   |   / /   ___/ / /___/ _, _/ ___ |/ ____/ /___/ _, _/ 
/_/   /_/ |_|\____/_/|_|  /_/   /____/\____/_/ |_/_/  |_/_/   /_____/_/ |_| 
"""

author = """
      _____        __        _   ______      ___          ___  _____
     / ___/__  ___/ /__ ____(_) / __/ /____ / _/__ ____  |_  |/ _  /
    / /__/ _ \/ _  / -_) __/   _\ \/ __/ -_) _/ _ `/ _ \/ __// // /
    \___/\___/\_,_/\__/_/ (_) /___/\__/\__/_/ \_,_/_//_/____/\___/ 
"""

print(titlu)
print(author)
print("What proxies do you want to scrape?")
print("[1] ALL TYPES")
print("[2] HTTPS/HTTP")
print("[3] SOCKS4")
print("[4] SOCKS5")
print("CODED BY Stefan20")
print()
inp = input("INPUT: ")
print()

if inp == '1':
    alltypes = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=all&timeout=10000&country=all&ssl=all&anonymity=all%22")
    with open('all_proxies.txt', 'wb') as f:
        f.write(alltypes.content)
    print("Proxies saved!")
    f.close()
elif inp == '2':
    httpstype = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all")
    with open('http_proxies.txt', 'wb') as g:
        g.write(httpstype.content)
    print("Proxies saved!")
    g.close()
elif inp == '3':
    sockspatrutype = requests.get("https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
    with open('socks4_proxies.txt', 'wb') as h:
        h.write(sockspatrutype.content)
    print("Proxies saved!")
    h.close()
elif inp == '4':
    sockscincitype = requests.get("https://api.proxyscrape.com/?request=getprox&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
    with open('socks5_proxies.txt', 'wb') as i:
        i.write(sockscincitype.content)
    print("Proxies saved!")
    i.close()
else:
    print("Invalid Input!")

print()
toexit = input("PRESS ANY KEY TO EXIT...")

#CODED BY STEFAN20
#CODED BY STEFAN20
#CODED BY STEFAN20