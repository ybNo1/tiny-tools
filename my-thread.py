from multiprocessing import Pool
from time import sleep
from multiprocessing import Pool
import random
def show(num):
    sleep(random.randint(0, 10))
    print('num : ' + str(num))
if __name__=="__main__":
    pool = Pool(processes = 60)
    for i in range(60):
        # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply_async(show, args=(i, ))       
    print('======  apply_async  ======')
    pool.close()
    #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    pool.join()