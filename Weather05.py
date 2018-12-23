# **************************************************
# *   Printing out the weather forecast of a Town. *
# *   These arguments are passed from Command Line *
# *   into the program                             *
# **************************************************

import sys                        # COMMAND LINE ARGUMENTS:
                                  #   In the command line, we can start a program 
                                  #   with additional arguments.
                                  #
                                  #   For example, the command line:
                                  #           --> python3 Weather05.py
                                  #   , could have some additional arguments:
                                  #           --> python3 Weather05.py argument01 argument02 argument03 .....
                                  #
                                  #   'sys' module: an additional module of the Python,
                                  #   that manages all Arguments in command line. 
                                  #

                                  # COMMAND LINE SYNTAX:
                                  #   Type in your command Line (Linux): 
                                  #            --> python3 Weather05.py <TOWN> <APPID> <DATE> <TIME> 
                                  #    FOR EXAMPLE:
                                  #            --> python3 Weather05.py London <APPID> 20181218 140020
                                  #        , where <APPID> is a 32-characters ID-KEY you can obtain for free after signing up to:
                                  #                                                          https://www.openweathermap.org/).







# *****************************************************************************************************************************
#                                                                                                                             *
# Dictionaries:
status_400 =  {
                "code": "400",
                "descr": "Bad Request"
              }
status_404 =  {
                "code": "404",
                "descr": "Not Found"
              }
status_500 =  {
                "code": "500",
                "descr": "Internal Server Error"
              }
#                                                                                                                             *
# *****************************************************************************************************************************







# *****************************************************************************************************************************
#                                                                                                                             *
# Check the Location.
try:
    sys.argv[1]                                          # sys.argv[1] is the second Argument in command line.
except IndexError:
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[1], second Argument missing in command line; TOWN missing; type:\n', 
          '       python3 Weather.py <TOWN> <APPID> <DATE> <TIME>')
    sys.exit()
else:
    argument01 = str(sys.argv[1])                                     
    print('\nargument01 :', argument01)
#                                                                                                                             *
# *****************************************************************************************************************************







# *****************************************************************************************************************************
#                                                                                                                             *
# Check the appid (obtainable for free after signing up to: https://www.openweathermap.org/).
try:
    sys.argv[2]                                          # sys.argv[2] is the third Argument in command line.
except IndexError:
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[2], third Argument missing in command line; APPID missing; type:\n', 
          '       python3 Weather.py', argument01, '<APPID> <DATE> <TIME>\n',
          '\n',
          '       APPID can be obtained for free after signing up to: https://www.openweathermap.org/')
    sys.exit()
else:
    argument02 = str(sys.argv[2])                                     
    print('argument02 :', argument02)
#                                                                                                                             *
# *****************************************************************************************************************************







# *****************************************************************************************************************************
#                                                                                                                             *
# Check the date.

import datetime

# check date_valid :  date has to be valid
try:                                                                   # sys.argv[3] is the fourth Argument in command line
    date_valid = datetime.datetime.strptime(sys.argv[3], '%Y%m%d')     # date valid:  YYYY-mm-dd
except IndexError:
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[3], fourth Argument missing in command line; DATE missing; type:\n', 
          '       python3 Weather.py', argument01, argument02, '<DATE> <TIME>\n',
          '\n',
          '       <DATE> format: yyyymmdd\n',
          '       <DATE> is mandatory')
    sys.exit()
except (ValueError, TypeError):
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[3], fourth Argument wrong in command line; DATE = ', sys.argv[3], ' has a bad Type or Value; type:\n', 
          '       python3 Weather.py', argument01, argument02, '<DATE> <TIME>\n',
          '\n',
          '       <DATE> format: yyyymmdd\n',
          '       <DATE> is mandatory')
    sys.exit()
else:
    d = datetime.date(datetime.datetime.strptime(sys.argv[3], '%Y%m%d').year,  
                      datetime.datetime.strptime(sys.argv[3], '%Y%m%d').month, 
                      datetime.datetime.strptime(sys.argv[3], '%Y%m%d').day
                     )
    argument03 = d

