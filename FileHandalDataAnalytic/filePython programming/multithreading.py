# import threading
# import time
# def worker(num):
#     print(f"starting {num}: programe");
#     time.sleep(5)
#     print(f"ending the program {num}:hii")
# threads=[]
# for i in range(5):
#     thread = threading.Thread(target = worker, args = (i,))
#     threads.append(thread)
#     thread.start()
    
# for thread in threads:
#     thread.join()
# print("all thread completed");
def gree():
    print("Good morning all")

gree()