#! /bin/python3

from colorama import Fore, Style
import pyfiglet
import requests 
import sys 
import subprocess 
import socket

Headers = open("Headers_with_values.txt","r")
raw_headers = open("raw_headers.txt","r")
user_agents = open("user-agents_enum.txt","r")
url_paths = open("url_fuzzing.txt","r")
target = sys.argv[1]
if target[len(target)-1] == '/' : 
        target = target[:len(target)-1]
methods = ["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH","INVENTED","HACK"]
HTTP_versions = ["1.0","1.1","2","3"]
response_headers = {}
encoding = {
    'a': '%61', 'b': '%62', 'c': '%63', 'd': '%64', 'e': '%65',
    'f': '%66', 'g': '%67', 'h': '%68', 'i': '%69', 'j': '%6a',
    'k': '%6b', 'l': '%6c', 'm': '%6d', 'n': '%6e', 'o': '%6f',
    'p': '%70', 'q': '%71', 'r': '%72', 's': '%73', 't': '%74',
    'u': '%75', 'v': '%76', 'w': '%77', 'x': '%78', 'y': '%79',
    'z': '%7a', 'A': '%41', 'B': '%42', 'C': '%43', 'D': '%44',
    'E': '%45', 'F': '%46', 'G': '%47', 'H': '%48', 'I': '%49',
    'J': '%4a', 'K': '%4b', 'L': '%4c', 'M': '%4d', 'N': '%4e',
    'O': '%4f', 'P': '%50', 'Q': '%51', 'R': '%52', 'S': '%53',
    'T': '%54', 'U': '%55', 'V': '%56', 'W': '%57', 'X': '%58',
    'Y': '%59', 'Z': '%5a'
}
double_encoding = {
    'a': '%2561', 'b': '%2562', 'c': '%2563', 'd': '%2564', 'e': '%2565',
    'f': '%2566', 'g': '%2567', 'h': '%2568', 'i': '%2569', 'j': '%256a',
    'k': '%256b', 'l': '%256c', 'm': '%256d', 'n': '%256e', 'o': '%256f',
    'p': '%2570', 'q': '%2571', 'r': '%2572', 's': '%2573', 't': '%2574',
    'u': '%2575', 'v': '%2576', 'w': '%2577', 'x': '%2578', 'y': '%2579',
    'z': '%257a', 'A': '%2541', 'B': '%2542', 'C': '%2543', 'D': '%2544',
    'E': '%2545', 'F': '%2546', 'G': '%2547', 'H': '%2548', 'I': '%2549',
    'J': '%254a', 'K': '%254b', 'L': '%254c', 'M': '%254d', 'N': '%254e',
    'O': '%254f', 'P': '%2550', 'Q': '%2551', 'R': '%2552', 'S': '%2553',
    'T': '%2554', 'U': '%2555', 'V': '%2556', 'W': '%2557', 'X': '%2558',
    'Y': '%2559', 'Z': '%255a'
}

# Banner
banner = pyfiglet.figlet_format("403-Unlocker",font="slant")
print(Fore.CYAN+'-'*50)
print(banner)
print(" "*10 + "By @Mazen_Mohammed")
print('-'*50+Style.RESET_ALL)

if "http" not in target :
    print("Please specify the http protocol type in the URL, ex : https://...")
    sys.exit()

# Fuzzing Headers
def Headers_Fuzzing() :
    print( Fore.BLUE +"[+] Fuzzing Headers..."+Style.RESET_ALL)
    for header in Headers :
        try:
            headers_dict = {}
            header = header.strip()
            key, value = header.split(": ",1)
            headers_dict[key] = value
            response = requests.get(target,headers=headers_dict)
            content_length = response.headers.get("Content-Length")
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
            content_length = response.headers.get("Content-Length")
            if response.status_code == 200 :
                print(f"{Fore.GREEN}[ {response.status_code} ]    {header.strip()}: {ip_address} | length : [ {content_length} ]{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Intercept the request from this URL : {target} in Burp or OWASPzap and add this header : {header}:{ip_address}{Style.RESET_ALL}")
            else :
                if '-v' not in sys.argv : 
                    print(f"{Fore.RED}[ {response.status_code} ]    {header.strip()}: {ip_address} | length : [ {content_length} ]{Style.RESET_ALL}")
        except socket.gaierror:
            print(f"Could not resolve the domain: {domain}")

# Overriding HTTP Method Uing Header
def Method_Fuzzing() : 
    print( Fore.BLUE +"[+] Trying Overriding HTTP Method..."+Style.RESET_ALL)
    for method in methods :
        try:
            response = requests.get(target,headers={'X-HTTP-Method-Override': method})
            content_length = response.headers.get("Content-Length")
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

# Fuzzing User-Agent
def UserAgent_Fuzzing() :
    print( "\033[34m" +"[+] Fuzzing User-Agent...\nThis one may take 5 to 10 mins !"+"\033[0m")
    for user_agent in user_agents :
        user_agent = user_agent.strip() 
        try :
            response = requests.get(target,headers={'User-Agent': user_agent})
            content_length = response.headers.get("Content-Length")
            if response.status_code == 200 :
                print(f"{Fore.GREEN}[ {response.status_code} ]    User-Agent: {user_agent} | length : [ {content_length} ]{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Intercept the request from this URL : {target} in Burp or OWASPzap and add this header : User-Agent: {user_agent}{Style.RESET_ALL}")
            else :
                if '-v' not in sys.argv :
                    print(f"{Fore.RED}[ {response.status_code} ]    User-Agent: {user_agent} | length : [ {content_length} ]{Style.RESET_ALL}")
        except Exception as e:
            print(f"{e} {user_agent}")

