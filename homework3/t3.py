import configparser
import time
import datetime
import psutil



def monitor ():
    Config = configparser.ConfigParser()
    Config.read('conf.ini')
    Output = Config['DEFAULT']['output']
    Interval = Config['DEFAULT']['interval']
    Snap = int(Config['SNAPSHOT']['number'])
    while True:
        # CPU load
        Cpu = psutil.cpu_percent(interval=1)
        # mem
        Mem = (psutil.virtual_memory()).percent
        Virt_mem = (psutil.swap_memory()).percent
        # io
        Disk_usage = (psutil.disk_usage('/')).percent
        # net
        Net_packets_recv = (psutil.net_io_counters(pernic=False)).packets_recv
        Net_packets_sent = (psutil.net_io_counters(pernic=False)).packets_sent

        Time_stampe = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        file = open("/home/student/PycharmProjects/untitled/venv/f", "a")
        print("SNAPSHOT{0:3d}::{1}::{2:4}::{3}::{4:3}::{5}::{6}".format(Snap, Time_stampe, Cpu, Mem, \
                                                                        Virt_mem, Disk_usage, Net_packets_recv))
        file.write("SNAPSHOT{0:3d}::{1}::{2:4}::{3}::{4:3}::{5}::{6}\n".format(Snap, Time_stampe, Cpu, Mem, \
                                                                               Virt_mem, Disk_usage, Net_packets_recv))
        file.close()
        Snap += 1
        Config['SNAPSHOT'] = {'number': "{}".format(Snap)}
        with open('conf.ini', 'w') as configfile:
            Config.write(configfile)
        time.sleep(int(Interval)*60)
    return 0

monitor ()

