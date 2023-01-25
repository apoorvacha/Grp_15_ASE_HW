# function settings(s,    t) --> t;  parse help string to extract a table of options
#   t={};s:gsub("\n[%s]+[-][%S]+[%s]+[-][-]([%S]+)[^\n]+= ([%S]+)",function(k,v) t[k]=coerce(v) end)
#   return t end

# function cli(options) --> t; update key,vals in `t` from command-line flags
#   for k,v in pairs(options) do
#     v=tostring(v)
#     for n,x in ipairs(arg) do
#       if x=="-"..(k:sub(1,1)) or x=="--"..k then
#          v = v=="false" and "true" or v=="true" and "false" or arg[n+1] end end
#     options[k] = coerce(v) end 
#   return options end

# -- `main` fills in the settings, updates them from the command line, runs
# -- the start up actions (and before each run, it resets the random number seed and settings);
# -- and, finally, returns the number of test crashed to the operating system.
# function main(options,help,funs,     k,saved,fails)  --> nil; main program
#   saved,fails={},0
#   for k,v in pairs(cli(settings(help))) do options[k] = v; saved[k]=v end 
#   if options.help then print(help) else 
#     for _,what in pairs(keys(funs)) do
#       if options.go=="all" or what==options.go then
#          for k,v in pairs(saved) do options[k]=v end
#          Seed = options.seed
#          if funs[what]()==false then fails=fails+1
#                                      print("❌ fail:",what) 
#                                 else print("✅ pass:",what) end end end end
#   for k,v in pairs(_ENV) do 
#     if not b4[k] then print( fmt("#W ?%s %s",k,type(v)) ) end end 
#   os.exit(fails) end 


import sys, getopt

argumentList = sys.argv[1:]
 
b4={}
ENV = {}
for k,v in ENV:
    b4[k]=v #cache old names (so later, we can find rogues)
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
    
def main():
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        #, 
        # checking each argument
        print(arguments,values)
        for currentArgument, currentValue in arguments:
             print(currentArgument)
             if currentArgument in ('-h', ''):
                #  print("help here")
                 help()
            # if currentArgument in ("-g", "--go"):
            #     help()
                
            # elif currentArgument in ("-m", "--My_file"):
            #     print ("Displaying file_name:", sys.argv[0])
                
            # elif currentArgument in ("-o", "--Output"):
            #     print (("Enabling special output mode (% s)") % (currentValue))
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

if __name__ == "__main__":
    main()

   
