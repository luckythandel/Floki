
import sys
from itertools import combinations
import colorama
from colorama import init

init(autoreset=True)
use = colorama.Fore.GREEN +'''

Usage: python floki.py <STRING> <LENGTH> -m [0,1,2] -o FileName
        
        -h      -->     Help Menu.
        -m      -->     AAAA(0), ABCD(1), AAAA + ABCD(2)
        -o      -->     To Save The Output in a File
        Add - at last to get the output in such format: AAAABBBCCCCDDD, ABCDACDB...

       
'''
try:
    num = int(sys.argv[2])
    query = sys.argv[1]
except:
    print(use)


dubble_bool = []
junk =[]
wordlist = []


def repeated_seq(arg1, arg2):
    """ Output will be like, AAAA BBBB CCCC
    arg1 --> string
    arg2 --> num
     """
    
    for row in range(len(arg1)):
        if ( arg1[row]*arg2 not in junk ):
            wordlist.append(arg1[row]*arg2)
            junk.append(arg1[row]*arg2)


def random_seq(arg1, arg2):
    """Output will be random but will not repeat it self.
    arg1 --> string
    arg2 --> num
    """

    base_list = []
    base = 0
    if ( arg2-1 < len(arg1) ):
        while base <= len(arg1)-1:
            string_list = list(arg1)
            base_char = string_list[base]
            string_list.remove(base_char)            
            if ( base_char not in base_list ):  #Doesn't let a word be Base_char twice.
                for i in combinations(string_list, num-1):
                    result_char = (base_char+''.join(i))
                    wordlist.append(result_char)
                    base_list.append(base_char)
                    print(result_char, flush=False, end='\n')

                else:
                    init(autoreset=True)
                    print(colorama.Fore.LIGHTYELLOW_EX+ f"\nBase Char {base_char} Completed!!\n") # remove this without any hesitation

            base +=1


def generate():
    """Simply Generate The Output"""

    if (sys.argv[3].lower() == "-m"):
        action = int(sys.argv[4])
        if (action in [0,1,2]):
            
            if action == 0:
                repeated_seq(query, num)
                for i in range(len(wordlist)):
                    if (sys.argv[len(sys.argv)-1] == "-"):
                        print(wordlist[i],end='')
                    else:
                        print(wordlist[i])
            if action == 1:
                random_seq(query,num)
                for i in range(len(wordlist)):
                    if (sys.argv[len(sys.argv)-1] == "-"):
                        print(wordlist[i],end='')
                    else:
                        print(wordlist[i])
            if action == 2:
                repeated_seq(query,num)
                random_seq(query,num)
                for i in range(len(wordlist)):
                    if (sys.argv[len(sys.argv)-1] == "-"):
                        print(wordlist[i],end='')
                    else:
                        print(wordlist[i])
            
        else:
            init(autoreset=True)
            print(colorama.Fore.RED+"Invalid Value\n")


def save_output(arg1):
    """Saves The Output To A File"""

    f = open(arg1, 'a')
    if (sys.argv[3].lower() == "-m"):
        action = int(sys.argv[4])
        if (action in [0,1,2]):
            
            if action == 0:
                repeated_seq(query, num)
                #f.truncate(0)             # Enable this only if you want to clear the saved content of the output file first.
                for i in range(len(wordlist)):
                    f.write(wordlist[i]+"\n")   
            if action == 1:
                random_seq(query,num)
                #f.truncate(0)             # Enable this only if you want to clear the saved content of the output file first.
                for i in range(len(wordlist)):
                    f.write(wordlist[i]+"\n")
            if action == 2:
                repeated_seq(query,num)
                random_seq(query,num)
                #f.truncate(0)             # Enable this only if you want to clear the saved content of the output file first.
                for i in range(len(wordlist)):
                    f.write(wordlist[i]+"\n")
            f.close()

        else:  
            init(autoreset=True)
            print(colorama.Fore.RED+"\nInvalid Value\n")
            


def main():
    "Main Fucntion That Will Handle These Two Functions"
    
    try:
        if len(sys.argv) == 7:
            filename = sys.argv[6]
            save_output(filename)
        elif len(sys.argv) == 5 or 6:
            generate()
    except:
         #print(use)
         print("")

            
            
main()


                
    