# print("datetime.date(datetime.datetime.strptime(sys.argv[3], '%Y%m%d').year,\n"
#       "              datetime.datetime.strptime(sys.argv[3], '%Y%m%d').month,\n"
#       "              datetime.datetime.strptime(sys.argv[3], '%Y%m%d').day\n"      
#       "             ) = ", 
#        datetime.date(datetime.datetime.strptime(sys.argv[3], '%Y%m%d').year,
#                      datetime.datetime.strptime(sys.argv[3], '%Y%m%d').month,
#                      datetime.datetime.strptime(sys.argv[3], '%Y%m%d').day
#                     )
#      )

print('argument03 :', argument03)
#                                                                                                                             *
# *****************************************************************************************************************************







# *****************************************************************************************************************************
#                                                                                                                             *
# check date & time :  date/time has to be in the future
def check_dt(d,t):
    dt = datetime.datetime.combine(datetime.date(d.year, d.month, d.day), 
                                   datetime.time(t.hour, t.minute, t.second)     # combine date & time:  YYYY-mm-dd HH:MM:SS
                                  )
    # print("combine(d,t) =", dt)
    if (dt < datetime.datetime.utcnow()):
        print('ERROR:', status_400["code"], status_400["descr"], '\n',
              'sys.argv[3]/sys.argv[4], date/time is in the past; ', dt , ' < ', datetime.datetime.utcnow(), ' type:\n', 
              '       python3 Weather.py', argument01, argument02, '<DATE> <TIME>\n',
              '\n',
              '       <DATE> format: YYYYmmdd   <TIME> format: HHMMSS\n',
              '       <DATE>,<TIME> are mandatory')
        sys.exit()
    else:
        # print("OK: ...... dt  >= datetime.datetime.utcnow()).....,", dt, ">", datetime.datetime.utcnow())
        return dt







# *****************************************************************************************************************************
#                                                                                                                             *
# Check the time.
try:                       # check errors : time has to be valid 
     time_valid = datetime.datetime.strptime(sys.argv[4], '%H%M%S')    # sys.argv[4] is the fifth Argument in command line
except IndexError:                                                     #                  (%Hours %Minutes %Seconds)
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[4], fifth Argument missing in command line; TIME missing; type:\n', 
          '       python3 Weather.py', argument01, argument02, argument03, '<TIME>\n',
          '\n',
          '       <TIME> format: HHMMSS\n',
          '       <TIME> is mandatory')
    sys.exit()
except TypeError:
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[4], fifth Argument wrong in command line; TIME = ',sys.argv[4],' has a bad Type; type:\n', 
          '       python3 Weather.py', argument01, argument02, argument03, '<TIME>\n',
          '\n',
          '       <TIME> format: HHMMSS\n',
          '       <TIME> is mandatory')
    sys.exit()
except ValueError:
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'sys.argv[4], fifth Argument wrong in command line; TIME = ',sys.argv[4],' has a bad Value; type:\n', 
          '       python3 Weather.py', argument01, argument02, argument03, '<TIME>\n',
          '\n',
          '       <TIME> format: HHMMSS\n',
          '       <TIME> is mandatory')
    sys.exit()
else:
    t = datetime.time(datetime.datetime.strptime(sys.argv[4], '%H%M%S').hour,    # sys.argv[4] is the fifth Argument in command line
                      datetime.datetime.strptime(sys.argv[4], '%H%M%S').minute,  #                  (%Hours %Minutes %Seconds)
                      datetime.datetime.strptime(sys.argv[4], '%H%M%S').second
                     )
    argument_03_04 = check_dt(d,t)                                               # combine(d,t)
    argument04 = t



# print("datetime.time(datetime.datetime.strptime(sys.argv[4], '%H%M%S').hour,\n"    
#       "              datetime.datetime.strptime(sys.argv[4], '%H%M%S').minute,\n"  
#       "              datetime.datetime.strptime(sys.argv[4], '%H%M%S').second\n"
#       "             ) = ", 
#        datetime.time(datetime.datetime.strptime(sys.argv[4], '%H%M%S').hour,
#                      datetime.datetime.strptime(sys.argv[4], '%H%M%S').minute,
#                      datetime.datetime.strptime(sys.argv[4], '%H%M%S').second
#                     )
#      )

print('argument04 :', argument04)
# print('argument_03_04 :', argument_03_04)
#                                                                                                                             *
# *****************************************************************************************************************************







