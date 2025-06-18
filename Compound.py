
from colorama import Fore, Style
import sys 
import subprocess 

def Compound_Commands(target,encoding,double_encoding,methods,HTTP_versions) :
    print( Fore.BLUE +"[+] Trying Compound Commands..."+Style.RESET_ALL)
    url = target
    url2 = target
    UserAgent = '-A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"' 
    if target.count('/') > 2 :
        file = target[target.rfind('/')+1:] 
        if file[0] in encoding :
            new_file = file.replace(file[0],encoding[file[0]])
            new_file2 = file.replace(file[0],double_encoding[file[0]])
            url = target[:target.rfind('/')+1]+new_file
            url2 = target[:target.rfind('/')+1]+new_file2
    for method in methods :
        for version in HTTP_versions :
            curl_output = subprocess.run(["curl","-v","-i",UserAgent,"-X",method,f"--http{version}", url],capture_output=True,text=True)
            curl_output2 = subprocess.run(["curl","-v","-i",UserAgent,"-X",method,f"--http{version}", url2],capture_output=True,text=True)
            curl_output3 = subprocess.run(["curl","-v","-i",UserAgent,"-X",method,f"--http{version}","-H",f"Referer: {url}",url],capture_output=True,text=True)
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
                        print(f"{Fore.RED}[ {status_code1} ]    curl -v -i -X {method} --http{version} {url2}{Style.RESET_ALL}")
                if status_code2 == "200" :
                    print(f"{Fore.GREEN}[ 200 ]    curl -v -i -X {method} --http{version} -H 'Referer: {url}' {url}{Style.RESET_ALL}")
                else :
                    if '-v' not in sys.argv :
                        print(f"{Fore.RED}[ {status_code2} ]    curl -v -i -X {method} --http{version} -H 'Referer: {url}' {url}{Style.RESET_ALL}")
            except Exception as e:
                print(e) 
