from colorama import Fore, Style
import requests 
import sys 

def Method_Fuzzing(target,methods,response_headers) : 
    print( Fore.BLUE +"[+] Trying Overriding HTTP Method..."+Style.RESET_ALL)
    for method in methods :
        try:
            response = requests.get(target,headers={"X-HTTP-Method-Override": method,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
            content_length = len(response.text)
            for headerr, value in response.headers.items() :
                if headerr not in response_headers : 
                    response_headers[headerr] = value
            if response.status_code == 200 :
                print(f"{Fore.GREEN}[ {response.status_code} ]    X-HTTP-Method-Override: {method} | length : [ {content_length} ]{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Intercept the request from this URL : {target} in Burp or OWASPzap and add this header : X-HTTP-Method-Override: {method}{Style.RESET_ALL}")
            else :
                if '-v' not in sys.argv :
                    print(f"{Fore.RED}[ {response.status_code} ]    X-HTTP-Method-Override: {method} | length : [ {content_length} ]{Style.RESET_ALL}")
        except Exception as e:
            print(f"{e} {method}")
    # Printing The Collected Headers Above
    print(Fore.YELLOW + "\n[*] Look for any useful headers here : "+Style.RESET_ALL)
    print(response_headers)