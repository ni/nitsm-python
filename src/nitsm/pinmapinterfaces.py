# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)]
# From type library 'NationalInstruments.TestStand.SemiconductorModule.PinMapInterfaces.tlb'
# On Thu Jan 28 09:47:32 2021
'NI TestStand 2020 Semiconductor Module Pin Map Interfaces'
makepy_version = '0.5.01'
python_version = 0x30608f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{AC54E909-CA87-48AB-9935-A908E5DCB97B}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	PinMapErrorCode_MismatchedHistoryRamPinNames=1          # from enum PinMapErrorCode

from win32com.client import DispatchBaseClass
class IMeasurementPublisher(DispatchBaseClass):
	CLSID = IID('{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}')
	coclass_clsid = None

	def GetInputDataBoolean(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743815, LCID, 1, (11, 0), ((3, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, inputDataId)

	def GetInputDataDouble(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743814, LCID, 1, (5, 0), ((3, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, inputDataId)

	def GetInputDataString(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(1610743816, LCID, 1, (8, 0), ((3, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, inputDataId)

	def PublishBool(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743809, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (11, 1)),siteNumberParam
			, pin, publishedDataId, measurement)

	def PublishBoolToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743812, LCID, 1, (24, 0), ((3, 1), (8, 1), (11, 1)),siteNumber
			, expression, measurement)

	def PublishDouble(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743808, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (5, 1)),siteNumberParam
			, pin, publishedDataId, measurement)

	def PublishDoubleToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743811, LCID, 1, (24, 0), ((3, 1), (8, 1), (5, 1)),siteNumber
			, expression, measurement)

	def PublishString(self, siteNumberParam=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743810, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1), (8, 1)),siteNumberParam
			, pin, publishedDataId, measurement)

	def PublishStringToTestStandVariable(self, siteNumber=defaultNamedNotOptArg, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((3, 1), (8, 1), (8, 1)),siteNumber
			, expression, measurement)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentInstanceData(DispatchBaseClass):
	CLSID = IID('{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InstrumentModel": (1610743809, 2, (8, 0), (), "InstrumentModel", None),
		"instrumentName": (1610743808, 2, (8, 0), (), "instrumentName", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentProperty(DispatchBaseClass):
	CLSID = IID('{A8A78603-E18C-4BCB-A347-334AA757B4D5}')
	coclass_clsid = None

	_prop_map_get_ = {
		"PropertyName": (1610743808, 2, (8, 0), (), "PropertyName", None),
		"PropertyValue": (1610743809, 2, (8, 0), (), "PropertyValue", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentPropertyList(DispatchBaseClass):
	CLSID = IID('{3BFF2733-C91A-4590-899A-BE97B57C9EDE}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InstrumentModel": (1610743808, 2, (8, 0), (), "InstrumentModel", None),
		# Method 'Properties' returns object of type 'IModelBasedInstrumentProperty'
		"Properties": (1610743809, 2, (8201, 0), (), "Properties", '{A8A78603-E18C-4BCB-A347-334AA757B4D5}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IModelBasedInstrumentResourcePropertyList(DispatchBaseClass):
	CLSID = IID('{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}')
	coclass_clsid = None

	_prop_map_get_ = {
		"InstrumentResource": (1610743808, 2, (8, 0), (), "InstrumentResource", None),
		# Method 'Properties' returns object of type 'IModelBasedInstrumentProperty'
		"Properties": (1610743809, 2, (8201, 0), (), "Properties", '{A8A78603-E18C-4BCB-A347-334AA757B4D5}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISemiconductorModuleContext(DispatchBaseClass):
	'NI TestStand Semiconductor Module Pin Map'
	CLSID = IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')
	coclass_clsid = None

	def CreateMultisiteDataForAnalogOutput(self, perPinWaveform=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743864, 1, (8204, 0), ((8204, 1), (8, 1), (12, 1), (16387, 2)), 'CreateMultisiteDataForAnalogOutput', None,perPinWaveform
			, pin, idleValue, numberOfChannelsInTask)

	def CreateMultisiteDataForAnalogOutput_2(self, perPinWaveform=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743865, 1, (8204, 0), ((8204, 1), (8200, 1), (12, 1), (16387, 2)), 'CreateMultisiteDataForAnalogOutput_2', None,perPinWaveform
			, pins, idleValue, numberOfChannelsInTask)

	def CreatePerSiteMultisiteDataForAnalogOutput(self, sitePinWaveforms=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743866, 1, (8204, 0), ((8204, 1), (8, 1), (12, 1), (16387, 2)), 'CreatePerSiteMultisiteDataForAnalogOutput', None,sitePinWaveforms
			, pin, idleValue, numberOfChannelsInTask)

	def CreatePerSiteMultisiteDataForAnalogOutput_2(self, sitePinWaveforms=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, idleValue=defaultNamedNotOptArg, numberOfChannelsInTask=pythoncom.Missing):
		return self._ApplyTypes_(1610743867, 1, (8204, 0), ((8204, 1), (8200, 1), (12, 1), (16387, 2)), 'CreatePerSiteMultisiteDataForAnalogOutput_2', None,sitePinWaveforms
			, pins, idleValue, numberOfChannelsInTask)

	def ExtractPinData(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743946, 1, (8197, 0), ((8197, 1), (8200, 1), (8, 1)), 'ExtractPinData', None,data
			, pins, pin)

	def ExtractPinData_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743948, 1, (8197, 0), ((8197, 1), (8200, 1), (8, 1)), 'ExtractPinData_2', None,data
			, pins, pin)

	def ExtractPinData_3(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743949, 1, (8203, 0), ((8203, 1), (8200, 1), (8, 1)), 'ExtractPinData_3', None,data
			, pins, pin)

	def ExtractPinData_4(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743951, 1, (8203, 0), ((8203, 1), (8200, 1), (8, 1)), 'ExtractPinData_4', None,data
			, pins, pin)

	def FilterPinsByInstrumentType(self, pins=defaultNamedNotOptArg, instrumentTypeId=defaultNamedNotOptArg, capability=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743811, 1, (8200, 0), ((8200, 1), (8, 1), (8, 1)), 'FilterPinsByInstrumentType', None,pins
			, instrumentTypeId, capability)

	def GetAllInstrumentDefinitions(self, instrumentTypeId=defaultNamedNotOptArg, instrumentNames=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743812, 1, (24, 0), ((8, 1), (24584, 2), (24584, 2), (24584, 2)), 'GetAllInstrumentDefinitions', None,instrumentTypeId
			, instrumentNames, channelGroupIds, channelLists)

	def GetAllSessionData(self, instrumentTypeId=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelGroupIds=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743814, 1, (24, 0), ((8, 1), (24588, 2), (24584, 2), (24584, 2)), 'GetAllSessionData', None,instrumentTypeId
			, sessions, channelGroupIds, channelLists)

	def GetChannelGroupAndChannelIndex(self, pins=defaultNamedNotOptArg, numberOfPinsPerChannelGroup=pythoncom.Missing, channelGroupIndices=pythoncom.Missing, channelIndices=pythoncom.Missing):
		return self._ApplyTypes_(1610743818, 1, (24, 0), ((8200, 1), (24579, 2), (24579, 2), (24579, 2)), 'GetChannelGroupAndChannelIndex', None,pins
			, numberOfPinsPerChannelGroup, channelGroupIndices, channelIndices)

	def GetChannelGroupAndChannelIndex_2(self, pinsInLookup=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, siteNumber=defaultNamedNotOptArg, channelGroupIndex=pythoncom.Missing
			, channelIndex=pythoncom.Missing):
		return self._ApplyTypes_(1610743819, 1, (24, 0), ((8200, 1), (8, 1), (3, 1), (16387, 2), (16387, 2)), 'GetChannelGroupAndChannelIndex_2', None,pinsInLookup
			, pin, siteNumber, channelGroupIndex, channelIndex)

	def GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite(self, pinNames=defaultNamedNotOptArg, dataFirstDimensionLength=defaultNamedNotOptArg, numberOfChannelsPerTask=pythoncom.Missing):
		return self._ApplyTypes_(1610744056, 1, (8195, 0), ((8200, 1), (3, 1), (24579, 2)), 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite', None,pinNames
			, dataFirstDimensionLength, numberOfChannelsPerTask)

	def GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites(self, pinNames=defaultNamedNotOptArg, dataFirstDimensionLength=defaultNamedNotOptArg, numberOfChannelsPerTask=pythoncom.Missing):
		return self._ApplyTypes_(1610744055, 1, (8195, 0), ((8200, 1), (3, 1), (24579, 2)), 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites', None,pinNames
			, dataFirstDimensionLength, numberOfChannelsPerTask)

	def GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite(self, pinNames=defaultNamedNotOptArg, dataFirstDimensionLength=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744054, 1, (8195, 0), ((8200, 1), (3, 1)), 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite', None,pinNames
			, dataFirstDimensionLength)

	def GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites(self, pinNames=defaultNamedNotOptArg, dataFirstDimensionLength=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744053, 1, (8195, 0), ((8200, 1), (3, 1)), 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites', None,pinNames
			, dataFirstDimensionLength)

	def GetDigitalPatternProjectCaptureWaveformFilePaths(self):
		return self._ApplyTypes_(1610743975, 1, (8200, 0), (), 'GetDigitalPatternProjectCaptureWaveformFilePaths', None,)

	def GetDigitalPatternProjectLevelsFilePaths(self):
		return self._ApplyTypes_(1610743971, 1, (8200, 0), (), 'GetDigitalPatternProjectLevelsFilePaths', None,)

	def GetDigitalPatternProjectPatternFilePaths(self):
		return self._ApplyTypes_(1610743973, 1, (8200, 0), (), 'GetDigitalPatternProjectPatternFilePaths', None,)

	def GetDigitalPatternProjectSourceWaveformFilePaths(self):
		return self._ApplyTypes_(1610743974, 1, (8200, 0), (), 'GetDigitalPatternProjectSourceWaveformFilePaths', None,)

	def GetDigitalPatternProjectSpecificationsFilePaths(self):
		return self._ApplyTypes_(1610743970, 1, (8200, 0), (), 'GetDigitalPatternProjectSpecificationsFilePaths', None,)

	def GetDigitalPatternProjectTimingFilePaths(self):
		return self._ApplyTypes_(1610743972, 1, (8200, 0), (), 'GetDigitalPatternProjectTimingFilePaths', None,)

	def GetFPGAInstrumentNames(self, instrumentNames=pythoncom.Missing, fpgaFilePaths=pythoncom.Missing):
		return self._ApplyTypes_(1610743887, 1, (24, 0), ((24584, 2), (24584, 2)), 'GetFPGAInstrumentNames', None,instrumentNames
			, fpgaFilePaths)

	def GetFPGAVIReference(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743888, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetFPGAVIReferences(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743889, 1, (8213, 0), ((8, 1),), 'GetFPGAVIReferences', None,pin
			)

	def GetFPGAVIReferences_2(self):
		return self._ApplyTypes_(1610743890, 1, (8213, 0), (), 'GetFPGAVIReferences_2', None,)

	def GetGlobalData(self, dataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743944, 1, (12, 0), ((8, 1),), 'GetGlobalData', None,dataId
			)

	def GetInputDataBoolean(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743928, 1, (8203, 0), ((8, 1), (8, 1)), 'GetInputDataBoolean', None,pin
			, inputDataId)

	def GetInputDataDouble(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743929, 1, (8197, 0), ((8, 1), (8, 1)), 'GetInputDataDouble', None,pin
			, inputDataId)

	def GetInputDataString(self, pin=defaultNamedNotOptArg, inputDataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743930, 1, (8200, 0), ((8, 1), (8, 1)), 'GetInputDataString', None,pin
			, inputDataId)

	def GetInstrumentNameAndChannelForPinOnSingleSite(self, pinName=defaultNamedNotOptArg, instrumentName=pythoncom.Missing, channelOrPort=pythoncom.Missing):
		return self._ApplyTypes_(1610744050, 1, (24, 0), ((8, 1), (16392, 2), (16392, 2)), 'GetInstrumentNameAndChannelForPinOnSingleSite', None,pinName
			, instrumentName, channelOrPort)

	# Result is of type IModelBasedInstrumentInstanceData
	def GetModelBasedInstrumentNames(self, category=defaultNamedNotOptArg, subcategory=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744000, 1, (8201, 0), ((8, 1), (8, 1)), 'GetModelBasedInstrumentNames', '{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}',category
			, subcategory)

	# Result is of type IModelBasedInstrumentPropertyList
	def GetModelBasedInstrumentProperties(self, instrumentName=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610744001, LCID, 1, (9, 0), ((8, 1),),instrumentName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetModelBasedInstrumentProperties', '{3BFF2733-C91A-4590-899A-BE97B57C9EDE}')
		return ret

	def GetModelBasedInstrumentResourceNames(self, instrumentName=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743999, 1, (8200, 0), ((8, 1),), 'GetModelBasedInstrumentResourceNames', None,instrumentName
			)

	# Result is of type IModelBasedInstrumentResourcePropertyList
	def GetModelBasedInstrumentResourceProperties(self, instrumentName=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744002, 1, (8201, 0), ((8, 1),), 'GetModelBasedInstrumentResourceProperties', '{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}',instrumentName
			)

	def GetNI5530RFPortModuleNames(self, ni5530RFPortModuleNames=pythoncom.Missing, calibrationFilePaths=pythoncom.Missing):
		return self._ApplyTypes_(1610743908, 1, (24, 0), ((24584, 2), (24584, 2)), 'GetNI5530RFPortModuleNames', None,ni5530RFPortModuleNames
			, calibrationFilePaths)

	def GetNI5530RFPortModuleSessions(self, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing):
		return self._ApplyTypes_(1610743910, 1, (24, 0), ((24597, 2), (24597, 2)), 'GetNI5530RFPortModuleSessions', None,ni5530RFPortModuleSessions
			, calibrationSessions)

	def GetNI5530RFPortModuleSessions_2(self, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing
			, ni5530Channel1=pythoncom.Missing, ni5530Channel2=pythoncom.Missing):
		return self._ApplyTypes_(1610743911, 1, (24, 0), ((8, 1), (24585, 2), (24597, 2), (24597, 2), (24584, 2), (24584, 2)), 'GetNI5530RFPortModuleSessions_2', None,pin
			, semiconductorModuleContexts, ni5530RFPortModuleSessions, calibrationSessions, ni5530Channel1, ni5530Channel2
			)

	def GetNI5530RFPortModuleSessions_3(self, pins=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, ni5530RFPortModuleSessions=pythoncom.Missing, calibrationSessions=pythoncom.Missing
			, ni5530Channel1=pythoncom.Missing, ni5530Channel2=pythoncom.Missing):
		return self._ApplyTypes_(1610743912, 1, (24, 0), ((8200, 1), (24585, 2), (24597, 2), (24597, 2), (24584, 2), (24584, 2)), 'GetNI5530RFPortModuleSessions_3', None,pins
			, semiconductorModuleContexts, ni5530RFPortModuleSessions, calibrationSessions, ni5530Channel1, ni5530Channel2
			)

	def GetNIDAQmxTask(self, pin=defaultNamedNotOptArg, task=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743860, 1, (24, 0), ((8, 1), (16396, 2), (16392, 2)), 'GetNIDAQmxTask', None,pin
			, task, channelList)

	def GetNIDAQmxTaskNames(self, taskType=defaultNamedNotOptArg, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743857, 1, (8200, 0), ((8, 1), (24584, 2)), 'GetNIDAQmxTaskNames', None,taskType
			, channelLists)

	def GetNIDAQmxTask_2(self, pins=defaultNamedNotOptArg, task=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743861, 1, (24, 0), ((8200, 1), (16396, 2), (16392, 2)), 'GetNIDAQmxTask_2', None,pins
			, task, channelList)

	def GetNIDAQmxTasks(self, taskType=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743859, 1, (8204, 0), ((8, 1),), 'GetNIDAQmxTasks', None,taskType
			)

	def GetNIDAQmxTasks_2(self, pin=defaultNamedNotOptArg, tasks=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743862, 1, (24, 0), ((8, 1), (24588, 2), (24584, 2)), 'GetNIDAQmxTasks_2', None,pin
			, tasks, channelLists)

	def GetNIDAQmxTasks_3(self, pins=defaultNamedNotOptArg, tasks=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743863, 1, (24, 0), ((8200, 1), (24588, 2), (24584, 2)), 'GetNIDAQmxTasks_3', None,pins
			, tasks, channelLists)

	def GetNIDCPowerAlarmSession(self, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744048, LCID, 1, (21, 0), ((21, 1),),session
			)

	def GetNIDCPowerInstrumentNames(self, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743821, 1, (8200, 0), ((24584, 2),), 'GetNIDCPowerInstrumentNames', None,channelLists
			)

	def GetNIDCPowerResourceStrings(self):
		return self._ApplyTypes_(1610744040, 1, (8200, 0), (), 'GetNIDCPowerResourceStrings', None,)

	def GetNIDCPowerSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743826, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIDCPowerSession', None,pin
			, session, channelList)

	def GetNIDCPowerSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610744042, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIDCPowerSession_2', None,pins
			, session, channelList)

	def GetNIDCPowerSessions(self):
		return self._ApplyTypes_(1610743823, 1, (8213, 0), (), 'GetNIDCPowerSessions', None,)

	def GetNIDCPowerSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743824, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIDCPowerSessions_2', None,pin
			, sessions, channelLists)

	def GetNIDCPowerSessions_3(self, pins=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743825, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIDCPowerSessions_3', None,pins
			, sessions, channelLists)

	def GetNIDigitalPatternInstrumentNames(self):
		return self._ApplyTypes_(1610743952, 1, (8200, 0), (), 'GetNIDigitalPatternInstrumentNames', None,)

	def GetNIDigitalPatternSession(self, pinNames=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing, siteList=pythoncom.Missing):
		return self._ApplyTypes_(1610743994, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2), (16392, 2)), 'GetNIDigitalPatternSession', None,pinNames
			, session, channelList, siteList)

	def GetNIDigitalPatternSession_2(self, pinName=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing, siteList=pythoncom.Missing):
		return self._ApplyTypes_(1610743995, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2), (16392, 2)), 'GetNIDigitalPatternSession_2', None,pinName
			, session, channelList, siteList)

	def GetNIDigitalPatternSessions(self):
		return self._ApplyTypes_(1610743953, 1, (8213, 0), (), 'GetNIDigitalPatternSessions', None,)

	def GetNIDigitalPatternSessions_2(self, pinNames=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing, siteLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743955, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2), (24584, 2)), 'GetNIDigitalPatternSessions_2', None,pinNames
			, sessions, channelLists, siteLists)

	def GetNIDigitalPatternSessions_3(self, pinName=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing, siteLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743956, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2), (24584, 2)), 'GetNIDigitalPatternSessions_3', None,pinName
			, sessions, channelLists, siteLists)

	def GetNIDmmInstrumentNames(self):
		return self._ApplyTypes_(1610743837, 1, (8200, 0), (), 'GetNIDmmInstrumentNames', None,)

	def GetNIDmmSession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743840, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIDmmSessions(self):
		return self._ApplyTypes_(1610743839, 1, (8213, 0), (), 'GetNIDmmSessions', None,)

	def GetNIDmmSessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743841, 1, (8213, 0), ((8, 1),), 'GetNIDmmSessions_2', None,pin
			)

	def GetNIDmmSessions_3(self, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743842, 1, (8213, 0), ((8200, 1),), 'GetNIDmmSessions_3', None,pins
			)

	def GetNIFGenInstrumentNames(self):
		return self._ApplyTypes_(1610743850, 1, (8200, 0), (), 'GetNIFGenInstrumentNames', None,)

	def GetNIFGenSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743853, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIFGenSession', None,pin
			, session, channelList)

	def GetNIFGenSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743855, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIFGenSession_2', None,pins
			, session, channelList)

	def GetNIFGenSessions(self):
		return self._ApplyTypes_(1610743852, 1, (8213, 0), (), 'GetNIFGenSessions', None,)

	def GetNIFGenSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743854, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIFGenSessions_2', None,pin
			, sessions, channelLists)

	def GetNIFGenSessions_3(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743856, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIFGenSessions_3', None,pins
			, session, channelLists)

	def GetNIHSDIOChannelMasks(self, pins=defaultNamedNotOptArg, masks=pythoncom.Missing):
		return self._ApplyTypes_(1610743834, 1, (24, 0), ((8200, 1), (24595, 2)), 'GetNIHSDIOChannelMasks', None,pins
			, masks)

	def GetNIHSDIOChannelMasks_2(self, pins=defaultNamedNotOptArg, masks=pythoncom.Missing):
		return self._ApplyTypes_(1610743835, 1, (24, 0), ((8200, 1), (24595, 2)), 'GetNIHSDIOChannelMasks_2', None,pins
			, masks)

	def GetNIHSDIOInstrumentNames(self):
		return self._ApplyTypes_(1610743827, 1, (8200, 0), (), 'GetNIHSDIOInstrumentNames', None,)

	def GetNIHSDIOSession(self, pin=defaultNamedNotOptArg, acquisitionSession=pythoncom.Missing, generationSession=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743832, 1, (24, 0), ((8, 1), (16405, 2), (16405, 2), (16392, 2)), 'GetNIHSDIOSession', None,pin
			, acquisitionSession, generationSession, channelList)

	def GetNIHSDIOSession_2(self, pins=defaultNamedNotOptArg, acquisitionSession=pythoncom.Missing, generationSession=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743833, 1, (24, 0), ((8200, 1), (16405, 2), (16405, 2), (16392, 2)), 'GetNIHSDIOSession_2', None,pins
			, acquisitionSession, generationSession, channelList)

	def GetNIHSDIOSessions(self, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing):
		return self._ApplyTypes_(1610743829, 1, (24, 0), ((24597, 2), (24597, 2)), 'GetNIHSDIOSessions', None,acquisitionSessions
			, generationSessions)

	def GetNIHSDIOSessions_2(self, pin=defaultNamedNotOptArg, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743830, 1, (24, 0), ((8, 1), (24597, 2), (24597, 2), (24584, 2)), 'GetNIHSDIOSessions_2', None,pin
			, acquisitionSessions, generationSessions, channelLists)

	def GetNIHSDIOSessions_3(self, pins=defaultNamedNotOptArg, acquisitionSessions=pythoncom.Missing, generationSessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743831, 1, (24, 0), ((8200, 1), (24597, 2), (24597, 2), (24584, 2)), 'GetNIHSDIOSessions_3', None,pins
			, acquisitionSessions, generationSessions, channelLists)

	def GetNIRFPMDeembeddingDataForDutPins(self, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743901, 1, (24, 0), ((24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMDeembeddingDataForDutPins', None,sessions
			, portLists, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFPMDeembeddingDataForSystemPins(self, sessions=pythoncom.Missing, portLists=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743903, 1, (24, 0), ((24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMDeembeddingDataForSystemPins', None,sessions
			, portLists, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFPMInstrumentNames(self, instrumentNames=pythoncom.Missing, calibrationFilePaths=pythoncom.Missing, iviSwitchNames=pythoncom.Missing, fpgaFilePaths=pythoncom.Missing):
		return self._ApplyTypes_(1610743892, 1, (24, 0), ((24584, 2), (24584, 2), (24584, 2), (24584, 2)), 'GetNIRFPMInstrumentNames', None,instrumentNames
			, calibrationFilePaths, iviSwitchNames, fpgaFilePaths)

	def GetNIRFPMSession(self, systemPin=defaultNamedNotOptArg, session=pythoncom.Missing, port=pythoncom.Missing, deembeddingFilePath=pythoncom.Missing
			, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610743896, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2), (16392, 2), (16387, 2)), 'GetNIRFPMSession', None,systemPin
			, session, port, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFPMSessions(self):
		return self._ApplyTypes_(1610743894, 1, (8213, 0), (), 'GetNIRFPMSessions', None,)

	def GetNIRFPMSessions_2(self, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portList=pythoncom.Missing
			, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743895, 1, (24, 0), ((8, 1), (24585, 2), (24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMSessions_2', None,pin
			, semiconductorModuleContexts, sessions, portList, deembeddingFilePaths, deembeddingOrientations
			)

	def GetNIRFPMSessions_3(self, pin1=defaultNamedNotOptArg, pin2=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing
			, portLists1=pythoncom.Missing, portLists2=pythoncom.Missing, deembeddingFilePaths1=pythoncom.Missing, deembeddingFilePaths2=pythoncom.Missing, deembeddingOrientations1=pythoncom.Missing
			, deembeddingOrientations2=pythoncom.Missing):
		return self._ApplyTypes_(1610743897, 1, (24, 0), ((8, 1), (8, 1), (24585, 2), (24597, 2), (24584, 2), (24584, 2), (24584, 2), (24584, 2), (24579, 2), (24579, 2)), 'GetNIRFPMSessions_3', None,pin1
			, pin2, semiconductorModuleContexts, sessions, portLists1, portLists2
			, deembeddingFilePaths1, deembeddingFilePaths2, deembeddingOrientations1, deembeddingOrientations2)

	def GetNIRFPMSessions_4(self, pins=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, sessions=pythoncom.Missing, portLists=pythoncom.Missing
			, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743898, 1, (24, 0), ((8200, 1), (24585, 2), (24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMSessions_4', None,pins
			, semiconductorModuleContexts, sessions, portLists, deembeddingFilePaths, deembeddingOrientations
			)

	def GetNIRFPMSessions_5(self, systemPins=defaultNamedNotOptArg, sessions=pythoncom.Missing, portList=pythoncom.Missing, deembeddingFilePaths=pythoncom.Missing
			, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610743900, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2), (24584, 2), (24579, 2)), 'GetNIRFPMSessions_5', None,systemPins
			, sessions, portList, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFSADeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610744027, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), 'GetNIRFSADeembeddingData', None,pin
			, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFSADeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610744028, 1, (24, 0), ((8, 1), (24584, 2), (24579, 2)), 'GetNIRFSADeembeddingData_2', None,pin
			, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFSAInstrumentNames(self):
		return self._ApplyTypes_(1610743872, 1, (8200, 0), (), 'GetNIRFSAInstrumentNames', None,)

	def GetNIRFSASession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743875, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIRFSASession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing):
		return self._ApplyTypes_(1610744021, 1, (21, 0), ((8, 1), (16392, 2)), 'GetNIRFSASession_2', None,pin
			, port)

	def GetNIRFSASessions(self):
		return self._ApplyTypes_(1610743874, 1, (8213, 0), (), 'GetNIRFSASessions', None,)

	def GetNIRFSASessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743876, 1, (8213, 0), ((8, 1),), 'GetNIRFSASessions_2', None,pin
			)

	def GetNIRFSASessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing):
		return self._ApplyTypes_(1610744022, 1, (8213, 0), ((8, 1), (24584, 2)), 'GetNIRFSASessions_3', None,pin
			, ports)

	def GetNIRFSGDeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610744029, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), 'GetNIRFSGDeembeddingData', None,pin
			, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFSGDeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610744030, 1, (24, 0), ((8, 1), (24584, 2), (24579, 2)), 'GetNIRFSGDeembeddingData_2', None,pin
			, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFSGInstrumentNames(self):
		return self._ApplyTypes_(1610743882, 1, (8200, 0), (), 'GetNIRFSGInstrumentNames', None,)

	def GetNIRFSGSession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743885, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIRFSGSession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing):
		return self._ApplyTypes_(1610744023, 1, (21, 0), ((8, 1), (16392, 2)), 'GetNIRFSGSession_2', None,pin
			, port)

	def GetNIRFSGSessions(self):
		return self._ApplyTypes_(1610743884, 1, (8213, 0), (), 'GetNIRFSGSessions', None,)

	def GetNIRFSGSessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743886, 1, (8213, 0), ((8, 1),), 'GetNIRFSGSessions_2', None,pin
			)

	def GetNIRFSGSessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing):
		return self._ApplyTypes_(1610744024, 1, (8213, 0), ((8, 1), (24584, 2)), 'GetNIRFSGSessions_3', None,pin
			, ports)

	def GetNIRFmxDeembeddingData(self, pin=defaultNamedNotOptArg, deembeddingFilePath=pythoncom.Missing, deembeddingOrientation=pythoncom.Missing):
		return self._ApplyTypes_(1610744025, 1, (24, 0), ((8, 1), (16392, 2), (16387, 2)), 'GetNIRFmxDeembeddingData', None,pin
			, deembeddingFilePath, deembeddingOrientation)

	def GetNIRFmxDeembeddingData_2(self, pin=defaultNamedNotOptArg, deembeddingFilePaths=pythoncom.Missing, deembeddingOrientations=pythoncom.Missing):
		return self._ApplyTypes_(1610744026, 1, (24, 0), ((8, 1), (24584, 2), (24579, 2)), 'GetNIRFmxDeembeddingData_2', None,pin
			, deembeddingFilePaths, deembeddingOrientations)

	def GetNIRFmxInstrumentNames(self):
		return self._ApplyTypes_(1610743877, 1, (8200, 0), (), 'GetNIRFmxInstrumentNames', None,)

	def GetNIRFmxSession(self, pin=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743880, LCID, 1, (21, 0), ((8, 1),),pin
			)

	def GetNIRFmxSession_2(self, pin=defaultNamedNotOptArg, port=pythoncom.Missing):
		return self._ApplyTypes_(1610744019, 1, (21, 0), ((8, 1), (16392, 2)), 'GetNIRFmxSession_2', None,pin
			, port)

	def GetNIRFmxSessions(self):
		return self._ApplyTypes_(1610743879, 1, (8213, 0), (), 'GetNIRFmxSessions', None,)

	def GetNIRFmxSessions_2(self, pin=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743881, 1, (8213, 0), ((8, 1),), 'GetNIRFmxSessions_2', None,pin
			)

	def GetNIRFmxSessions_3(self, pin=defaultNamedNotOptArg, ports=pythoncom.Missing):
		return self._ApplyTypes_(1610744020, 1, (8213, 0), ((8, 1), (24584, 2)), 'GetNIRFmxSessions_3', None,pin
			, ports)

	def GetNIRelayDriverModuleNames(self):
		return self._ApplyTypes_(1610743978, 1, (8200, 0), (), 'GetNIRelayDriverModuleNames', None,)

	def GetNIRelayDriverSession(self, relay=defaultNamedNotOptArg, niSwitchSession=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743981, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIRelayDriverSession', None,relay
			, niSwitchSession, niSwitchRelayNames)

	def GetNIRelayDriverSession_2(self, relays=defaultNamedNotOptArg, niSwitchSession=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743982, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIRelayDriverSession_2', None,relays
			, niSwitchSession, niSwitchRelayNames)

	def GetNIRelayDriverSessions(self):
		return self._ApplyTypes_(1610743980, 1, (8213, 0), (), 'GetNIRelayDriverSessions', None,)

	def GetNIRelayDriverSessions_2(self, relay=defaultNamedNotOptArg, niSwitchSessions=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743983, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIRelayDriverSessions_2', None,relay
			, niSwitchSessions, niSwitchRelayNames)

	def GetNIRelayDriverSessions_3(self, relays=defaultNamedNotOptArg, niSwitchSessions=pythoncom.Missing, niSwitchRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743984, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIRelayDriverSessions_3', None,relays
			, niSwitchSessions, niSwitchRelayNames)

	def GetNIScopeInstrumentNames(self):
		return self._ApplyTypes_(1610743843, 1, (8200, 0), (), 'GetNIScopeInstrumentNames', None,)

	def GetNIScopeSession(self, pin=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743846, 1, (24, 0), ((8, 1), (16405, 2), (16392, 2)), 'GetNIScopeSession', None,pin
			, session, channelList)

	def GetNIScopeSession_2(self, pins=defaultNamedNotOptArg, session=pythoncom.Missing, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743848, 1, (24, 0), ((8200, 1), (16405, 2), (16392, 2)), 'GetNIScopeSession_2', None,pins
			, session, channelList)

	def GetNIScopeSessions(self):
		return self._ApplyTypes_(1610743845, 1, (8213, 0), (), 'GetNIScopeSessions', None,)

	def GetNIScopeSessions_2(self, pin=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743847, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2)), 'GetNIScopeSessions_2', None,pin
			, sessions, channelLists)

	def GetNIScopeSessions_3(self, pins=defaultNamedNotOptArg, sessions=pythoncom.Missing, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743849, 1, (24, 0), ((8200, 1), (24597, 2), (24584, 2)), 'GetNIScopeSessions_3', None,pins
			, sessions, channelLists)

	def GetPinNames(self, instrumentTypeId=defaultNamedNotOptArg, capability=defaultNamedNotOptArg, dutPinNames=pythoncom.Missing, systemPinNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743810, 1, (24, 0), ((8, 1), (8, 1), (24584, 2), (24584, 2)), 'GetPinNames', None,instrumentTypeId
			, capability, dutPinNames, systemPinNames)

	def GetRelayDriverSessionsFromRelayConfiguration(self, configurationName=defaultNamedNotOptArg, sessionsForRelaysInOpenState=pythoncom.Missing, niSwitchRelayNamesForRelaysInOpenState=pythoncom.Missing, sessionsForRelaysInClosedState=pythoncom.Missing
			, niSwitchRelayNamesForRelaysInClosedState=pythoncom.Missing):
		return self._ApplyTypes_(1610744003, 1, (24, 0), ((8, 1), (24597, 2), (24584, 2), (24597, 2), (24584, 2)), 'GetRelayDriverSessionsFromRelayConfiguration', None,configurationName
			, sessionsForRelaysInOpenState, niSwitchRelayNamesForRelaysInOpenState, sessionsForRelaysInClosedState, niSwitchRelayNamesForRelaysInClosedState)

	def GetRelayDriverSessionsFromRelays(self, relayNames=defaultNamedNotOptArg, switchRelayActionsAsIntegerArray=defaultNamedNotOptArg, sessionsForRelaysInOpenState=pythoncom.Missing, niSwitchRelayNamesForRelaysInOpenState=pythoncom.Missing
			, sessionsForRelaysInClosedState=pythoncom.Missing, niSwitchRelayNamesForRelaysInClosedState=pythoncom.Missing):
		return self._ApplyTypes_(1610744032, 1, (24, 0), ((8200, 1), (8195, 1), (24597, 2), (24584, 2), (24597, 2), (24584, 2)), 'GetRelayDriverSessionsFromRelays', None,relayNames
			, switchRelayActionsAsIntegerArray, sessionsForRelaysInOpenState, niSwitchRelayNamesForRelaysInOpenState, sessionsForRelaysInClosedState, niSwitchRelayNamesForRelaysInClosedState
			)

	def GetRelayNames(self, siteRelayNames=pythoncom.Missing, systemRelayNames=pythoncom.Missing):
		return self._ApplyTypes_(1610743989, 1, (24, 0), ((24584, 2), (24584, 2)), 'GetRelayNames', None,siteRelayNames
			, systemRelayNames)

	def GetRelaysInRelayGroups(self, relayGroups=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743990, 1, (8200, 0), ((8200, 1),), 'GetRelaysInRelayGroups', None,relayGroups
			)

	# Result is of type ISemiconductorModuleContext
	def GetSemiconductorModuleContextWithSites(self, SiteNumbers=defaultNamedNotOptArg):
		ret = self._oleobj_.InvokeTypes(1610744033, LCID, 1, (9, 0), ((8195, 1),),SiteNumbers
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSemiconductorModuleContextWithSites', '{3976D65A-5A34-45FC-B30D-79C4A601C537}')
		return ret

	def GetSessionData(self, instrumentTypeId=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, sessionData=pythoncom.Missing, channelGroupIds=pythoncom.Missing
			, channelLists=pythoncom.Missing):
		return self._ApplyTypes_(1610743815, 1, (24, 0), ((8, 1), (8200, 1), (24588, 2), (24584, 2), (24584, 2)), 'GetSessionData', None,instrumentTypeId
			, pins, sessionData, channelGroupIds, channelLists)

	def GetSessionData_2(self, instrumentTypeId=defaultNamedNotOptArg, pins=defaultNamedNotOptArg, sessionData=pythoncom.Missing, channelGroupId=pythoncom.Missing
			, channelList=pythoncom.Missing):
		return self._ApplyTypes_(1610743816, 1, (24, 0), ((8, 1), (8200, 1), (16396, 2), (16392, 2), (16392, 2)), 'GetSessionData_2', None,instrumentTypeId
			, pins, sessionData, channelGroupId, channelList)

	def GetSiteData(self, dataId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743942, 1, (8204, 0), ((8, 1),), 'GetSiteData', None,dataId
			)

	# Result is of type ISemiconductorModuleContext
	def GetSiteSemiconductorModuleContexts(self):
		return self._ApplyTypes_(1610743817, 1, (8201, 0), (), 'GetSiteSemiconductorModuleContexts', '{3976D65A-5A34-45FC-B30D-79C4A601C537}',)

	def GetSpecValue(self, symbol=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743932, LCID, 1, (5, 0), ((8, 1),),symbol
			)

	def GetSpecValues(self, symbols=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743931, 1, (8197, 0), ((8200, 1),), 'GetSpecValues', None,symbols
			)

	def GetSupportedAlarmNames(self, resourceString=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744043, 1, (8200, 0), ((8, 1),), 'GetSupportedAlarmNames', None,resourceString
			)

	def GetSwitchNames(self, switchTypeId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743904, 1, (8200, 0), ((8, 1),), 'GetSwitchNames', None,switchTypeId
			)

	def GetSwitchSessions(self, switchTypeId=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743906, 1, (8204, 0), ((8, 1),), 'GetSwitchSessions', None,switchTypeId
			)

	def GetSwitchSessions_2(self, switchTypeId=defaultNamedNotOptArg, pin=defaultNamedNotOptArg, semiconductorModuleContexts=pythoncom.Missing, switchSessions=pythoncom.Missing
			, switchRoute=pythoncom.Missing):
		return self._ApplyTypes_(1610743907, 1, (24, 0), ((8, 1), (8, 1), (24585, 2), (24588, 2), (24584, 2)), 'GetSwitchSessions_2', None,switchTypeId
			, pin, semiconductorModuleContexts, switchSessions, switchRoute)

	def GlobalDataExists(self, dataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743992, LCID, 1, (11, 0), ((8, 1),),dataId
			)

	def PerInstrumentToPerSiteData(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744012, 1, (8197, 0), ((8197, 1), (8200, 1)), 'PerInstrumentToPerSiteData', None,data
			, pins)

	def PerInstrumentToPerSiteData2D(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744013, 1, (8197, 0), ((8197, 1), (8200, 1)), 'PerInstrumentToPerSiteData2D', None,data
			, pins)

	def PerInstrumentToPerSiteData2D_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744015, 1, (8203, 0), ((8203, 1), (8200, 1)), 'PerInstrumentToPerSiteData2D_2', None,data
			, pins)

	def PerInstrumentToPerSiteData_2(self, data=defaultNamedNotOptArg, pins=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610744014, 1, (8203, 0), ((8203, 1), (8200, 1)), 'PerInstrumentToPerSiteData_2', None,data
			, pins)

	def PerInstrumentToPerSitePatternResults(self, pins=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743998, 1, (8203, 0), ((8200, 1), (8203, 1)), 'PerInstrumentToPerSitePatternResults', None,pins
			, patternResults)

	def PerInstrumentToPerSiteWaveforms(self, pins=defaultNamedNotOptArg, instrumentWaveforms=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743959, 1, (8211, 0), ((8200, 1), (8211, 1)), 'PerInstrumentToPerSiteWaveforms', None,pins
			, instrumentWaveforms)

	def PerSiteToPerInstrumentWaveforms(self, pins=defaultNamedNotOptArg, perSiteWaveforms=defaultNamedNotOptArg):
		return self._ApplyTypes_(1610743960, 1, (8211, 0), ((8200, 1), (8211, 1)), 'PerSiteToPerInstrumentWaveforms', None,pins
			, perSiteWaveforms)

	def Publish(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743913, LCID, 1, (24, 0), ((8, 1), (8, 1), (8197, 1)),pin
			, publishedDataId, measurements)

	def PublishHistoryRamCycleInformation(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, sessionIndex=defaultNamedNotOptArg, siteIndex=defaultNamedNotOptArg
			, patternName=defaultNamedNotOptArg, timeSetName=defaultNamedNotOptArg, vectorNumber=defaultNamedNotOptArg, cycleNumber=defaultNamedNotOptArg, expectedPinStates=defaultNamedNotOptArg
			, actualPinStates=defaultNamedNotOptArg, perPinPassFail=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744018, LCID, 1, (24, 0), ((8200, 1), (8, 1), (3, 1), (3, 1), (8, 1), (8, 1), (20, 1), (20, 1), (8209, 1), (8209, 1), (8203, 1)),pins
			, publishedDataId, sessionIndex, siteIndex, patternName, timeSetName
			, vectorNumber, cycleNumber, expectedPinStates, actualPinStates, perPinPassFail
			)

	def PublishPatternResults(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743958, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, patternResults)

	def PublishPatternResults_2(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, patternResults=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743996, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, patternResults)

	def PublishPerSite(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744004, LCID, 1, (24, 0), ((8, 1), (8, 1), (8197, 1)),pin
			, publishedDataId, measurements)

	def PublishPerSite_2(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744005, LCID, 1, (24, 0), ((8, 1), (8, 1), (8203, 1)),pin
			, publishedDataId, measurements)

	def PublishPerSite_3(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744006, LCID, 1, (24, 0), ((8, 1), (8, 1), (8200, 1)),pin
			, publishedDataId, measurements)

	def PublishPerSite_4(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744009, LCID, 1, (24, 0), ((8, 1), (8, 1), (5, 1)),pin
			, publishedDataId, measurement)

	def PublishPerSite_5(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744010, LCID, 1, (24, 0), ((8, 1), (8, 1), (11, 1)),pin
			, publishedDataId, measurement)

	def PublishPerSite_6(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744011, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1)),pin
			, publishedDataId, measurement)

	def PublishPinNamesForHistoryRamCycleInformation(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, pinNames=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744017, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8200, 1)),pins
			, publishedDataId, pinNames)

	def PublishToTestStandVariablePerSite(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744034, LCID, 1, (24, 0), ((8, 1), (8197, 1)),expression
			, measurements)

	def PublishToTestStandVariablePerSite_2(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744035, LCID, 1, (24, 0), ((8, 1), (8203, 1)),expression
			, measurements)

	def PublishToTestStandVariablePerSite_3(self, expression=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744036, LCID, 1, (24, 0), ((8, 1), (8200, 1)),expression
			, measurements)

	def PublishToTestStandVariablePerSite_4(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744037, LCID, 1, (24, 0), ((8, 1), (5, 1)),expression
			, measurement)

	def PublishToTestStandVariablePerSite_5(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744038, LCID, 1, (24, 0), ((8, 1), (11, 1)),expression
			, measurement)

	def PublishToTestStandVariablePerSite_6(self, expression=defaultNamedNotOptArg, measurement=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744039, LCID, 1, (24, 0), ((8, 1), (8, 1)),expression
			, measurement)

	def Publish_10(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743926, LCID, 1, (24, 0), ((8, 1), (8197, 1)),publishedDataId
			, measurements)

	def Publish_11(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743927, LCID, 1, (24, 0), ((8, 1), (8200, 1)),publishedDataId
			, measurements)

	def Publish_2(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743914, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8197, 1)),pins
			, publishedDataId, measurements)

	def Publish_3(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743915, LCID, 1, (24, 0), ((8, 1), (8, 1), (8197, 1)),pin
			, publishedDataId, measurements)

	def Publish_4(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743917, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8197, 1)),pins
			, publishedDataId, measurements)

	def Publish_5(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743919, LCID, 1, (24, 0), ((8, 1), (8, 1), (8203, 1)),pin
			, publishedDataId, measurements)

	def Publish_6(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743920, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, measurements)

	def Publish_7(self, pin=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743921, LCID, 1, (24, 0), ((8, 1), (8, 1), (8203, 1)),pin
			, publishedDataId, measurements)

	def Publish_8(self, pins=defaultNamedNotOptArg, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743923, LCID, 1, (24, 0), ((8200, 1), (8, 1), (8203, 1)),pins
			, publishedDataId, measurements)

	def Publish_9(self, publishedDataId=defaultNamedNotOptArg, measurements=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743925, LCID, 1, (24, 0), ((8, 1), (8203, 1)),publishedDataId
			, measurements)

	def ReportError(self, errorCode=defaultNamedNotOptArg, parameters=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744031, LCID, 1, (24, 0), ((3, 1), (8200, 1)),errorCode
			, parameters)

	def ReportIncompatibleArrayLengths(self, arrayParameterName1=defaultNamedNotOptArg, arrayParameterName2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743986, LCID, 1, (24, 0), ((8, 1), (8, 1)),arrayParameterName1
			, arrayParameterName2)

	def ReportInvalidArray(self, parameterName=defaultNamedNotOptArg, elementType=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743985, LCID, 1, (24, 0), ((8, 1), (8, 1)),parameterName
			, elementType)

	def ReportInvalidTimeToWait(self, parameterName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743987, LCID, 1, (24, 0), ((8, 1),),parameterName
			)

	def ReportMissingDriver(self, driverName=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743988, LCID, 1, (24, 0), ((8, 1),),driverName
			)

	def ReportUnsupportedCapability(self, capability=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743976, LCID, 1, (24, 0), ((8, 1),),capability
			)

	def SetFPGAVIReference(self, instrumentName=defaultNamedNotOptArg, fpgaVIReference=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743891, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, fpgaVIReference)

	def SetGlobalData(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743945, LCID, 1, (24, 0), ((8, 1), (12, 1)),dataId
			, data)

	def SetNI5530RFPortModuleSession(self, ni5530RFPortModuleName=defaultNamedNotOptArg, ni5530RFPortModuleSession=defaultNamedNotOptArg, calibrationSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743909, LCID, 1, (24, 0), ((8, 1), (21, 1), (21, 1)),ni5530RFPortModuleName
			, ni5530RFPortModuleSession, calibrationSession)

	def SetNIDAQmxTask(self, taskName=defaultNamedNotOptArg, task=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743858, LCID, 1, (24, 0), ((8, 1), (12, 1)),taskName
			, task)

	def SetNIDCPowerSession(self, instrumentName=defaultNamedNotOptArg, channelId=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743822, LCID, 1, (24, 0), ((8, 1), (8, 1), (21, 1)),instrumentName
			, channelId, session)

	def SetNIDCPowerSession_2(self, resourceString=defaultNamedNotOptArg, session=defaultNamedNotOptArg, alarmNames=defaultNamedNotOptArg, alarmSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744041, LCID, 1, (24, 0), ((8, 1), (21, 1), (8200, 1), (21, 1)),resourceString
			, session, alarmNames, alarmSession)

	def SetNIDCPowerSession_3(self, instrumentName=defaultNamedNotOptArg, channelId=defaultNamedNotOptArg, session=defaultNamedNotOptArg, alarmNames=defaultNamedNotOptArg
			, alarmSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744044, LCID, 1, (24, 0), ((8, 1), (8, 1), (21, 1), (8200, 1), (21, 1)),instrumentName
			, channelId, session, alarmNames, alarmSession)

	def SetNIDigitalPatternSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743954, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, session)

	def SetNIDmmSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743838, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIFGenSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743851, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, session)

	def SetNIHSDIOSessions(self, instrumentName=defaultNamedNotOptArg, acquisitionSession=defaultNamedNotOptArg, generationSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743828, LCID, 1, (24, 0), ((8, 1), (21, 1), (21, 1)),instrumentName
			, acquisitionSession, generationSession)

	def SetNIRFPMSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743893, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRFSASession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743873, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRFSGSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743883, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRFmxSession(self, instrumentName=defaultNamedNotOptArg, instrumentSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743878, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, instrumentSession)

	def SetNIRelayDriverSession(self, relayDriverName=defaultNamedNotOptArg, niSwitchSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743979, LCID, 1, (24, 0), ((8, 1), (21, 1)),relayDriverName
			, niSwitchSession)

	def SetNIScopeSession(self, instrumentName=defaultNamedNotOptArg, session=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743844, LCID, 1, (24, 0), ((8, 1), (21, 1)),instrumentName
			, session)

	def SetSessionData(self, instrumentTypeId=defaultNamedNotOptArg, instrumentName=defaultNamedNotOptArg, channelGroupId=defaultNamedNotOptArg, sessionData=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743813, LCID, 1, (24, 0), ((8, 1), (8, 1), (8, 1), (12, 1)),instrumentTypeId
			, instrumentName, channelGroupId, sessionData)

	def SetSiteData(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743943, LCID, 1, (24, 0), ((8, 1), (8204, 1)),dataId
			, data)

	def SetSiteData_2(self, dataId=defaultNamedNotOptArg, data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610744008, LCID, 1, (24, 0), ((8, 1), (8204, 1)),dataId
			, data)

	def SetSwitchSession(self, switchTypeId=defaultNamedNotOptArg, switchName=defaultNamedNotOptArg, switchSession=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743905, LCID, 1, (24, 0), ((8, 1), (8, 1), (12, 1)),switchTypeId
			, switchName, switchSession)

	def SiteDataExists(self, dataId=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(1610743991, LCID, 1, (11, 0), ((8, 1),),dataId
			)

	_prop_map_get_ = {
		"IsSemiconductorModuleInOfflineMode": (1610743993, 2, (11, 0), (), "IsSemiconductorModuleInOfflineMode", None),
		# Method 'MeasurementPublisher' returns object of type 'IMeasurementPublisher'
		"MeasurementPublisher": (1610743808, 2, (9, 0), (), "MeasurementPublisher", '{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}'),
		"PinMapPath": (1610743963, 2, (8, 0), (), "PinMapPath", None),
		"PinMapUsesNIDCPowerChannelGroups": (1610744052, 2, (11, 0), (), "PinMapUsesNIDCPowerChannelGroups", None),
		"SiteNumbers": (1610743809, 2, (8195, 0), (), "SiteNumbers", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IMeasurementPublisher_vtables_dispatch_ = 1
IMeasurementPublisher_vtables_ = [
	(( 'PublishDouble' , 'siteNumberParam' , 'pin' , 'publishedDataId' , 'measurement' , 
			 ), 1610743808, (1610743808, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PublishBool' , 'siteNumberParam' , 'pin' , 'publishedDataId' , 'measurement' , 
			 ), 1610743809, (1610743809, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PublishString' , 'siteNumberParam' , 'pin' , 'publishedDataId' , 'measurement' , 
			 ), 1610743810, (1610743810, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PublishDoubleToTestStandVariable' , 'siteNumber' , 'expression' , 'measurement' , ), 1610743811, (1610743811, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PublishBoolToTestStandVariable' , 'siteNumber' , 'expression' , 'measurement' , ), 1610743812, (1610743812, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PublishStringToTestStandVariable' , 'siteNumber' , 'expression' , 'measurement' , ), 1610743813, (1610743813, (), [ 
			 (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataDouble' , 'siteNumberParam' , 'pin' , 'inputDataId' , 'pRetVal' , 
			 ), 1610743814, (1610743814, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataBoolean' , 'siteNumberParam' , 'pin' , 'inputDataId' , 'pRetVal' , 
			 ), 1610743815, (1610743815, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataString' , 'siteNumberParam' , 'pin' , 'inputDataId' , 'pRetVal' , 
			 ), 1610743816, (1610743816, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentInstanceData_vtables_dispatch_ = 1
IModelBasedInstrumentInstanceData_vtables_ = [
	(( 'instrumentName' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'InstrumentModel' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentProperty_vtables_dispatch_ = 1
IModelBasedInstrumentProperty_vtables_ = [
	(( 'PropertyName' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PropertyValue' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentPropertyList_vtables_dispatch_ = 1
IModelBasedInstrumentPropertyList_vtables_ = [
	(( 'InstrumentModel' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Properties' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (24585, 10, None, "IID('{A8A78603-E18C-4BCB-A347-334AA757B4D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IModelBasedInstrumentResourcePropertyList_vtables_dispatch_ = 1
IModelBasedInstrumentResourcePropertyList_vtables_ = [
	(( 'InstrumentResource' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Properties' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (24585, 10, None, "IID('{A8A78603-E18C-4BCB-A347-334AA757B4D5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISemiconductorModuleContext_vtables_dispatch_ = 1
ISemiconductorModuleContext_vtables_ = [
	(( 'MeasurementPublisher' , 'pRetVal' , ), 1610743808, (1610743808, (), [ (16393, 10, None, "IID('{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SiteNumbers' , 'pRetVal' , ), 1610743809, (1610743809, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetPinNames' , 'instrumentTypeId' , 'capability' , 'dutPinNames' , 'systemPinNames' , 
			 ), 1610743810, (1610743810, (), [ (8, 1, None, None) , (8, 1, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FilterPinsByInstrumentType' , 'pins' , 'instrumentTypeId' , 'capability' , 'pRetVal' , 
			 ), 1610743811, (1610743811, (), [ (8200, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GetAllInstrumentDefinitions' , 'instrumentTypeId' , 'instrumentNames' , 'channelGroupIds' , 'channelLists' , 
			 ), 1610743812, (1610743812, (), [ (8, 1, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SetSessionData' , 'instrumentTypeId' , 'instrumentName' , 'channelGroupId' , 'sessionData' , 
			 ), 1610743813, (1610743813, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GetAllSessionData' , 'instrumentTypeId' , 'sessions' , 'channelGroupIds' , 'channelLists' , 
			 ), 1610743814, (1610743814, (), [ (8, 1, None, None) , (24588, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GetSessionData' , 'instrumentTypeId' , 'pins' , 'sessionData' , 'channelGroupIds' , 
			 'channelLists' , ), 1610743815, (1610743815, (), [ (8, 1, None, None) , (8200, 1, None, None) , (24588, 2, None, None) , 
			 (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GetSessionData_2' , 'instrumentTypeId' , 'pins' , 'sessionData' , 'channelGroupId' , 
			 'channelList' , ), 1610743816, (1610743816, (), [ (8, 1, None, None) , (8200, 1, None, None) , (16396, 2, None, None) , 
			 (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetSiteSemiconductorModuleContexts' , 'pRetVal' , ), 1610743817, (1610743817, (), [ (24585, 10, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GetChannelGroupAndChannelIndex' , 'pins' , 'numberOfPinsPerChannelGroup' , 'channelGroupIndices' , 'channelIndices' , 
			 ), 1610743818, (1610743818, (), [ (8200, 1, None, None) , (24579, 2, None, None) , (24579, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GetChannelGroupAndChannelIndex_2' , 'pinsInLookup' , 'pin' , 'siteNumber' , 'channelGroupIndex' , 
			 'channelIndex' , ), 1610743819, (1610743819, (), [ (8200, 1, None, None) , (8, 1, None, None) , (3, 1, None, None) , 
			 (16387, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerInstrumentNames' , 'channelLists' , 'pRetVal' , ), 1610743821, (1610743821, (), [ (24584, 2, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDCPowerSession' , 'instrumentName' , 'channelId' , 'session' , ), 1610743822, (1610743822, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSessions' , 'pRetVal' , ), 1610743823, (1610743823, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSessions_2' , 'pin' , 'sessions' , 'channelLists' , ), 1610743824, (1610743824, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSessions_3' , 'pins' , 'sessions' , 'channelLists' , ), 1610743825, (1610743825, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSession' , 'pin' , 'session' , 'channelList' , ), 1610743826, (1610743826, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOInstrumentNames' , 'pRetVal' , ), 1610743827, (1610743827, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SetNIHSDIOSessions' , 'instrumentName' , 'acquisitionSession' , 'generationSession' , ), 1610743828, (1610743828, (), [ 
			 (8, 1, None, None) , (21, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSessions' , 'acquisitionSessions' , 'generationSessions' , ), 1610743829, (1610743829, (), [ (24597, 2, None, None) , 
			 (24597, 2, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSessions_2' , 'pin' , 'acquisitionSessions' , 'generationSessions' , 'channelLists' , 
			 ), 1610743830, (1610743830, (), [ (8, 1, None, None) , (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSessions_3' , 'pins' , 'acquisitionSessions' , 'generationSessions' , 'channelLists' , 
			 ), 1610743831, (1610743831, (), [ (8200, 1, None, None) , (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSession' , 'pin' , 'acquisitionSession' , 'generationSession' , 'channelList' , 
			 ), 1610743832, (1610743832, (), [ (8, 1, None, None) , (16405, 2, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOSession_2' , 'pins' , 'acquisitionSession' , 'generationSession' , 'channelList' , 
			 ), 1610743833, (1610743833, (), [ (8200, 1, None, None) , (16405, 2, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOChannelMasks' , 'pins' , 'masks' , ), 1610743834, (1610743834, (), [ (8200, 1, None, None) , 
			 (24595, 2, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GetNIHSDIOChannelMasks_2' , 'pins' , 'masks' , ), 1610743835, (1610743835, (), [ (8200, 1, None, None) , 
			 (24595, 2, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmInstrumentNames' , 'pRetVal' , ), 1610743837, (1610743837, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDmmSession' , 'instrumentName' , 'instrumentSession' , ), 1610743838, (1610743838, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSessions' , 'pRetVal' , ), 1610743839, (1610743839, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSession' , 'pin' , 'pRetVal' , ), 1610743840, (1610743840, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSessions_2' , 'pin' , 'pRetVal' , ), 1610743841, (1610743841, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDmmSessions_3' , 'pins' , 'pRetVal' , ), 1610743842, (1610743842, (), [ (8200, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeInstrumentNames' , 'pRetVal' , ), 1610743843, (1610743843, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SetNIScopeSession' , 'instrumentName' , 'session' , ), 1610743844, (1610743844, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSessions' , 'pRetVal' , ), 1610743845, (1610743845, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSession' , 'pin' , 'session' , 'channelList' , ), 1610743846, (1610743846, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSessions_2' , 'pin' , 'sessions' , 'channelLists' , ), 1610743847, (1610743847, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSession_2' , 'pins' , 'session' , 'channelList' , ), 1610743848, (1610743848, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'GetNIScopeSessions_3' , 'pins' , 'sessions' , 'channelLists' , ), 1610743849, (1610743849, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenInstrumentNames' , 'pRetVal' , ), 1610743850, (1610743850, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SetNIFGenSession' , 'instrumentName' , 'session' , ), 1610743851, (1610743851, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSessions' , 'pRetVal' , ), 1610743852, (1610743852, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSession' , 'pin' , 'session' , 'channelList' , ), 1610743853, (1610743853, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSessions_2' , 'pin' , 'sessions' , 'channelLists' , ), 1610743854, (1610743854, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSession_2' , 'pins' , 'session' , 'channelList' , ), 1610743855, (1610743855, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'GetNIFGenSessions_3' , 'pins' , 'session' , 'channelLists' , ), 1610743856, (1610743856, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTaskNames' , 'taskType' , 'channelLists' , 'pRetVal' , ), 1610743857, (1610743857, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDAQmxTask' , 'taskName' , 'task' , ), 1610743858, (1610743858, (), [ (8, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTasks' , 'taskType' , 'pRetVal' , ), 1610743859, (1610743859, (), [ (8, 1, None, None) , 
			 (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTask' , 'pin' , 'task' , 'channelList' , ), 1610743860, (1610743860, (), [ 
			 (8, 1, None, None) , (16396, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTask_2' , 'pins' , 'task' , 'channelList' , ), 1610743861, (1610743861, (), [ 
			 (8200, 1, None, None) , (16396, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTasks_2' , 'pin' , 'tasks' , 'channelLists' , ), 1610743862, (1610743862, (), [ 
			 (8, 1, None, None) , (24588, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDAQmxTasks_3' , 'pins' , 'tasks' , 'channelLists' , ), 1610743863, (1610743863, (), [ 
			 (8200, 1, None, None) , (24588, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'CreateMultisiteDataForAnalogOutput' , 'perPinWaveform' , 'pin' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743864, (1610743864, (), [ (8204, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'CreateMultisiteDataForAnalogOutput_2' , 'perPinWaveform' , 'pins' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743865, (1610743865, (), [ (8204, 1, None, None) , (8200, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'CreatePerSiteMultisiteDataForAnalogOutput' , 'sitePinWaveforms' , 'pin' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743866, (1610743866, (), [ (8204, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'CreatePerSiteMultisiteDataForAnalogOutput_2' , 'sitePinWaveforms' , 'pins' , 'idleValue' , 'numberOfChannelsInTask' , 
			 'pRetVal' , ), 1610743867, (1610743867, (), [ (8204, 1, None, None) , (8200, 1, None, None) , (12, 1, None, None) , 
			 (16387, 2, None, None) , (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSAInstrumentNames' , 'pRetVal' , ), 1610743872, (1610743872, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFSASession' , 'instrumentName' , 'instrumentSession' , ), 1610743873, (1610743873, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASessions' , 'pRetVal' , ), 1610743874, (1610743874, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASession' , 'pin' , 'pRetVal' , ), 1610743875, (1610743875, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASessions_2' , 'pin' , 'pRetVal' , ), 1610743876, (1610743876, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxInstrumentNames' , 'pRetVal' , ), 1610743877, (1610743877, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFmxSession' , 'instrumentName' , 'instrumentSession' , ), 1610743878, (1610743878, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSessions' , 'pRetVal' , ), 1610743879, (1610743879, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSession' , 'pin' , 'pRetVal' , ), 1610743880, (1610743880, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSessions_2' , 'pin' , 'pRetVal' , ), 1610743881, (1610743881, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGInstrumentNames' , 'pRetVal' , ), 1610743882, (1610743882, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFSGSession' , 'instrumentName' , 'instrumentSession' , ), 1610743883, (1610743883, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSessions' , 'pRetVal' , ), 1610743884, (1610743884, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSession' , 'pin' , 'pRetVal' , ), 1610743885, (1610743885, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSessions_2' , 'pin' , 'pRetVal' , ), 1610743886, (1610743886, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAInstrumentNames' , 'instrumentNames' , 'fpgaFilePaths' , ), 1610743887, (1610743887, (), [ (24584, 2, None, None) , 
			 (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAVIReference' , 'pin' , 'pRetVal' , ), 1610743888, (1610743888, (), [ (8, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAVIReferences' , 'pin' , 'pRetVal' , ), 1610743889, (1610743889, (), [ (8, 1, None, None) , 
			 (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'GetFPGAVIReferences_2' , 'pRetVal' , ), 1610743890, (1610743890, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'SetFPGAVIReference' , 'instrumentName' , 'fpgaVIReference' , ), 1610743891, (1610743891, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMInstrumentNames' , 'instrumentNames' , 'calibrationFilePaths' , 'iviSwitchNames' , 'fpgaFilePaths' , 
			 ), 1610743892, (1610743892, (), [ (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRFPMSession' , 'instrumentName' , 'instrumentSession' , ), 1610743893, (1610743893, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions' , 'pRetVal' , ), 1610743894, (1610743894, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_2' , 'pin' , 'semiconductorModuleContexts' , 'sessions' , 'portList' , 
			 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610743895, (1610743895, (), [ (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSession' , 'systemPin' , 'session' , 'port' , 'deembeddingFilePath' , 
			 'deembeddingOrientation' , ), 1610743896, (1610743896, (), [ (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , 
			 (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_3' , 'pin1' , 'pin2' , 'semiconductorModuleContexts' , 'sessions' , 
			 'portLists1' , 'portLists2' , 'deembeddingFilePaths1' , 'deembeddingFilePaths2' , 'deembeddingOrientations1' , 
			 'deembeddingOrientations2' , ), 1610743897, (1610743897, (), [ (8, 1, None, None) , (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , 
			 (24579, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_4' , 'pins' , 'semiconductorModuleContexts' , 'sessions' , 'portLists' , 
			 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610743898, (1610743898, (), [ (8200, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMSessions_5' , 'systemPins' , 'sessions' , 'portList' , 'deembeddingFilePaths' , 
			 'deembeddingOrientations' , ), 1610743900, (1610743900, (), [ (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , 
			 (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMDeembeddingDataForDutPins' , 'sessions' , 'portLists' , 'deembeddingFilePaths' , 'deembeddingOrientations' , 
			 ), 1610743901, (1610743901, (), [ (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFPMDeembeddingDataForSystemPins' , 'sessions' , 'portLists' , 'deembeddingFilePaths' , 'deembeddingOrientations' , 
			 ), 1610743903, (1610743903, (), [ (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchNames' , 'switchTypeId' , 'pRetVal' , ), 1610743904, (1610743904, (), [ (8, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'SetSwitchSession' , 'switchTypeId' , 'switchName' , 'switchSession' , ), 1610743905, (1610743905, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchSessions' , 'switchTypeId' , 'pRetVal' , ), 1610743906, (1610743906, (), [ (8, 1, None, None) , 
			 (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'GetSwitchSessions_2' , 'switchTypeId' , 'pin' , 'semiconductorModuleContexts' , 'switchSessions' , 
			 'switchRoute' , ), 1610743907, (1610743907, (), [ (8, 1, None, None) , (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24588, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleNames' , 'ni5530RFPortModuleNames' , 'calibrationFilePaths' , ), 1610743908, (1610743908, (), [ (24584, 2, None, None) , 
			 (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'SetNI5530RFPortModuleSession' , 'ni5530RFPortModuleName' , 'ni5530RFPortModuleSession' , 'calibrationSession' , ), 1610743909, (1610743909, (), [ 
			 (8, 1, None, None) , (21, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleSessions' , 'ni5530RFPortModuleSessions' , 'calibrationSessions' , ), 1610743910, (1610743910, (), [ (24597, 2, None, None) , 
			 (24597, 2, None, None) , ], 1 , 1 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleSessions_2' , 'pin' , 'semiconductorModuleContexts' , 'ni5530RFPortModuleSessions' , 'calibrationSessions' , 
			 'ni5530Channel1' , 'ni5530Channel2' , ), 1610743911, (1610743911, (), [ (8, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'GetNI5530RFPortModuleSessions_3' , 'pins' , 'semiconductorModuleContexts' , 'ni5530RFPortModuleSessions' , 'calibrationSessions' , 
			 'ni5530Channel1' , 'ni5530Channel2' , ), 1610743912, (1610743912, (), [ (8200, 1, None, None) , (24585, 2, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , 
			 (24597, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'Publish' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743913, (1610743913, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'Publish_2' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743914, (1610743914, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'Publish_3' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743915, (1610743915, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'Publish_4' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743917, (1610743917, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'Publish_5' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743919, (1610743919, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'Publish_6' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743920, (1610743920, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'Publish_7' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610743921, (1610743921, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'Publish_8' , 'pins' , 'publishedDataId' , 'measurements' , ), 1610743923, (1610743923, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'Publish_9' , 'publishedDataId' , 'measurements' , ), 1610743925, (1610743925, (), [ (8, 1, None, None) , 
			 (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'Publish_10' , 'publishedDataId' , 'measurements' , ), 1610743926, (1610743926, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'Publish_11' , 'publishedDataId' , 'measurements' , ), 1610743927, (1610743927, (), [ (8, 1, None, None) , 
			 (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataBoolean' , 'pin' , 'inputDataId' , 'pRetVal' , ), 1610743928, (1610743928, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataDouble' , 'pin' , 'inputDataId' , 'pRetVal' , ), 1610743929, (1610743929, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'GetInputDataString' , 'pin' , 'inputDataId' , 'pRetVal' , ), 1610743930, (1610743930, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'GetSpecValues' , 'symbols' , 'pRetVal' , ), 1610743931, (1610743931, (), [ (8200, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'GetSpecValue' , 'symbol' , 'pRetVal' , ), 1610743932, (1610743932, (), [ (8, 1, None, None) , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'GetSiteData' , 'dataId' , 'pRetVal' , ), 1610743942, (1610743942, (), [ (8, 1, None, None) , 
			 (24588, 10, None, None) , ], 1 , 1 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'SetSiteData' , 'dataId' , 'data' , ), 1610743943, (1610743943, (), [ (8, 1, None, None) , 
			 (8204, 1, None, None) , ], 1 , 1 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'GetGlobalData' , 'dataId' , 'pRetVal' , ), 1610743944, (1610743944, (), [ (8, 1, None, None) , 
			 (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'SetGlobalData' , 'dataId' , 'data' , ), 1610743945, (1610743945, (), [ (8, 1, None, None) , 
			 (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743946, (1610743946, (), [ (8197, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData_2' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743948, (1610743948, (), [ (8197, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData_3' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743949, (1610743949, (), [ (8203, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'ExtractPinData_4' , 'data' , 'pins' , 'pin' , 'pRetVal' , 
			 ), 1610743951, (1610743951, (), [ (8203, 1, None, None) , (8200, 1, None, None) , (8, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1200 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternInstrumentNames' , 'pRetVal' , ), 1610743952, (1610743952, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1208 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSessions' , 'pRetVal' , ), 1610743953, (1610743953, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1216 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDigitalPatternSession' , 'instrumentName' , 'session' , ), 1610743954, (1610743954, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1224 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSessions_2' , 'pinNames' , 'sessions' , 'channelLists' , 'siteLists' , 
			 ), 1610743955, (1610743955, (), [ (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1232 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSessions_3' , 'pinName' , 'sessions' , 'channelLists' , 'siteLists' , 
			 ), 1610743956, (1610743956, (), [ (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1240 , (3, 0, None, None) , 0 , )),
	(( 'PublishPatternResults' , 'pins' , 'publishedDataId' , 'patternResults' , ), 1610743958, (1610743958, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1256 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteWaveforms' , 'pins' , 'instrumentWaveforms' , 'pRetVal' , ), 1610743959, (1610743959, (), [ 
			 (8200, 1, None, None) , (8211, 1, None, None) , (24595, 10, None, None) , ], 1 , 1 , 4 , 0 , 1264 , (3, 0, None, None) , 0 , )),
	(( 'PerSiteToPerInstrumentWaveforms' , 'pins' , 'perSiteWaveforms' , 'pRetVal' , ), 1610743960, (1610743960, (), [ 
			 (8200, 1, None, None) , (8211, 1, None, None) , (24595, 10, None, None) , ], 1 , 1 , 4 , 0 , 1272 , (3, 0, None, None) , 0 , )),
	(( 'PinMapPath' , 'pRetVal' , ), 1610743963, (1610743963, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 1296 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectSpecificationsFilePaths' , 'pRetVal' , ), 1610743970, (1610743970, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1352 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectLevelsFilePaths' , 'pRetVal' , ), 1610743971, (1610743971, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1360 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectTimingFilePaths' , 'pRetVal' , ), 1610743972, (1610743972, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1368 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectPatternFilePaths' , 'pRetVal' , ), 1610743973, (1610743973, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1376 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectSourceWaveformFilePaths' , 'pRetVal' , ), 1610743974, (1610743974, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1384 , (3, 0, None, None) , 0 , )),
	(( 'GetDigitalPatternProjectCaptureWaveformFilePaths' , 'pRetVal' , ), 1610743975, (1610743975, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1392 , (3, 0, None, None) , 0 , )),
	(( 'ReportUnsupportedCapability' , 'capability' , ), 1610743976, (1610743976, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1400 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverModuleNames' , 'pRetVal' , ), 1610743978, (1610743978, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1416 , (3, 0, None, None) , 0 , )),
	(( 'SetNIRelayDriverSession' , 'relayDriverName' , 'niSwitchSession' , ), 1610743979, (1610743979, (), [ (8, 1, None, None) , 
			 (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1424 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSessions' , 'pRetVal' , ), 1610743980, (1610743980, (), [ (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1432 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSession' , 'relay' , 'niSwitchSession' , 'niSwitchRelayNames' , ), 1610743981, (1610743981, (), [ 
			 (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1440 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSession_2' , 'relays' , 'niSwitchSession' , 'niSwitchRelayNames' , ), 1610743982, (1610743982, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1448 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSessions_2' , 'relay' , 'niSwitchSessions' , 'niSwitchRelayNames' , ), 1610743983, (1610743983, (), [ 
			 (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1456 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRelayDriverSessions_3' , 'relays' , 'niSwitchSessions' , 'niSwitchRelayNames' , ), 1610743984, (1610743984, (), [ 
			 (8200, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1464 , (3, 0, None, None) , 0 , )),
	(( 'ReportInvalidArray' , 'parameterName' , 'elementType' , ), 1610743985, (1610743985, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1472 , (3, 0, None, None) , 0 , )),
	(( 'ReportIncompatibleArrayLengths' , 'arrayParameterName1' , 'arrayParameterName2' , ), 1610743986, (1610743986, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1480 , (3, 0, None, None) , 0 , )),
	(( 'ReportInvalidTimeToWait' , 'parameterName' , ), 1610743987, (1610743987, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1488 , (3, 0, None, None) , 0 , )),
	(( 'ReportMissingDriver' , 'driverName' , ), 1610743988, (1610743988, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1496 , (3, 0, None, None) , 0 , )),
	(( 'GetRelayNames' , 'siteRelayNames' , 'systemRelayNames' , ), 1610743989, (1610743989, (), [ (24584, 2, None, None) , 
			 (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1504 , (3, 0, None, None) , 0 , )),
	(( 'GetRelaysInRelayGroups' , 'relayGroups' , 'pRetVal' , ), 1610743990, (1610743990, (), [ (8200, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1512 , (3, 0, None, None) , 0 , )),
	(( 'SiteDataExists' , 'dataId' , 'pRetVal' , ), 1610743991, (1610743991, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1520 , (3, 0, None, None) , 0 , )),
	(( 'GlobalDataExists' , 'dataId' , 'pRetVal' , ), 1610743992, (1610743992, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 1528 , (3, 0, None, None) , 0 , )),
	(( 'IsSemiconductorModuleInOfflineMode' , 'pRetVal' , ), 1610743993, (1610743993, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1536 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSession' , 'pinNames' , 'session' , 'channelList' , 'siteList' , 
			 ), 1610743994, (1610743994, (), [ (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1544 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDigitalPatternSession_2' , 'pinName' , 'session' , 'channelList' , 'siteList' , 
			 ), 1610743995, (1610743995, (), [ (8, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1552 , (3, 0, None, None) , 0 , )),
	(( 'PublishPatternResults_2' , 'pins' , 'publishedDataId' , 'patternResults' , ), 1610743996, (1610743996, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1560 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSitePatternResults' , 'pins' , 'patternResults' , 'pRetVal' , ), 1610743998, (1610743998, (), [ 
			 (8200, 1, None, None) , (8203, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1576 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentResourceNames' , 'instrumentName' , 'pRetVal' , ), 1610743999, (1610743999, (), [ (8, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1584 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentNames' , 'category' , 'subcategory' , 'pRetVal' , ), 1610744000, (1610744000, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (24585, 10, None, "IID('{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}')") , ], 1 , 1 , 4 , 0 , 1592 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentProperties' , 'instrumentName' , 'pRetVal' , ), 1610744001, (1610744001, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{3BFF2733-C91A-4590-899A-BE97B57C9EDE}')") , ], 1 , 1 , 4 , 0 , 1600 , (3, 0, None, None) , 0 , )),
	(( 'GetModelBasedInstrumentResourceProperties' , 'instrumentName' , 'pRetVal' , ), 1610744002, (1610744002, (), [ (8, 1, None, None) , 
			 (24585, 10, None, "IID('{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}')") , ], 1 , 1 , 4 , 0 , 1608 , (3, 0, None, None) , 0 , )),
	(( 'GetRelayDriverSessionsFromRelayConfiguration' , 'configurationName' , 'sessionsForRelaysInOpenState' , 'niSwitchRelayNamesForRelaysInOpenState' , 'sessionsForRelaysInClosedState' , 
			 'niSwitchRelayNamesForRelaysInClosedState' , ), 1610744003, (1610744003, (), [ (8, 1, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , 
			 (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1616 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610744004, (1610744004, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 1624 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_2' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610744005, (1610744005, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1632 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_3' , 'pin' , 'publishedDataId' , 'measurements' , ), 1610744006, (1610744006, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1640 , (3, 0, None, None) , 0 , )),
	(( 'SetSiteData_2' , 'dataId' , 'data' , ), 1610744008, (1610744008, (), [ (8, 1, None, None) , 
			 (8204, 1, None, None) , ], 1 , 1 , 4 , 0 , 1656 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_4' , 'pin' , 'publishedDataId' , 'measurement' , ), 1610744009, (1610744009, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 1664 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_5' , 'pin' , 'publishedDataId' , 'measurement' , ), 1610744010, (1610744010, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1672 , (3, 0, None, None) , 0 , )),
	(( 'PublishPerSite_6' , 'pin' , 'publishedDataId' , 'measurement' , ), 1610744011, (1610744011, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1680 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData' , 'data' , 'pins' , 'pRetVal' , ), 1610744012, (1610744012, (), [ 
			 (8197, 1, None, None) , (8200, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1688 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData2D' , 'data' , 'pins' , 'pRetVal' , ), 1610744013, (1610744013, (), [ 
			 (8197, 1, None, None) , (8200, 1, None, None) , (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 1696 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData_2' , 'data' , 'pins' , 'pRetVal' , ), 1610744014, (1610744014, (), [ 
			 (8203, 1, None, None) , (8200, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1704 , (3, 0, None, None) , 0 , )),
	(( 'PerInstrumentToPerSiteData2D_2' , 'data' , 'pins' , 'pRetVal' , ), 1610744015, (1610744015, (), [ 
			 (8203, 1, None, None) , (8200, 1, None, None) , (24587, 10, None, None) , ], 1 , 1 , 4 , 0 , 1712 , (3, 0, None, None) , 0 , )),
	(( 'PublishPinNamesForHistoryRamCycleInformation' , 'pins' , 'publishedDataId' , 'pinNames' , ), 1610744017, (1610744017, (), [ 
			 (8200, 1, None, None) , (8, 1, None, None) , (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1728 , (3, 0, None, None) , 0 , )),
	(( 'PublishHistoryRamCycleInformation' , 'pins' , 'publishedDataId' , 'sessionIndex' , 'siteIndex' , 
			 'patternName' , 'timeSetName' , 'vectorNumber' , 'cycleNumber' , 'expectedPinStates' , 
			 'actualPinStates' , 'perPinPassFail' , ), 1610744018, (1610744018, (), [ (8200, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (20, 1, None, None) , 
			 (20, 1, None, None) , (8209, 1, None, None) , (8209, 1, None, None) , (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1736 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSession_2' , 'pin' , 'port' , 'pRetVal' , ), 1610744019, (1610744019, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1744 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxSessions_3' , 'pin' , 'ports' , 'pRetVal' , ), 1610744020, (1610744020, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1752 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASession_2' , 'pin' , 'port' , 'pRetVal' , ), 1610744021, (1610744021, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1760 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSASessions_3' , 'pin' , 'ports' , 'pRetVal' , ), 1610744022, (1610744022, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1768 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSession_2' , 'pin' , 'port' , 'pRetVal' , ), 1610744023, (1610744023, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1776 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGSessions_3' , 'pin' , 'ports' , 'pRetVal' , ), 1610744024, (1610744024, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24597, 10, None, None) , ], 1 , 1 , 4 , 0 , 1784 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxDeembeddingData' , 'pin' , 'deembeddingFilePath' , 'deembeddingOrientation' , ), 1610744025, (1610744025, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1792 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFmxDeembeddingData_2' , 'pin' , 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610744026, (1610744026, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 1800 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSADeembeddingData' , 'pin' , 'deembeddingFilePath' , 'deembeddingOrientation' , ), 1610744027, (1610744027, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1808 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSADeembeddingData_2' , 'pin' , 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610744028, (1610744028, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 1816 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGDeembeddingData' , 'pin' , 'deembeddingFilePath' , 'deembeddingOrientation' , ), 1610744029, (1610744029, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 1824 , (3, 0, None, None) , 0 , )),
	(( 'GetNIRFSGDeembeddingData_2' , 'pin' , 'deembeddingFilePaths' , 'deembeddingOrientations' , ), 1610744030, (1610744030, (), [ 
			 (8, 1, None, None) , (24584, 2, None, None) , (24579, 2, None, None) , ], 1 , 1 , 4 , 0 , 1832 , (3, 0, None, None) , 0 , )),
	(( 'ReportError' , 'errorCode' , 'parameters' , ), 1610744031, (1610744031, (), [ (3, 1, None, None) , 
			 (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1840 , (3, 0, None, None) , 0 , )),
	(( 'GetRelayDriverSessionsFromRelays' , 'relayNames' , 'switchRelayActionsAsIntegerArray' , 'sessionsForRelaysInOpenState' , 'niSwitchRelayNamesForRelaysInOpenState' , 
			 'sessionsForRelaysInClosedState' , 'niSwitchRelayNamesForRelaysInClosedState' , ), 1610744032, (1610744032, (), [ (8200, 1, None, None) , (8195, 1, None, None) , 
			 (24597, 2, None, None) , (24584, 2, None, None) , (24597, 2, None, None) , (24584, 2, None, None) , ], 1 , 1 , 4 , 0 , 1848 , (3, 0, None, None) , 0 , )),
	(( 'GetSemiconductorModuleContextWithSites' , 'SiteNumbers' , 'pRetVal' , ), 1610744033, (1610744033, (), [ (8195, 1, None, None) , 
			 (16393, 10, None, "IID('{3976D65A-5A34-45FC-B30D-79C4A601C537}')") , ], 1 , 1 , 4 , 0 , 1856 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite' , 'expression' , 'measurements' , ), 1610744034, (1610744034, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 1864 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_2' , 'expression' , 'measurements' , ), 1610744035, (1610744035, (), [ (8, 1, None, None) , 
			 (8203, 1, None, None) , ], 1 , 1 , 4 , 0 , 1872 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_3' , 'expression' , 'measurements' , ), 1610744036, (1610744036, (), [ (8, 1, None, None) , 
			 (8200, 1, None, None) , ], 1 , 1 , 4 , 0 , 1880 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_4' , 'expression' , 'measurement' , ), 1610744037, (1610744037, (), [ (8, 1, None, None) , 
			 (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 1888 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_5' , 'expression' , 'measurement' , ), 1610744038, (1610744038, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 1896 , (3, 0, None, None) , 0 , )),
	(( 'PublishToTestStandVariablePerSite_6' , 'expression' , 'measurement' , ), 1610744039, (1610744039, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 1904 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerResourceStrings' , 'pRetVal' , ), 1610744040, (1610744040, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1912 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDCPowerSession_2' , 'resourceString' , 'session' , 'alarmNames' , 'alarmSession' , 
			 ), 1610744041, (1610744041, (), [ (8, 1, None, None) , (21, 1, None, None) , (8200, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1920 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerSession_2' , 'pins' , 'session' , 'channelList' , ), 1610744042, (1610744042, (), [ 
			 (8200, 1, None, None) , (16405, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1928 , (3, 0, None, None) , 0 , )),
	(( 'GetSupportedAlarmNames' , 'resourceString' , 'pRetVal' , ), 1610744043, (1610744043, (), [ (8, 1, None, None) , 
			 (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 1936 , (3, 0, None, None) , 0 , )),
	(( 'SetNIDCPowerSession_3' , 'instrumentName' , 'channelId' , 'session' , 'alarmNames' , 
			 'alarmSession' , ), 1610744044, (1610744044, (), [ (8, 1, None, None) , (8, 1, None, None) , (21, 1, None, None) , 
			 (8200, 1, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 1944 , (3, 0, None, None) , 0 , )),
	(( 'GetNIDCPowerAlarmSession' , 'session' , 'pRetVal' , ), 1610744048, (1610744048, (), [ (21, 1, None, None) , 
			 (16405, 10, None, None) , ], 1 , 1 , 4 , 0 , 1976 , (3, 0, None, None) , 0 , )),
	(( 'GetInstrumentNameAndChannelForPinOnSingleSite' , 'pinName' , 'instrumentName' , 'channelOrPort' , ), 1610744050, (1610744050, (), [ 
			 (8, 1, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 1992 , (3, 0, None, None) , 0 , )),
	(( 'PinMapUsesNIDCPowerChannelGroups' , 'pRetVal' , ), 1610744052, (1610744052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 2008 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithSameDataForAllSites' , 'pinNames' , 'dataFirstDimensionLength' , 'pRetVal' , ), 1610744053, (1610744053, (), [ 
			 (8200, 1, None, None) , (3, 1, None, None) , (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 2016 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForSingleTaskWithDifferentDataForEachSite' , 'pinNames' , 'dataFirstDimensionLength' , 'pRetVal' , ), 1610744054, (1610744054, (), [ 
			 (8200, 1, None, None) , (3, 1, None, None) , (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 2024 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithSameDataForAllSites' , 'pinNames' , 'dataFirstDimensionLength' , 'numberOfChannelsPerTask' , 'pRetVal' , 
			 ), 1610744055, (1610744055, (), [ (8200, 1, None, None) , (3, 1, None, None) , (24579, 2, None, None) , (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 2032 , (3, 0, None, None) , 0 , )),
	(( 'GetDAQmxAnalogOutputDataIndexesForMultipleTasksWithDifferentDataForEachSite' , 'pinNames' , 'dataFirstDimensionLength' , 'numberOfChannelsPerTask' , 'pRetVal' , 
			 ), 1610744056, (1610744056, (), [ (8200, 1, None, None) , (3, 1, None, None) , (24579, 2, None, None) , (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 2040 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{3976D65A-5A34-45FC-B30D-79C4A601C537}' : ISemiconductorModuleContext,
	'{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}' : IModelBasedInstrumentInstanceData,
	'{3BFF2733-C91A-4590-899A-BE97B57C9EDE}' : IModelBasedInstrumentPropertyList,
	'{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}' : IModelBasedInstrumentResourcePropertyList,
	'{A8A78603-E18C-4BCB-A347-334AA757B4D5}' : IModelBasedInstrumentProperty,
	'{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}' : IMeasurementPublisher,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{3976D65A-5A34-45FC-B30D-79C4A601C537}' : 'ISemiconductorModuleContext',
	'{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}' : 'IModelBasedInstrumentInstanceData',
	'{3BFF2733-C91A-4590-899A-BE97B57C9EDE}' : 'IModelBasedInstrumentPropertyList',
	'{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}' : 'IModelBasedInstrumentResourcePropertyList',
	'{A8A78603-E18C-4BCB-A347-334AA757B4D5}' : 'IModelBasedInstrumentProperty',
	'{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}' : 'IMeasurementPublisher',
}


NamesToIIDMap = {
	'ISemiconductorModuleContext' : '{3976D65A-5A34-45FC-B30D-79C4A601C537}',
	'IModelBasedInstrumentInstanceData' : '{0E6C9B02-DB5A-4298-A2B3-8EEFDFAF71FB}',
	'IModelBasedInstrumentPropertyList' : '{3BFF2733-C91A-4590-899A-BE97B57C9EDE}',
	'IModelBasedInstrumentResourcePropertyList' : '{EE428DBB-7E58-4965-A4A8-1E10C53F9BA9}',
	'IModelBasedInstrumentProperty' : '{A8A78603-E18C-4BCB-A347-334AA757B4D5}',
	'IMeasurementPublisher' : '{48E8AD0C-C048-47D7-BA19-2D79CF62FF77}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

