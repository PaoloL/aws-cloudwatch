#!/usr/bin/env python2

__version__     = "1.0.1"
__author__      = "Paolo Latella"
__email__       = "paolo.latella@xpeppers.com"

from boto.ec2 import cloudwatch
import psutil
import urllib2

pid_file="/var/run/nginx.pid"

#get instance medatadata
InstanceId=urllib2.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()

#connect to Cloudwatch
cw = cloudwatch.connect_to_region('eu-central-1')

#retrieve RAM info by psutil
ram_percent = psutil.virtual_memory().percent
swp_percent = psutil.swap_memory().percent
#push metric to cloudwatch
cw.put_metric_data('MEM', 'RAM Usage', ram_percent, unit='Percent', dimensions={"InstanceId": InstanceId})
cw.put_metric_data('MEM', 'SWP Usage', swp_percent, unit='Percent', dimensions={"InstanceId": InstanceId})

#get process info by psutil
run_file = open(pid_file,"r")
pid = run_file.readline()
run_file.close()
p = psutil.Process(int(pid))
pid_percent = p.memory_percent()
pid_thread = p.num_threads()
print(pid_percent)
#push metric to cloudwatch
cw.put_metric_data('PID', 'Thread', pid_thread, unit='Count', dimensions={"InstanceId": InstanceId})
cw.put_metric_data('PID', 'Memory Usage', pid_percent, unit='Percent', dimensions={"InstanceId": InstanceId})