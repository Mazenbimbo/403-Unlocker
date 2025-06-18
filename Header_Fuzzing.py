import requests
import sys 
from colorama import Fore, Style
import socket


def Headers_Fuzzing(target,Headers,raw_headers,response_headers) :
    print( Fore.BLUE +"[+] Fuzzing Headers..."+Style.RESET_ALL)
    for header in Headers :
        try:
            headers_dict = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            header = header.strip()
            key, value = header.split(": ",1)
            headers_dict[key] = value
            response = requests.get(target,headers=headers_dict)
            content_length = len(response.text)
            for headerr, value in response.headers.items() :
                if headerr not in response_headers or value not in response_headers: 
                    response_headers[headerr] = value
            if response.status_code == 200 :
                print(f"{Fore.GREEN}[ {response.status_code} ]    {header} | length : [ {content_length} ]{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Intercept the request from this URL : {target} in Burp or OWASPzap and add this header : {header}{Style.RESET_ALL}")
            else :
                if '-v' not in sys.argv : 
                    print(f"{Fore.RED}[ {response.status_code} ]    {header} | length : [ {content_length} ]{Style.RESET_ALL}")
        except Exception as e:
            print(f"{e} {header}")

    # Fuzzing Headers Part 2
    for header in raw_headers :
        try:
            domain = target[target.index("/")+2:target.index("com")+3]
            ip_address = socket.gethostbyname(domain)
            headerr = { header.strip() : ip_address }
            response = requests.get(target,headers=headerr)
            content_length = len(response.text)
            if response.status_code == 200 :
                print(f"{Fore.GREEN}[ {response.status_code} ]    {header.strip()}: {ip_address} | length : [ {content_length} ]{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Intercept the request from this URL : {target} in Burp or OWASPzap and add this header : {header}:{ip_address}{Style.RESET_ALL}")
            else :
                if '-v' not in sys.argv : 
                    print(f"{Fore.RED}[ {response.status_code} ]    {header.strip()}: {ip_address} | length : [ {content_length} ]{Style.RESET_ALL}")
        except socket.gaierror:
            print(f"Could not resolve the domain: {domain}")
