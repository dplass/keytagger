Keytagger
=========

writes codes (markers) related to key presses, to annotate physiological data 
recordings.

### Available at the moment

* writing keyboard codes to COM6 (for example, to use with the Emotiv EPOC), and printing information for logging.
It should be relatively easy to adjust to output to a parallel port (with 
pyparallel), and to also catch mouse activities (using pyhook)

* writing codes related to mouse button presses to COM6, and printing information for logging.

* printing mouse wheel actions.

* uncommented: code to make screenshots on mouse clicks. This code can cause delays and does not seem to work in-game (then makes screenshots of the desktop beneath it).

### Requires

python libraries: pyHook*, pyserial, pythoncom, PIL
And if no serial port available: com0com, to create a virtual pair.

* Added pyHook dir, because I had to include one small fix, that may be related to working on a 64-bit system.

### How to use keyboard2com with the Emotiv EPOC

* With com0com, create COM5 and COM6
* In Emotiv Testbench, set the COM port to COM5
The script writes to COM6.

To log additional information on the key presses, such as the active window, use

python keytagger.py >> log-%DATE:~-4%%DATE:~-7,-5%%DATE:~-10,-8%-%TIME:~-11,-9%%TIME:~-8,-6%.txt

(the log filename will be marked with a timestamp)

### TODO

* Also listen to mouse actions
* Key combi to turn the tagging on/off
* Key combi to kill the program
* Make a nice main function which takes specific arguments, such as for the com 
port.
* Encountered a bug that resulted in a TypeError (not an Integer), that seems 
related to using the hook. Now I simply catch the error after adding the key ID
to a queue, and that works. But this should be fixed at some point!
* Create a parallel port version to use with Biosemi.
* Add an optional timeout to the writing and an optional reset code.



