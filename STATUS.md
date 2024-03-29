# Status
## Instrument Based Session API
(Excluding HSDIO)

| Instrument Type | .NET Method                                                             | Python                                          | Python System Tests       |
|-----------------|-------------------------------------------------------------------------|-------------------------------------------------|---------------------------|
| NI-DAQmx        | GetNIDAQmxTaskNames                                                     | get\_all\_nidaqmx\_task\_names                  | test\_nidaqmx             |
| NI-DAQmx        | SetNIDAQmxTask                                                          | set\_nidaqmx\_task                              | test\_nidaqmx             |
| NI-DAQmx        | GetNIDAQmxTask(s)                                                       | pins\_to\_nidaqmx\_task(s)                      | test\_nidaqmx             |
| NI-DAQmx        | GetAllNIDAQmxTasks                                                      | get\_all\_nidaqmx\_tasks                        | test\_nidaqmx             |
| NI-DCPower      | GetNIDCPowerInstrumentNames                                             | *omitted on purpose                             |                           |
| NI-DCPower      | GetNIDCPowerResourceStrings                                             | get\_all\_nidcpower\_resource\_strings          | test\_nidcpower           |
| NI-DCPower      | GetNIDCPowerSession(s)                                                  | pins\_to\_nidcpower\_session(s)                 | test\_nidcpower           |
| NI-DCPower      | SetNIDCPowerSession (name/channel)                                      | *omitted on purpose                             |                           |
| NI-DCPower      | SetNIDCPowerSession (resourceString)                                    | set\_nidcpower\_session                         | test\_nidcpower           |
| NI-DCPower      | GetAllNIDCPowerSessions                                                 | get\_all\_nidcpower\_sessions                   | test\_nidcpower           |
| NI-Digital      | GetNIDigitalPatternInstrumentNames                                      | get\_all\_nidigital\_instrument\_names          | test\_nidigital           |
| NI-Digital      | GetNIDigitalPatternSession(s)                                           | \*omitted on purpose                            |                           |
| NI-Digital      | GetNIDigitalPatternSession(s)ForPattern                                 | get\_nidigital\_session\_for\_pattern           | test\_nidigital           |
| NI-Digital      | GetNIDigitalPatternSession(s)ForPpmu                                    | get\_nidigital\_session\_for\_ppmu              | test\_nidigital           |
| NI-Digital      | SetNIDigitalPatternSession                                              | set\_nidigital\_session                         | test\_nidigital           |
| NI-Digital      | GetAllNIDigitalPatternSessions                                          | get\_all\_nidigital\_sessions                   | test\_nidigital           |
| NI-Digital      | FetchMultisiteHistoryRamInformation\*<br/>\*NI-Digital driver extension |                                                 |                           |
| NI-Digital      | NIDigitalHistoryRamCycleInformation\*<br/>\*class to support HRAM data  |                                                 |                           |
| NI-DMM          | GetNIDmmInstrumentNames                                                 | get\_all\_nidmm\_instrument\_names              | test\_nidmm               |
| NI-DMM          | GetNIDmmSession(s)                                                      | pin\_to\_nidmm\_session(s)                      | test\_nidmm               |
| NI-DMM          | SetNIDmmSession                                                         | set\_nidmm\_session                             | test\_nidmm               |
| NI-DMM          | GetAllNIDmmSessions                                                     | get\_all\_nidmm\_sessions                       | test\_nidmm               |
| NI-FGEN         | GetNIFGenInstrumentNames                                                | get\_all\_nifgen\_instrument\_names             | test\_nifgen              |
| NI-FGEN         | GetNIFgenSession(s)                                                     | pins\_to\_nifgen\_session(s)                    | test\_nifgen              |
| NI-FGEN         | SetNIFGenSession                                                        | set\_nifgen\_session                            | test\_nifgen              |
| NI-FGEN         | GetAllNIFGenSessions                                                    | get\_all\_nifgen\_sessions                      | test\_nifgen              |
| NI-RFmx         | GetNIRfmxInstrumentNames                                                |                                                 |                           |
| NI-RFmx         | GetNIRfmxMultipleDeembeddingData                                        |                                                 |                           |
| NI-RFmx         | GetNIRfmxSingleDeembeddingData                                          |                                                 |                           |
| NI-RFmx         | GetNIRfmxSession(s)                                                     |                                                 |                           |
| NI-RFmx         | SetNIRfmxSession                                                        |                                                 |                           |
| NI-RFmx         | GetAllNIRFmxSessions                                                    |                                                 |                           |
| NI-RFPM         | GetNIRfpmInstrumentNames                                                |                                                 |                           |
| NI-RFPM         | GetNIRfpmSessions                                                       |                                                 |                           |
| NI-RFPM         | SetNIRfpmSession                                                        |                                                 |                           |
| NI-RFPM         | GetAllNIRfpmSessions                                                    |                                                 |                           |
| NI-RFSA         | GetNIRfsaInstrumentNames                                                |                                                 |                           |
| NI-RFSA         | GetNIRfsaMultipleDeembeddingData                                        |                                                 |                           |
| NI-RFSA         | GetNIRfsaSingleDeembeddingData                                          |                                                 |                           |
| NI-RFSA         | GetNIRfsaSession(s)                                                     |                                                 |                           |
| NI-RFSA         | SetNIRfsaSession                                                        |                                                 |                           |
| NI-RFSA         | GetAllNIRfsaSessions                                                    |                                                 |                           |
| NI-RFSG         | GetNIRfsgInstrumentNames                                                |                                                 |                           |
| NI-RFSG         | GetNIRfsgMultipleDeembeddingData                                        |                                                 |                           |
| NI-RFSG         | GetNIRfsgSingleDeembeddingData                                          |                                                 |                           |
| NI-RFSG         | GetNIRfsgSession(s)                                                     |                                                 |                           |
| NI-RFSG         | SetNIRfsgSession                                                        |                                                 |                           |
| NI-RFSG         | GetAllNIRfsgSessions                                                    |                                                 |                           |
| NI-Scope        | GetNIScopeInstrumentNames                                               | get\_all\_niscope\_instrument\_names            | test\_niscope             |
| NI-Scope        | GetNIScopeSession(s)                                                    | pins\_to\_niscope\_session(s)                   | test\_niscope             |
| NI-Scope        | SetNIScopeSession                                                       | set\_niscope\_session                           | test\_niscope             |
| NI-Scope        | GetAllNIScopeSessions                                                   | get\_all\_niscope\_sessions                     | test\_niscope             |
| FPGA            | GetFpgaInstrumentNames                                                  |                                                 |                           |
| FPGA            | SetFpgaVIReference                                                      |                                                 |                           |
| FPGA            | GetFpgaVIReference(s)                                                   |                                                 |                           |
| FPGA            | GetAllFpgaVIReferences                                                  |                                                 |                           |
| Relay Driver    | GetRelayDriverModuleNames                                               | get\_relay\_driver\_module\_names               | test\_nirelaydriver       |
| Relay Driver    | GetRelayDriverNISwitchSession(s)                                        | relays\_to\_relay\_driver\_niswitch\_session(s) | test\_nirelaydriver       |
| Relay Driver    | SetRelayDriverNISwitchSession                                           | set\_relay\_driver\_niswitch\_session           | test\_nirelaydriver       |
| Relay Driver    | GetAllRelayDriverNISwitchSessions                                       | get\_all\_relay\_driver\_niswitch\_sessions     | test\_nirelaydriver       |
| Relay Driver    | ControlRelay                                                            | control_relays                                  | unit test suffices        |
| Relay Driver    | ApplyRelayConfiguration                                                 | apply_relay_configuration                       | unit test suffices        |
| Custom          | GetCustomInstrumentNames                                                | get\_custom\_instrument\_names                  | test\_custom\_instruments |
| Custom          | SetCustomSession                                                        | set\_custom\_session                            | test\_custom\_instruments |
| Custom          | GetCustomSession(s)                                                     | pins\_to\_custom\_session(s)                    | test\_custom\_instruments |
| Custom          | GetAllCustomSessions                                                    | get\_all\_custom\_sessions                      | test\_custom\_instruments |
| Multiplexer     | GetSwitchNames                                                          | get\_all\_switch\_names                         | test\_switch              |
| Multiplexer     | SetSwitchSession                                                        | set\_switch\_session                            | test\_switch              |
| Multiplexer     | GetSwitchSession(s)                                                     | pin\_to\_switch\_sessions                       | test\_switch              |
| Multiplexer     | GetAllSwitchSessions                                                    | get\_all\_switch\_sessions                      | test\_switch              |

