#!/usr/bin/python
# -*- coding: UTF-8 -*-


SN = ""
Customer = ""
BoardStyle = ""
TesterName = ""
Process = ""
FixtureSlot = ""
Fixture = ""
SoftwareDocument = ""
SoftwareRevision = ""
AssemblyNumber = ""
AssemblyRevision = ""
AssemblyVersion = ""
FirmwareRevision = ""
TestStatus = ""     #Pass,Fail,About
OperatorID = ""
Line = ""
Site = ""
StarTTime = ""
StopTime = ""
TestResult = ""
Image = ""
MAC = ""
MAXFailLabel = ""
MAXProbeQTY = ""
FailLabel = []
FailMessage = []
MeasureLabel = []
MeasureData = []
MeasureMessage = []


def clean():
    SN = ""
    Customer = ""
    BoardStyle = ""
    TesterName = ""
    Process = ""
    FixtureSlot = ""
    Fixture = ""
    SoftwareDocument = ""
    SoftwareRevision = ""
    AssemblyNumber = ""
    AssemblyRevision = ""
    AssemblyVersion = ""
    FirmwareRevision = ""
    TestStatus = ""
    OperatorID = ""
    Line = ""
    Site = ""
    StarTTime = ""
    StopTime = ""
    TestResult = ""
    Image = ""
    MAC = ""
    MAXFailLabel = ""
    MAXProbeQTY = ""
    FailLabel = []
    FailMessage = []
    MeasureLabel = []
    MeasureData = []
    MeasureMessage = []

def print_alldata():
    print("SN=%s" %SN)
    print("Customer=%s" %Customer)
    print("BoardStyle=%s" %BoardStyle)
    print("TesterName=%s" %TesterName)
    print("Process=%s" %Process)
    print("FixtureSlot=%s" %FixtureSlot)
    print("Fixture=%s" %Fixture)
    print("SoftwareDocument=%s" %SoftwareDocument)
    print("SoftwareRevision=%s" %SoftwareRevision)
    print("AssemblyNumber=%s" %AssemblyNumber)
    print("AssemblyRevision=%s" %AssemblyRevision)
    print("AssemblyVersion=%s" %AssemblyVersion)
    print("FirmwareRevision=%s" %FirmwareRevision)
    print("TestStatus=%s" %TestStatus)
    print("OperatorID=%s" %OperatorID)
    print("Line=%s" %Line)
    print("Site=%s" %Site)
    print("StarTTime=%s" %StarTTime)
    print("StopTime=%s" %StopTime)
    print("TestResult=%s" %TestResult)
    print("Image=%s" %Image)
    print("MAC=%s" %MAC)
    print("MAXFailLabel=%s" %MAXFailLabel)
    print("MAXProbeQTY=%s" %MAXProbeQTY)
    print("FailLabel=%s" %FailLabel)
    print("FailMessage=%s" %FailMessage)
    print("MeasureLabel=%s" %MeasureLabel)
    print("MeasureData=%s" %MeasureData)
    print("MeasureMessage=%s" %MeasureMessage)

def make_test_data():
    SN = "9F001ABE4E7495DD6F2"
    Customer = "HP"
    BoardStyle = ""
    TesterName = "huahpict18"
    Process = "ICT"
    FixtureSlot = "1"
    Fixture = "0001"
    SoftwareDocument = "N/A"
    SoftwareRevision = "N/A"
    AssemblyNumber = "1PV64-60001"
    AssemblyRevision = "N/A"
    AssemblyVersion = "A5845.02"
    FirmwareRevision = "N/A"
    TestStatus = "Pass"
    OperatorID = "000057"
    Line = "Bay05"
    Site = "11"
    StarTTime = "181205205819"
    StopTime = "181205205916"
    TestResult = "P"
    Image = "1"
    MAC = ""
    MAXFailLabel = "50"
    MAXProbeQTY = "50"
    FailLabel = ["1%R1","2%C1"]
    FailMessage = []
    MeasureLabel = []
    MeasureData = []
    MeasureMessage = []


#Init()
#PrintAllData()
