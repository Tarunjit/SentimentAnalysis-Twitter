## Source: http://api-portal.anypoint.mulesoft.com/twitter/api/twitter-rest-api/docs/concepts
## Source : https://github.com/geduldig/TwitterAPI

from TwitterAPI import TwitterAPI
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import _thread

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("SampleText.txt").read()
    #pullData = open("example2.txt").read()
    dataArray = pullData.split("\n")
    xar = []
    yar = []
    for eachline in dataArray:
        if len(eachline)>1:
            x,y = eachline.split(",")
            xar.append(int(x))
            yar.append(int(y))

    ax1.plot(xar,yar)

def func1(i):
    print('hello from thread %s\n' % i)

    ani = animation.FuncAnimation(fig,animate,interval=1000)
    plt.show()

def func2(i):
    print('hello from thread %s\n' % i)

    TRACK_TERM = 'pizza'

    ACCESS_TOKEN_KEY = "91070076-hXHCPWZNQiJ1LwwUFZLzjGJXMZLwoJkbZLKVCi6jx"
    ACCESS_TOKEN_SECRET = "V0zScYzfuKBTl0VWWHpG84Y34gNGkIN80PDs5eQsnEdgO"
    CONSUMER_KEY = "vVypmaitmk21exXEo22Bi691H"
    CONSUMER_SECRET = "9wWmNH6UgDafRuZKTZ02G7arEf9YsJfH2oYanaE6itk0FyMFKA"

    api = TwitterAPI(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN_KEY,
        ACCESS_TOKEN_SECRET)

    r = api.request('statuses/filter', {'track': TRACK_TERM})

    c = 0
    with open("example2.txt", "w+") as ed:
        for i in r:
            # ed.write(str(i["entities"]["hastags"])+"\n")
            if "pizza" in i["text"]:
                c+=1
            ed.write(str(c)+"," +str(c*3)+"\n")
#
# _thread.start_new(func1,(0,))

def func3(i):
    with open("SampleText.txt","a+") as fd:
        while(i<1000):
            fd.write(str(i) + "," + str(i*3)+"\n")
            i +=1
            time.sleep(1)

_thread.start_new(func3, (1,))

#
# def hello(num):
#     print('hello from thread %s\n' % num)
#
# _thread.start_new(hello,(3,))

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()

while 1:
    pass