## Pin Query API
| Class                           | .NET Method                                    | Python                                                                                             | Python System Tests |
|---------------------------------|------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------|
| SemiconductorModuleContext      | PublishPerSite                                 | publish\_per\_site                                                                                 |                     |
| SemiconductorModuleContext      | PublishToTestStandVariablePerSite              |                                                                                                    |                     |
| PinQueryContext                 | ExtractPinData                                 |                                                                                                    |                     |
| PinQueryContext                 | PerInstrumentToPerSiteData                     |                                                                                                    |                     |
| PinQueryContext                 | GetSessionAndChannelIndex                      | get\_session\_and\_channel\_index                                                                  | unit test suffices  |
| MultiplePinQueryContext         | PerInstrumentToPerSiteData                     |                                                                                                    |                     |
| \_\_SingleSessionQueryContext   | Publish                                        | publish\*<br/>\*supports all variations of data types (float/bool) and number of pins and sessions | various             |
| \_\_MultipleSessionQueryContext | Publish                                        | publish                                                                                            | various             |
| NIDigitalPatternPinQueryContext | PublishPatternResults                          | publish\_pattern\_results                                                                          | test\_nidigital     |
| NIDigitalPatternPinQueryContext | PerInstrumentToPerSitePatternResults           |                                                                                                    |                     |
| NIDigitalPatternPinQueryContext | PerInstrumentToPerSiteWaveforms                |                                                                                                    |                     |
| NIDigitalPatternPinQueryContext | PerSiteToPerInstrumentWaveforms                |                                                                                                    |                     |
| NIDAQmxPinQueryContext          | CreateMultisiteDataForDAQmxAnalogOutput        |                                                                                                    |                     |
| NIDAQmxPinQueryContext          | CreatePerSiteMultisiteDataForDAQmxAnalogOutput |                                                                                                    |                     |

