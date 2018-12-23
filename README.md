# weather-forecast
A Python script for the Weather Forecast
-------------------------------------------

This is a Command Line script for Linux, printing out the weather forecast starting from a  date/time.
#

° Download the script Weather05.py on your computer.

° Put the script in the root of your Linux.

° Open your Linux terminal (for example in Ubuntu 18.04:  Ctrl - Alt + T ).

° Type in the command line:

 --> python3 Weather05.py «TOWN» «APPID» «DATE» «TIME»

---------------------------------------------
 FOR EXAMPLE:
 
 --> python3 Weather05.py London «APPID» 20181229 140020
  
 , where «APPID» is a 32-characters ID-KEY you can obtain for free after signing up to:
  
……………. https://www.openweathermap.org/ ……………..
#

This is a Python script for the requests to the URL

All the arguments are mandatory.

Combining the date (YYYYmmgg) and time (e.g.: HHMMSS) you'll get the starting time the weather forecast will be printed out.
#

ERRORS. The script will response with three status_code and descriptions:

 status_code = "400" ----->  "Bad Request"
 
 status_code = "404" ----->  "Not Found"
 
 status_code = "500" ----->  "Internal Server Error" 
 


