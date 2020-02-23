import numpy as np
import pandas as pd
import math
import time
from pymongo import MongoClient
from pprint import pprint

# Connection to database
client = MongoClient(port=27017)
db = client.ptposAddress # mongodb database in server hadoop@demo.rosebaycorporate.com -p 3002

start = 1
batch_size = 100   # Batch size
counter = 0  # starting from 1 because we are ignoring the first column which is the header name
# Counter is used to skip the batches
i = 1
while counter < 2:   # set the batch
    # start = counter * batch_size
    df = pd.read_csv('C:\\Users\\die_zer0\\hilman\\Data acquistion system\\alamat penerima januari reg 4 5.csv', header=None, names=['al_penerima'], skiprows=1, nrows=batch_size)
    # start = counter * batch_size
    # update to start and end rows
    for address in df['al_penerima']:
        data = {}
        print('Data processing : {}'.format(i))
        data['raw address'] = address
        print('Raw address : {}'.format(address))

    ####### Write a script to parse addresses using parser module

        result = db.addresses.insert_one(data)  # Save data in database
        print('Data processed : {}'.format(i))

        i+=1
        time.sleep(1)
    counter += 1