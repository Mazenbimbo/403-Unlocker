#! /bin/python3

from colorama import Fore, Style
import pyfiglet
import sys 
import Header_Fuzzing
import Path_Fuzzing
import Compound
import Method_Fuzzing
import User_Agent_Fuzzing

Headers = open("Headers_with_values.txt","r")
raw_headers = open("raw_headers.txt","r")
user_agents = open("user-agents_enum.txt","r")
url_paths = open("url_fuzzing.txt","r")

help_message = """\
\n Usage : $ ./403_Unlocker.py [URL] [Options]

Please specify the http protocol type in the URL, ex : https://...

Options :
 -v     -->   To Not Show The Testing Progress 
 -c     -->   For Compound Commands (( This one uses multiple techniques together ))
 -p     -->   For Path Fuzzing 
 -h     -->   For Headers Fuzzing 
 -u     -->   For UserAgent Fuzzing (( This option might take from 5 to 10 mins & it's not included in the --all option ))
 -m     -->   For HTTP Method Exploitation 
 --all  -->   To Try All Techniques Above 
 --help -->   For The Help Menu
"""

if len(sys.argv) < 2 :
    print(help_message)
    sys.exit()

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

if "--help" in  sys.argv or "http" not in target :
    print(help_message)
else :
    if '-p' in sys.argv or '--all' in sys.argv:
        Path_Fuzzing.Path_Fuzzing(target,url_paths)
        Path_Fuzzing.Other_URL_Fuzzings(target)            
    if '-h' in sys.argv or '--all' in sys.argv: 
        Header_Fuzzing.Headers_Fuzzing(target,Headers,raw_headers,response_headers)
    if '-u' in sys.argv :
        User_Agent_Fuzzing.UserAgent_Fuzzing(target,user_agents)
    if '-m' in sys.argv or '--all' in sys.argv:
        Method_Fuzzing.Method_Fuzzing(target,methods,response_headers)
    if '-c' in sys.argv or '--all' in sys.argv:
        Compound.Compound_Commands(target,encoding,double_encoding,methods,HTTP_versions)