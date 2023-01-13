//passthief is a Python script designed to work with dynamic loading of modules or plugins, whatever you may call them.
//By default Firefox and Chrome modules are enabled.
//If you wish to use a module called "linux", you call the script like this:
./passthief.py -m linux

//The output should be something like this(if the module is present):

	██████╗  █████╗ ███████╗███████╗████████╗██╗  ██╗██╗███████╗███████╗
	██╔══██╗██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║  ██║██║██╔════╝██╔════╝
	██████╔╝███████║███████╗███████╗   ██║   ███████║██║█████╗  █████╗
	██╔═══╝ ██╔══██║╚════██║╚════██║   ██║   ██╔══██║██║██╔══╝  ██╔══╝
	██║     ██║  ██║███████║███████║   ██║   ██║  ██║██║███████╗██║
	╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚═╝
	Version 0.2.1
	
[*] Checking modules:
[*] Loaded module: Linux
[*] Loaded module: Firefox
[*] Loaded module: Chrome

Started: 10/12/2017 3:9
-Chrome:
...
-Firefox:
...
-Linux:
...
Finished: 10/12/2017 3:9



//If you wish to write a module for passthief,you're lucky because it's very easy.
//All you have to do is create a corresponding .py file in the modules directory.
//Let's write a test module together:
cd modules
touch test.py

//Open up your favorite code/text editor and let's get started.
import colorama
from colorama.Fore import GREEN
from colorama.Style import RESET_ALL
def steal():
	colorama.init()
    	return print_it()
def print_it():
	return "{g}This works!{rs}".format(g=GREEN,rs=RESET_ALL)

//Now try it out:
./passthief.py -m test

