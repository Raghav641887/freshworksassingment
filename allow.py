import threading
from threading import*
import time
import backendcode as x
x.create("sastra",25)

x.create("src",71,2100)

x.read("sastra")

x.read("src")

x.create("sastra",50)

x.modify("sastra",55)

x.delete("sastra")

key_name = input()
value = int(input())
timeout = int(input())
t1=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout))
t1.start()
t1.join()
key_name = input()
value = int(input())
timeout = int(input())
t2=threading.Thread(target=(x.create or x.read or x.delete),args=(key_name,value,timeout))
t2.start()
t2.join()