# Path Fuzzing 
def Path_Fuzzing() :
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
                    response = requests.get(url,timeout=5)
                    content_length = response.headers.get("Content-Length")
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
                response = requests.get(url,timeout=5)
                response2= requests.get(url1,timeout=5)
                content_length = response.headers.get("Content-Length")
                content_length2 = response2.headers.get("Content-Length")
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

def Compound_Commands(target) :
    print( Fore.BLUE +"[+] Trying Compound Commands..."+Style.RESET_ALL)
    url = target
    url2 = target
    # https://google.org/file.txt
    if target.count('/') > 2 :
        file = target[target.rfind('/')+1:] 
        if file[0] in encoding :
            new_file = file.replace(file[0],encoding[file[0]])
            new_file2 = file.replace(file[0],double_encoding[file[0]])
            url = target[:target.rfind('/')+1]+new_file
            url2 = target[:target.rfind('/')+1]+new_file2
    for method in methods :
        for version in HTTP_versions :
            curl_output = subprocess.run(["curl","-v","-i","-X",method,f"--http{version}", url],capture_output=True,text=True)
            curl_output2 = subprocess.run(["curl","-v","-i","-X",method,f"--http{version}", url2],capture_output=True,text=True)
            curl_output3 = subprocess.run(["curl","-v","-i","-X",method,f"--http{version}","-H",f"Referer: {url}",url],capture_output=True,text=True)
            try  :
                status_code = curl_output.stdout[curl_output.stdout.find(" ")+1:curl_output.stdout.find(" ")+4]
                status_code1 = curl_output2.stdout[curl_output2.stdout.find(" ")+1:curl_output2.stdout.find(" ")+4]
                status_code2 = curl_output3.stdout[curl_output3.stdout.find(" ")+1:curl_output3.stdout.find(" ")+4]
                if status_code == "200" :
                    print(f"{Fore.GREEN}[ 200 ]    curl -v -i -X {method} --http{version} {url}{Style.RESET_ALL}")
                else :
                    if '-v' not in sys.argv :
                        print(f"{Fore.RED}[ {status_code} ]    curl -v -i -X {method} --http{version} {url}{Style.RESET_ALL}")
                if status_code1 == "200" :
                    print(f"{Fore.GREEN}[ 200 ]    curl -v -i -X {method} --http{version} {url2}{Style.RESET_ALL}")
                else :
                    if '-v' not in sys.argv :
                        print(f"{Fore.RED}[ {status_code1} ]    curl -v -i -X {method} --http{version} {url}{Style.RESET_ALL}")
                if status_code2 == "200" :
                    print(f"{Fore.GREEN}[ 200 ]    curl -v -i -X {method} --http{version} -H 'Referer:{url}' {url}{Style.RESET_ALL}")
                else :
                    if '-v' not in sys.argv :
                        print(f"{Fore.RED}[ {status_code2} ]    curl -v -i -X {method} --http{version} {url}{Style.RESET_ALL}")
            except Exception as e:
                print(e) 

def Other_URL_Fuzzings():
    url1 = "https://"+target[target.index("/")+2:]
    url2 = "http://"+target[target.index("/")+2:]
    response = requests.get(url1)
    content_length = response.headers.get("Content-Length")
    if response.status_code == 200 : print(f"{Fore.GREEN}[ {response.status_code} ]   {url1} | length : [ {content_length} ]{Style.RESET_ALL}")
    else : print(f"{Fore.RED}[ {response.status_code} ]   {url1} | length : [ {content_length} ]{Style.RESET_ALL}")
    response = requests.get(url2)
    content_length = response.headers.get("Content-Length")
    if response.status_code == 200 : print(f"{Fore.GREEN}[ {response.status_code} ]   {url2} | length : [ {content_length} ]{Style.RESET_ALL}")
    else : print(f"{Fore.RED}[ {response.status_code} ]   {url2} | length : [ {content_length} ]{Style.RESET_ALL}")

# Printing Help Menu
def Print_Help_Menu() : 
    print(" Usage : $ ./403_Unlocker.py [URL] [Options]\n")
    print("Options :")
    print(" -v     -->   To Not Show The Testing Progress ")
    print(" -c     -->   For Compound Commands (( This one uses multiple techniques together ))")
    print(" -p     -->   For Path Fuzzing ")
    print(" -h     -->   For Headers Fuzzing ")
    print(" -u     -->   For UserAgent Fuzzing (( This option might take from 5 to 10 mins & it's not included in the --all option ))")
    print(" -m     -->   For HTTP Method Expolitation ")
    print(" --all  -->   To Try All Techniques Above ")
    print(" --help -->   For The Help Menu ")

if "--help" in  sys.argv :
    Print_Help_Menu()
else :
    if '-p' in sys.argv or '--all' in sys.argv:
        Path_Fuzzing()
        Other_URL_Fuzzings()            
    if '-h' in sys.argv or '--all' in sys.argv: 
        Headers_Fuzzing()
    if '-u' in sys.argv :
        UserAgent_Fuzzing()
    if '-m' in sys.argv or '--all' in sys.argv:
        Method_Fuzzing()
    if '-c' in sys.argv or '--all' in sys.argv:
        Compound_Commands(target)
