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


def Clean():
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

def PrintAllData():
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


#Init()
#PrintAllData()
