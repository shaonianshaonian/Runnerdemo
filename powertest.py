# python2.7
# coding:utf-8
import requests,json,threading,time,datetime,logging
#定义消息发送次数
MessageSum = 0

#request请求api地址

url="http://112.74.234.108:8081/historicalquotation/queryHistoricalK?contractCode=Ag(T%2bD)&kType=month"
# 定义request的body内容
date={
    "contractCode": "Ag(T%2bD)",
    "kType": "month"
}
#定义header内容
header = {"content-type": "application/json"
          }

#定义log打印格式
"""logging.basicConfig(level=logging.DEBUG,
                    format='[process:%(process)d][threadid:%(thread)d][threadName:%(threadName)s][%(asctime)s][%(relativeCreated)d ][%(filename)s][line:%(lineno)d][module:%(module)s][funcName:%(funcName)s] %(levelname)s %(message)s',
                    filename='pushlog\\'+str(time.time())+ '.log',
                    filemode='warning')"""
#定义时间戳
def output_systime():
     nowtime_min=time.strftime('%Y%m%d%H%M%S')
     nowtime_microsecond=str(datetime.datetime.now().microsecond)
     nowtime=int(nowtime_min+nowtime_microsecond)
     print "当前时间为%s"%nowtime
     """logging.debug("当前时间为%s"%nowtime)"""

def sendMessage():
    global MessageSum
    for i in range(1,1000):        #消息发送次数可调整
        output_systime()
        r = requests.post(url,)
        print r.text
        MessageSum=MessageSum+1
    print "当前一共成功发送消息数目为%s"%MessageSum
    """logging.debug("当前一共成功发送消息数目为%s" % MessageSum)"""

def startThread(treadNum):
    threads=[]
    for treadtime in xrange(1,treadNum):
        T1 = threading.Thread(target=sendMessage)
        threads.append(T1)
        T1.setDaemon(True)

    for T1 in threads:
        T1.start()
        print "第%s个线程已经启动" % (threads.index(T1)+1)
        """logging.debug("第%s个线程已经启动" % (threads.index(T1)+1))"""
    for T1 in threads:
        T1.join()

    print "任务完成，线程终止，当前时间为%s" %time.ctime()
    """logging.debug("任务完成，线程终止，当前时间为%s" %time.ctime())"""

if __name__ == '__main__':
    print "多线程API自动化测试脚本启动"
    """logging.debug("多线程API自动化测试脚本启动")"""
    startThread(200)