# *****************************************************************************************************************************
#                                                                                                                             *
# importing the requests library 
#                                                                                                                             *
# *****************************************************************************************************************************
import json
import requests
print('requests.__version__ :', requests.__version__)


# definig API_URL: ###################################################################################################
# 
#  API_URL = 'https://api.openweathermap.org/data/2.5/forecast?q=London&APPID=appid&stream=True'     
# 
#                     , where <appid> is a 32-characters ID-KEY you can obtain for free after signing up to:
#                                                                                  https://www.openweathermap.org/
# 
# ####################################################################################################################

# defining the api-endpoint 
API_ENDPOINT =  'https://api.openweathermap.org/data/2.5/forecast'

# your Location here
location     =  argument01 

# defining the appid that can be obtained for free after signing up to: https://www.openweathermap.org/
appid        =  argument02

# your PARAMS to be sent to api: Location, API KEY 
PARAMS       =  {'q':location, 
                 'APPID':appid,        # insert here your appid value (32 cahacters)
                 'stream':'True'} 


# ################################################################################################
# get a Response (Object). We can get all the information we need from this object. 
# 
# ################################################################################################

# NOTE: "GET" / "POST" requests
#       Here "POST" method is mandatory, because of the secret information of the 'APPID'
#       By the "POST" method, data are separated from the URL (for your own safety)

# get a Response (Object). We can get all the information we need from this object:
#                           r = requests.post(url = API_ENDPOINT, params = PARAMS)

try:
    r = requests.post(url = API_ENDPOINT, params = PARAMS)
    r.raise_for_status()
except requests.exceptions.HTTPError as err1:
    print('')
    print('Error:', status_404["code"], status_404["descr"], '\n',
          'requests invalid or no data found;  type:\n', 
          '       python3 Weather.py <TOWN> <APPID> <DATE> <TIME>\n',
          '\n',
          '       <TIME> format: HHMMSS\n',
          '       <TIME> is mandatory')
    print(err1)
    sys.exit()
except (requests.exceptions.URLRequired, requests.exceptions.RequestException, requests.exceptions.ConnectionError,
        requests.exceptions.Timeout, requests.exceptions.TooManyRedirects) as err2:
    print('')
    print('Error:', status_500["code"], status_500["descr"], '\n',
          'requests invalid or no data found;  type:\n', 
          '       python3 Weather.py <TOWN> <APPID> <DATE> <TIME>\n',
          '\n',
          '       <TIME> format: HHMMSS\n',
          '       <TIME> is mandatory')
    print(err2)
    sys.exit()





print('r.status_code:', r.status_code)
# print("r.request.headers['User-Agent']:", r.request.headers['User-Agent'])  # the headers we sent to the server
# print("r.headers['content-type']:", r.headers['content-type'])              # the headers the server sent back to us
# print("r.url:", r.url)
print()
# print(r.json())

R = r.json()

# lenght_R_list = len(R['list'])
# print("lenght_R['list']:", lenght_R_list)

i = 0
j = 0
for line in R['list']:
    # print("\n line", line)
    if (datetime.datetime.strptime(R['list'][i]['dt_txt'], "%Y-%m-%d %H:%M:%S") >= argument_03_04):
        j = j + 1
        print(j, ')', R['list'][i]['dt_txt'])
        print('', R['city']['name'], '(', R['city']['country'], '),\n',
            R['list'][i]['weather'][0]['main']+':', R['list'][i]['weather'][0]['description'], ',\n',
            'Humidity:', str(R['list'][i]['main']['humidity'])+'% ,\n', 
            'Pressure:', str(R['list'][i]['main']['pressure'])+'hPa ,\n',
            'Temperature:', str(round(R['list'][i]['main']['temp']-273.15, 1))+'°C\n')
        i = i + 1
    else:
        i = i + 1


if(j == 0):
    print('ERROR:', status_400["code"], status_400["descr"], '\n',
          'no data found in the request, date/time could be too far in the future (more than 5 days) or no data found;   type:\n', 
          '       python3 Weather.py <TOWN> <APPID> <DATE> <TIME>\n',
          '\n',
          '       <DATE> format: YYYYmmdd   <TIME> format: HHMMSS\n',
          '       <DATE>,<TIME> are mandatory')
    sys.exit()

