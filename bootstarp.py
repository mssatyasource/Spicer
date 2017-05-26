import logging
import os
from Trace import Trace



def InitalizeApplication():
    Trace.initLogFile()
    Trace.Info('application started')