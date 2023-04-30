import screen_brightness_control as sbc
import os
import platform
import distro
import cpuinfo
from colorama import Fore, Back, Style
import psutil

datalist = list()

def checkOS():
    
    datalist.append(platform.system())
    datalist.append(platform.release())
    datalist.append(cpuinfo.get_cpu_info()["brand_raw"])

def MacOS():
    checkOS()
    memfull = (psutil.virtual_memory().total / 1000000)
    datalist.append('%.0f' % (memfull))
    print((Fore.YELLOW) + f"Operating System : {datalist[0]}" + (Fore.GREEN) + f"\nVersion : {datalist[1]}" + (Fore.RED) + f"\nProcessor Name : {datalist[2]}" + (Fore.CYAN) + f"\n Total System Memory : {datalist[3]}MB")

def windows():
    checkOS()
    memfull = (psutil.virtual_memory().total / 1000000)
    datalist.append('%.0f' % (memfull))
    print((Fore.YELLOW) + f"Operating System : {datalist[0]}" + (Fore.GREEN) + f"\nVersion : {datalist[1]}" + (Fore.RED) + f"\nProcessor Name : {datalist[2]}" + (Fore.CYAN) + f"\n Total System Memory : {datalist[3]}MB")
      
    
def linux():
    checkOS()
    datalist.append(distro.id())
    memfull = (psutil.virtual_memory().total / 1000000)
    datalist.append('%.0f' % (memfull))
    datalist.append(sbc.get_brightness()[0])
    print((Fore.YELLOW) + f"Operating System : {datalist[0]}" + (Fore.GREEN) + f"\nLinux Kernel Version : {datalist[1]}" + (Fore.RED) + f"\nProcessor Name : {datalist[2]}" + (Fore.BLUE) + f"\nLinux Distribution : {datalist[3].capitalize()}" + (Fore.CYAN) + f"\nTotal System Memory : {datalist[4]} MB" + (Fore.WHITE) + f"\nScreen Brightness Level : {datalist[5]}%")

if platform.system() == "Linux":
    linux()
elif platform.system() == "Windows":
    windows()
elif platform.system() == "Darwin":
    MacOS()

    




    

        
