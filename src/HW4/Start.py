import sys, getopt
from Examples import *
from pathlib import Path

argumentList = sys.argv[1:]
 
b4={}
ENV = {}
for k,v in ENV:
    #cache old names (so later, we can find rogues)
    b4[k]=v

# Options
options = "hg"
 
# Long options
long_options = []

def help():
    a= """
        data.lua : an example csv reader script
        (c)2022, Tim Menzies <timm@ieee.org>, BSD-2 
        USAGE:   data.lua  [OPTIONS] [-g ACTION]
        OPTIONS:
        -d  --dump  on crash, dump stack = false
        -f  --file  name of file         = ../etc/data/auto93.csv
        -g  --go    start-up action      = data
        -h  --help  show help            = false
        -s  --seed  random number seed   = 937162211
        ACTIONS:
        ]] """
    print(a)

the = {"seed": 937162211, "dump": False, "go": "data", "help": False}

def run_tests():
    func_pass= 0
    test_suite = [test_sym, test_nums, test_the, test_every]

    for i,test in enumerate(test_suite):
        if(test()):
            func_pass += 1
    print("\nTotal Test Cases Passing: " + str(func_pass) + "\nTotal Test Cases Failing: " + str(len(test_suite)-func_pass))
  
    
def main():
    try:    
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        # checking each argument
        for currentArgument, currentValue in arguments:
             if currentArgument in ('-h', ''):
                 help()
             if currentArgument in ("-g", ''):
                run_tests()
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

if __name__ == "__main__":
    main()

   
