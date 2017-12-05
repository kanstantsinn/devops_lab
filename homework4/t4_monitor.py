import datetime
import psutil

class Monitor:
    'Monitoring system class'
    empCount = 0
    def __init__(self, snap):
        self.cpu = psutil.cpu_percent(interval=1)
        self.mem = (psutil.virtual_memory()).percent
        self.virt_mem = (psutil.swap_memory()).percent
        self.disk_usage = (psutil.disk_usage('/')).percent
        self.net_packets_recv = (psutil.net_io_counters(pernic=False)).packets_recv
        self.time_stampe = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.snap = snap
        Monitor.empCount += 1
    def display(self):
        print("SNAPSHOT{0:3d}::{1}::{2:4}::{3}::{4:3}::{5}::{6}\n".format(self.snap, self.time_stampe, self.cpu, self.mem, \
                                                                        self.virt_mem, self.disk_usage, self.net_packets_recv))
    def logging(self):
        file = open("/home/student/PycharmProjects/untitled/venv/monitor.log", "a")
        file.write("SNAPSHOT{0:3d}::{1}::{2:4}::{3}::{4:3}::{5}::{6}\n".format(self.snap, self.time_stampe, self.cpu, self.mem, \
                                                                        self.virt_mem, self.disk_usage, self.net_packets_recv))
        file.close()
        print(
            "SNAPSHOT{0:3d}::{1}::{2:4}::{3}::{4:3}::{5}::{6}\n".format(self.snap, self.time_stampe, self.cpu, self.mem, \
                                                                        self.virt_mem, self.disk_usage,
                                                                        self.net_packets_recv))
    def __repr__(self):
        return "cpu : " + str(self.cpu) + ", mem: " + str(self.mem) + ", disk usage: " + str(self.disk_usage)



