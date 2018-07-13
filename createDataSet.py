#!/usr/bin/python

import sys
import argparse
import h5py
import numpy as np 
import time
parser = argparse.ArgumentParser()
parser.add_argument("filename",help="hdf5 file name")
parser.add_argument("-d","--days", type=int,default=1,help="data for numbers of days(>0)")
parser.add_argument("-i","--interval", default=1,type=int,help="number of seconds between two records(>0)")
parser.add_argument("-n","--numbers", default=2,type=int,help="numbers of data points(>0)")
parser.add_argument("-m","--minus", default=False,type=bool,help="data can be minus")
args = parser.parse_args()


if args.days == 0 or args.interval == 0 or args.numbers == 0 :
	parser.print_help();
	sys.exit(-1);
#args.days=0.25
totalDataSample=int(args.days*24*60*60/args.interval)
print(totalDataSample)
f = h5py.File(args.filename, 'w')
for n in range(1,args.numbers+1):
	timestamp=int(time.time())
	data = np.empty([2, totalDataSample])
	data[0:] = range(timestamp-int(args.days*24*60*60),timestamp,args.interval)
	if args.minus :
		data[1:]=(np.random.rand(1, totalDataSample)-0.5)*2000
	else:
		data[1:]=np.random.rand(1, totalDataSample)*1000	
	datapoint = f.create_dataset("datapoint"+str(n), (2, totalDataSample), chunks=True,data=data)
f.close()