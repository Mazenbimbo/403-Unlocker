from colorama import Fore, Style
import requests 
import sys 

def UserAgent_Fuzzing(target,user_agents) :
    print( "\033[34m" +"[+] Fuzzing User-Agent...\nThis one may take 5 to 10 mins !"+"\033[0m")
    for user_agent in user_agents :
        user_agent = user_agent.strip() 
        try :
            response = requests.get(target,headers={'User-Agent': user_agent})
            content_length = len(response.text)
            if response.status_code == 200 :
                print(f"{Fore.GREEN}[ {response.status_code} ]    User-Agent: {user_agent} | length : [ {content_length} ]{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Intercept the request from this URL : {target} in Burp or OWASPzap and add this header : User-Agent: {user_agent}{Style.RESET_ALL}")
            else :
                if '-v' not in sys.argv :
                    print(f"{Fore.RED}[ {response.status_code} ]    User-Agent: {user_agent} | length : [ {content_length} ]{Style.RESET_ALL}")
        except Exception as e:
            print(f"{e} {user_agent}")