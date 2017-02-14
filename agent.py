import time
import q_l
import rl_backend.modelX as mdX
import rl_backend.modelDetective as mdD
import numpy as np
<<<<<<< HEAD
#import matplotlib.pyplot as plt
=======
import matplotlib.pyplot as plt
>>>>>>> 2f744e67739147e729ece0226257010b6cd4a7bb
mdx = mdX.Model()
mdd = [None] * 5
for i in range (5):
	mdd[i] = mdD.Model()

epsilon = np.linspace(1, 0, num = 20000)
start = 0

def run_agent():
    start = 0
    countD = 0
    countX = 0
    diff = [0]*20000
    zeros = [0]*20000
    for i in range(len(epsilon)):
        times = time.time()
        _,month,day,hour,minute,second,_,_,_ = time.localtime(time.time())
        directory = str(month) + '-' + str(day) + '/' + str(hour) + '/' + str(minute) + '/'
        file_name = str(second)+'-'+ str(times - int(times)) + '.txt'
<<<<<<< HEAD
        ag = q_l.q_learn(mdx,mdd,explore = epsilon[start],directory = directory,file_name=file_name,loglevel='NOTSET')
        reward = ag.run_episode()
        ag.close_log() #Closing the log files
=======
        ag = q_l.q_learn(mdx,mdd,explore = epsilon[start],directory = directory,file_name=file_name,loglevel='CRITICAL')
        reward = ag.run_episode()
>>>>>>> 2f744e67739147e729ece0226257010b6cd4a7bb
        if reward == -100:
            countX+=1
        else:
            countD+=1
<<<<<<< HEAD
=======

>>>>>>> 2f744e67739147e729ece0226257010b6cd4a7bb
        print(epsilon[start],'\t',countD,'\t',countX)
        start = start + 1
        diff[i] = countD-countX
    print("Detectives=",countD)
    print("X=",countX)
<<<<<<< HEAD
    #plt.plot(diff)
    #plt.plot(zeros,'r--')
    #plt.ylabel('Detectives- X')
    #plt.xlabel('Episode')
    #plt.show()
=======
    plt.plot(diff)
    plt.plot(zeros,'r--')
    plt.ylabel('Detectives- X')
    plt.xlabel('Episode')
    plt.show()
>>>>>>> 2f744e67739147e729ece0226257010b6cd4a7bb


run_agent()
