"""
load btc history date to pandas DataFrame
export DataFrames to HDFStore
"""
import numpy as np
import pandas as pd
import datetime
import glob
import sys

def LoadData(filename):
    """
    do Load data stuff
    return a DataFrame with time index
    """
    b_with_id = filename.split('.')[0].endswith('id')
    if b_with_id == False:
        col_name = ['timestamp','type','amount','price']
    else:
        col_name = ['timestamp','type','amount','price','id']

    try:
        df = pd.read_csv(filename,names=col_name)
        time_index = df['timestamp'].apply(lambda t:datetime.datetime.fromtimestamp(t))
        df.index = time_index

    except Exception,e:
        print e

    return df

def LoadCsvInPath(path,h5file=''):
    """
    """
    csvs = glob.glob(path+'/*.csv')

    # first do load single files to hdfstore
    # they are not with id
    try:
        for f in csvs:
            table_name = 'trade_'+f.split('.')[0].split('/')[-1]
            df = LoadData(f)
            print('Processing ' + f + ' with tablename: ' + table_name)
            df.to_hdf(h5file,table_name,append=True)
    except Exception,e:
        print e

def LoadAll2HDFStore(path,h5file=''):
    """
    use glob
    """
    directories = glob.glob(path+'/*/')
    # second do load files in paths
    # they may follow a id
    directories.append('/./')
    try:
        for d in directories:
            LoadCsvInPath(d,h5file)
    except Exception,e:
        print e

def usage():
    print "usage:"
    print sys.argv[0] +" path hdf5path"
    print "example: python load_data.py /opt/btc_data_path /data/btc.h5"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        exit(-1)

    LoadAll2HDFStore(sys.argv[1],sys.argv[2])
