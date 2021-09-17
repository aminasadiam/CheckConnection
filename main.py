import platform
import subprocess
import requests
import time
import jdatetime
from datetime import datetime

def getPing(hostname):
    parametr = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parametr, '1', hostname]
    return subprocess.getoutput(command)

def checkConnection():
    url = 'https://aparat.com'
    timeout = 5

    try:
        request = requests.get(url, timeout)
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        return False

def submitLog(log):
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(log)


def main():
    disconnectTime = ''

    while checkConnection:
        result = getPing('4.2.2.4').split(' ')
    
        if "Average" in result:
            pos = result.index('Average')
            print(result[pos + 2])
        else:
            disconnectTime = jdatetime.datetime.now().strftime("%Y/%b/%d - %a - %H:%M:%S")
            submitLog(f'{disconnectTime} Disconnected\n')
            print('Disconnected!')
        
        time.sleep(1)

if __name__ == '__main__':
    main()