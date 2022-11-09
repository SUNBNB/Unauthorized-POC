# coding=utf-8
import ftplib, threading, requests, socket
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import time

R = threading.Lock()


def file_write(text):
    global R
    R.acquire()
    f = open('aodsec.txt', 'a', encoding='utf-8').write(text + '\n')
    R.release()
def rsync(u):
    try:
        u = u.replace("http://","").replace(":873","")
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((u,873))
        s.send(bytes("", 'UTF-8'))
        result = s.recv(1024).decode()
        # print(result)
        if "RSYNCD" in result:
            print(u + "可能存在rsync未授权,需要手工确认")
            file_write(u + "可能存在rsync未授权,需要手工确认")
        s.close()
    except Exception as e:
        pass
    finally:
        pass
        bar.update(1)
if __name__ == '__main__':
    print("""  
	  [#] Create By ::
	    _                     _    ___   __   ____                             
	   / \   _ __   __ _  ___| |  / _ \ / _| |  _ \  ___ _ __ ___   ___  _ __  
	  / _ \ | '_ \ / _` |/ _ \ | | | | | |_  | | | |/ _ \ '_ ` _ \ / _ \| '_ \ 
	 / ___ \| | | | (_| |  __/ | | |_| |  _| | |_| |  __/ | | | | | (_) | | | |
	/_/   \_\_| |_|\__, |\___|_|  \___/|_|   |____/ \___|_| |_| |_|\___/|_| |_|
	               |___/            By https://aodsec.com                                           
	""")
    time.sleep(2)
    ip = open('url.txt', 'r', encoding='utf-8').read().split('\n')
    bar = tqdm(total=len(ip))
    pool = ThreadPoolExecutor(500)
    for target in ip:
        target = target.strip()
        pool.submit(rsync, target)
