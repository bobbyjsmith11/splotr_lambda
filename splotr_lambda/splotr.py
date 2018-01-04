#!/usr/bin/python
"""
========================
splotr.py
========================
"""

import matplotlib
import numpy as np
import skrf

matplotlib.use('agg')

def my_handler(event, context):
    # return {"message" : "what's up"}
    dat = event['queryStringParameters']

    try:
      message = 'Hello {} {}!'.format(dat['first_name'],
                                      dat['last_name'])
      # message = 'Hello {} {}!'.format(event['first_name'],
      #                                 event['last_name'])
    except KeyError:
      return {
               'statusCoode': 200,
               'body': str(event)
             }
    return {
             'statusCoode': 200,
             'body': message
           }


def getLogMagnitude( fi ):
    """
    """
    try:
        n = skrf.Network( fname )   # pass in the file you just created
    except Exception as e:
        print(e)
    d = { 'f':                  n.f.tolist(),
          'number_of_ports':    int(n.number_of_ports)
          }
    for j in range(n.number_of_ports):      # j is second port
        for k in range(n.number_of_ports):  # k is first port
            tmp = []
            d["s"+str(j+1)+str(k+1)+"db"] = n.s_db[:,j,k].tolist()
    return response.json(d)


