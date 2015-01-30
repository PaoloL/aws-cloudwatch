aws-cloudwatch
===========

A simple Amazon cloudwatch example


memwatch.py
--------------------------------
How to use boto library and psutil in Python to monitor RAM and Process resrources and push metric to CloudWatch

1) Install
sudo apt-get install python-pip
sudo apt-get install python-dev
pip install boto
pip install psutils

2) Use from a EC2 instance
while true ; do python memwatch.py; sleep 60; echo "pushed"; done

