#!/usr/bin/python
# -*- coding: UTF-8 -*-

import configparser
import time
import os
import standard_data as STD


ReportFilePath = r"C:\TestLogSummary1"

ComputerName = os.getenv('COMPUTERNAME', 'defaultValue')

ModelName = "W2G50-60001"
FixtureID = "01"
Timestr = time.strftime('%Y%m%d',time.localtime(time.time()))
StrYear = Timestr[0:4]
StrMonth = Timestr[4:6]
StrDay = Timestr[6:8]

IniFileName = ComputerName + "_" + ModelName + "_" + FixtureID + "_" + Timestr + ".txt"
ReportFilePath = ReportFilePath + "\\" + StrYear + "\\" + StrMonth
IniFilePathName = ReportFilePath + "\\" + IniFileName

def create_ini_file(IniFilePathName):
    config = configparser.ConfigParser()
    config['Summary'] = {}
    config['Summary']['Total'] = '0'
    config['Summary']['Rate'] = '0'
    config['Summary']['Pass'] = '0'
    config['Summary']['Fail'] = '0'
    config['Summary']['CTMAX'] = '0'
    config['Summary']['CTMIN'] = '0'
    config['Summary']['CTAverage'] = '0'
    config['Summary']['StartTestTime'] = '0'
    config['Summary']['EndTestTime'] = '0'

    config['CellsSummary'] = {}
    config['CellsSummary']['Cell_1_Total'] = '0'
    config['CellsSummary']['Cell_1_Rate'] = '0'
    config['CellsSummary']['Cell_1_Pass'] = '0'
    config['CellsSummary']['Cell_1_Fail'] = '0'
    
    config['FailCount'] = {}

    with open(IniFilePathName, 'w') as configfile:
        config.write(configfile)

def record_data(Standard_Data):
    '''
        Recorder test log into *.ini file, 
        ini file name:ComputerName_ModelAssembly_FixtureID_Time.ini
        ini file contents:
        [Summary]
        [CellsSummary]
        [FailCount]
    '''
    # check path exist
    if not os.path.exists(ReportFilePath):
        print("The %s path not found, We will create the path." %ReportFilePath)
        os.makedirs(ReportFilePath)

    # check ini file exist
    if not os.path.isfile(IniFilePathName):
        print("The %s file not found, We will create it." %IniFilePathName)
        create_ini_file(IniFilePathName)

    # recode data into file




if __name__ == '__main__':
    P1 = STD()
    P1.make_test_data()
    P1.print_alldata()
    #record_data(P1)

P = "asdf"
print(IniFilePathName)
record_data(P)