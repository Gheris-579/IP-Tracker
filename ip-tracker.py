import requests
import json
import sys
import time
from colorama import init, Fore
import os

try:
    os.system('cls')
except:
    os.system('clear')


#colors
init()
GREEN = Fore.GREEN
RED = Fore.RED
LIGHT = Fore.LIGHTBLUE_EX

left = ">>"*50
rigth = "<<"*50


print(f"""\n{LIGHT}{left}
        ██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
        ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
        ██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
        ██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
        ██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
        ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                 
{rigth}""")


def progres_bar(part, total, length=30):
    frac = part / total
    completed = int(frac * length)
    missing = length - completed
    bar = f"{'#'* completed}{'-'* missing}{frac: .2%}"
    return bar

n = 30

print(f"""
{GREEN}
{left}
                Instgram: gheris__579_
                Github: Gheris-579
    
1: START
99: Exit
{rigth} 
""")


exit = int(input(f"{GREEN}[:]>> "))

# LINK OF IP-API
url = "http://ip-api.com/json/"

def main():
    try:
        ip = input("\nEnter the public IP : ")

        req = requests.get(url+ip)

        data = req.text

        value = json.loads(data)

        if value['status'] == "success":
            print("\n")
            for i in range(n + 1):
                time.sleep(0.1)
                print(progres_bar(i, n, 50), end="\r")
            print("\n")
            print(f"""
                IP :   {value['query']}
                ISP :   {value['isp']}
                Country : {value['country']}
                County code :   {value['countryCode']}
                Region :   {value['region']}
                City :    {value['city']}
                Region Name :    {value['regionName']}
                AS :    {str(value['as'])}
                Time Zone :    {value["timezone"]}
                Latitude :     {str(value['lat'])}
                Longitude :   {str(value['lon'])}
                
            """)
        else:
            print("The IP address is a bogon IP. No data for this IP address.")
    except:
        print("Make sure you have internet connection")


if __name__ == "__main__":
    if exit == 1:
        main()
    elif exit == 99:
        print("Thank you for using :)")
        sys.exit()