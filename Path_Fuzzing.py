import requests
import sys 
from colorama import Fore, Style

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def Path_Fuzzing(target,url_paths) :
    print( Fore.BLUE +"[+] Fuzzing Path..."+Style.RESET_ALL)
    for url_path in url_paths :
        url_path = url_path.strip()
        before,after = url_path.split("admin",1) 
        url = target
        url1 = target
        if target.count('/') == 2:
            if len(after)== 0 or after[0] != "/":
                continue
            else :
                try :
                    url = url + after
                    response = requests.get(url,timeout=5,headers=user_agent)
                    content_length = len(response.text)
                    if response.status_code == 200 :
                        print(f"{Fore.GREEN}[ {response.status_code} ]   {url} | length : [ {content_length} ]{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}Access this URL : {url} using curl {Style.RESET_ALL}")
                    else : 
                        if '-v' not in sys.argv :
                            print(f"{Fore.RED}[ {response.status_code} ]   {url} | length : [ {content_length} ]{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{e} {url_path}")

        else :
            try :
                url = url[:url.rfind('/')+1]+before+url[url.rfind('/')+1:]+after
                url1 = url1[:url1.rfind('/')+1]+before+url1[url1.rfind('/')+1:].upper()+after
                response = requests.get(url,timeout=5,headers=user_agent)
                response2= requests.get(url1,timeout=5,headers=user_agent)
                content_length = len(response.text)
                content_length2 = len(response2.text)
                if response.status_code == 200 or response2.status_code == 200:
                    if response.status_code == 200:
                        print(f"{Fore.GREEN}[ {response.status_code} ]   {url} | length : [ {content_length} ] {Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}Access this URL : {url} using curl {Style.RESET_ALL}")
                    if response2.status_code == 200: 
                        print(f"{Fore.GREEN}[ {response2.status_code} ]   {url1} | length : [ {content_length2} ]{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}Access this URL : {url1} using curl {Style.RESET_ALL}")
                else : 
                    if '-v' not in sys.argv :
                        print(Fore.RED,end="")
                        print(f"[ {response.status_code} ]   {url} | length : [ {content_length} ]")
                        print(f"[ {response2.status_code} ]   {url1} | length : [ {content_length2} ]")
                        print(Style.RESET_ALL,end="")
            except Exception as e:
                print(f"{e} {url_path}")


def Other_URL_Fuzzings(target):
    url1 = "https://"+target[target.index("/")+2:]
    url2 = "http://"+target[target.index("/")+2:]
    response = requests.get(url1,headers=user_agent)
    content_length = len(response.text)
    if response.status_code == 200 : print(f"{Fore.GREEN}[ {response.status_code} ]   {url1} | length : [ {content_length} ]{Style.RESET_ALL}")
    else : print(f"{Fore.RED}[ {response.status_code} ]   {url1} | length : [ {content_length} ]{Style.RESET_ALL}")
    response = requests.get(url2,headers=user_agent)
    content_length = len(response.text)
    if response.status_code == 200 : print(f"{Fore.GREEN}[ {response.status_code} ]   {url2} | length : [ {content_length} ]{Style.RESET_ALL}")
    else : print(f"{Fore.RED}[ {response.status_code} ]   {url2} | length : [ {content_length} ]{Style.RESET_ALL}")
