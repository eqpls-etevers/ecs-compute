# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from fastapi import HTTPException


#===============================================================================
# Constant
#===============================================================================
class TimeString:
    # Seconds
    S1 = 1
    S2 = 2
    S3 = 3
    S5 = 5
    S10 = 10
    S15 = 15
    S20 = 20
    S30 = 30
    S60 = 60
    # Minutes
    M1 = 60
    M2 = 120
    M3 = 180
    M5 = 300
    M10 = 600
    M15 = 900
    M20 = 1200
    M30 = 1800
    M60 = 3600
    # Hours
    H1 = 3600
    H2 = 7200
    H3 = 10800
    H6 = 21600
    H8 = 28800
    # Year
    Y1 = 31536000

    @classmethod
    def str2int(cls, key): return cls.__getattribute__(cls, key)

class EpException(HTTPException):

    def __init__(self, status_code, message):
        HTTPException.__init__(self, status_code, {'message':str(message)})
        LOG.ERROR(f'{status_code}: {str(message)}')