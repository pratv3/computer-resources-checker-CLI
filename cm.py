import os
os.system("pip install time")
print("only works in windows os(linux version is comming soon)")
time.sleep(5)
os.system("color 9E")
os.system("cls")
os.system("pip install psutil")
from psutil import *
import time
while True:
    print("DEVLOPED by PRATV3")
    def cp ():
        v=int(cpu_percent())
        if v<=25:
            print("CPU-=[||||||]")
        if v>25 and v<=50:
            print("CPU-=[||||||||||]")
        if v>50 and v<=75:
            print("CPU-=[|||||||||||||||]")
        if v>75:
            print("CPU-=[||||||||||||||||||]")
        print(f"CPU in %-={v}")
    def disk():
        import random
        try:
            lst=["C://","E://","F://","D://"]
            a=random.choice(lst)
            usage=disk_usage(a)
            usd=usage.free / 1024**3
            us=usage.used / 1024**3
            dis=disk_partitions()
            print(f"{a} free--{usd}GiB")
            print(f"{a} used--{us}GiB")
            print(f"PARTITIONS_____--{dis}")
        except:
            print(f"no disk partition name{lst}")
        
    
        
    print("_______________________________LIVE CPU,RAM,HDD Uses____________________________________")
    cp()
    print(f"CPU-cores-={cpu_count()}")
    print(f"CPU-frequency-={cpu_freq()}")
    print(f"CPU-busses-={cpu_times_percent()}")
    print("____________________________________RAM(random acess memory)______________________________________")
    c=virtual_memory()
    print(c)
    print("____________________________________HDD(Hard Disk Drive)_________________________________________________")
    disk()
    time.sleep(1)
    os.system("cls")