## Other
| Category/Palette     | .NET Method                                   | Python                                             | Python System Tests  |
|----------------------|-----------------------------------------------|----------------------------------------------------|----------------------|
| Specifications       | GetSpecificationsValue                        | get\_specifications\_value                         | test_specifications  |
| Specifications       | GetSpecificationsValues                       | get\_specifications\_values                        | test_specifications  |
| Site and Global Data | GetGlobalData                                 | get\_global\_data                                  | test_site_and_global |
| Site and Global Data | GetSiteData                                   | get\_site\_data                                    | test_site_and_global |
| Site and Global Data | GlobalDataExists                              | global\_data\_exists                               | test_site_and_global |
| Site and Global Data | SetGlobalData                                 | set\_global\_data                                  | test_site_and_global |
| Site and Global Data | SetSiteData                                   | set\_site\_data                                    | test_site_and_global |
| Site and Global Data | SiteDataExists                                | site\_data\_exists                                 | test_site_and_global |
| Advanced             | GetSemiconductorModuleContextWithSites        |                                                    |                      |
| Advanced             | GetSiteSemiconductorModuleContext             |                                                    |                      |
| Misc                 | FilterPinsByInstrumentType                    | filter\_pins\_by\_instrument\_type                 | unit test suffices   |
| Misc                 | GetPins                                       | get\_pin\_names                                    | unit test suffices   |
| Misc                 | GetPinsInPinGroup(s)                          | get\_pins\_in\_pin\_groups                         | unit test suffices   |
| Misc                 | GetRelays                                     | get\_relay\_names                                  | unit test suffices   |
| Misc                 | GetRelaysInRelayGroups                        |                                                    |                      |
| Misc                 | IsSemiconductorModuleInOfflineMode            |                                                    |                      |
| Misc                 | PinMapFilePath                                | pin\_map\_file\_path                               | unit test suffices   |
| Misc                 | PinMapUsesNIDCPowerChannelGroups              |                                                    |                      |
| Misc                 | SiteNumbers                                   | site\_numbers                                      | unit test suffices   |
| Misc                 | InstrumentTypeIdConstants                     | InstrumentTypeIdConstants                          | n/a                  |
| Digital Project      | DigitalPatternProjectCaptureWaveformFilePaths | nidigital\_project\_capture\_waveform\_file\_paths | test\_nidigital      |
| Digital Project      | DigitalPatternProjectLevelsFilePaths          | nidigital\_project\_levels\_file\_paths            | test\_nidigital      |
| Digital Project      | DigitalPatternProjectPatternFilePaths         | nidigital\_project\_pattern\_file\_paths           | test\_nidigital      |
| Digital Project      | DigitalPatternProjectSourceWaveformFilePaths  | nidigital\_project\_source\_waveform\_file\_paths  | test\_nidigital      |
| Digital Project      | DigitalPatternProjectSpecificationsFilePaths  | nidigital\_project\_specifications\_file\_paths    | test\_nidigital      |
| Digital Project      | DigitalPatternProjectTimingFilePaths          | nidigital\_project\_timing\_file\_paths            | test\_nidigital      |
| Input Data           | GetInputDataAsBooleans                        |                                                    |                      |
| Input Data           | GetInputDataAsDouble                          |                                                    |                      |
| Input Data           | GetInputDataAsStrings                         |                                                    |                      |

## Model-Based Instruments
| Class/Interface                   | Method/Property          | Python |
|-----------------------------------|--------------------------|--------|
| SemiconductorModuleContext        | GetModelBasedInstruments |        |
| IModelBasedInstrument             | Category                 |        |
| IModelBasedInstrument             | ModelName                |        |
| IModelBasedInstrument             | Name                     |        |
| IModelBasedInstrument             | Subcategory              |        |
| IModelBasedInstrument             | TryGetResource           |        |
| IModelBasedResource               | ModelResourceName        |        |
| IModelBasedPropertyItemContainer  | TryGetPropertyValue      |        |
| ModelBasedInstrumentSearchOptions | Category                 |        |
| ModelBasedInstrumentSearchOptions | Subcategory              |        |
