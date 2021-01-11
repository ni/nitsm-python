"""
NI TestStand Semiconductor Module Context Python Wrapper
"""

import time
import enum
import pythoncom
import nitsm.codemoduleapi.pinmapinterfaces
import nitsm.codemoduleapi.pinquerycontexts

__all__ = ['Capability', 'InstrumentTypeIdConstants', 'SemiconductorModuleContext']


class Capability(enum.Enum):
    ALL = 0
    NI_HSDIO_DYNAMIC_DIO = 1


class InstrumentTypeIdConstants(enum.Enum):
    ANY = ''
    NI_DAQMX = 'niDAQmx'
    NI_DCPOWER = 'niDCPower'
    NI_DIGITAL_PATTERN = 'niDigitalPattern'
    NI_DMM = 'niDMM'
    NI_FGEN = 'niFGen'
    NI_GENERIC_MULTIPLEXER = 'NIGenericMultiplexer'
    NI_HSDIO = 'niHSDIO'
    NI_MODEL_BASED_INSTRUMENT = 'niModelBasedInstrument'
    NI_RELAY_DRIVER = 'niRelayDriver'
    NI_RFPM = 'niRFPM'
    NI_RFSA = 'niRFSA'
    NI_RFSG = 'niRFSG'
    NI_SCOPE = 'niScope'

    def __str__(self):
        return self.value


class SemiconductorModuleContext:
    _sessions = {}

    def __init__(self, tsm_com_obj):
        """
        Args:
            tsm_com_obj: TestStand Semiconductor Module Context object passed to Python from TestStand
        """

        self._context = nitsm.codemoduleapi.pinmapinterfaces.ISemiconductorModuleContext(tsm_com_obj)
        self._context._oleobj_ = tsm_com_obj._oleobj_.QueryInterface(self._context.CLSID, pythoncom.IID_IDispatch)

    # General and Advanced

    def get_pin_names(self, instrument_type_id, capability):
        """
        Returns all DUT and system pins available in the Semiconductor Module context that are connected to an
        instrument of the type you specify in the instrument_type_id. This method returns only the pins specified on the
        Options tab of the Semiconductor Multi Test step. Pass an empty string to instrument_type_id to return all
        available pins.

        Args:
            instrument_type_id: Specifies the type of instrument for which you want to return DUT and system pins. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types
                that TSM supports natively. For all other types of instruments, you must define a type ID for the
                instrument in the pin map file. Typically, this type ID is an instrument driver name or other ID that is
                common for instruments that users program in a similar way. Pass InstrumentTypeIdConstants.Any to
                include pins from all instruments.

            capability: Limits the filtered pins to those connected to a channel that defines the capability you
                specify. Use capability to differentiate between pins in the same instrument with different
                capabilities, such as NI-HSDIO Dynamic DIO channels and PFI lines. If a pin is connected to channels in
                which the capability is defined only for a subset of sites, the method throws an exception. Pass
                Capability.ALL to return all pins that match instrument_type_id.

        Returns:
            dut_pins: Returns an array of strings that contains the DUT pins in the Semiconductor Module context that
                are connected to an instrument of the type you specify in the instrument_type_id.

            system_pins: Returns an array of strings that contains the system pins in the Semiconductor Module context
                that are connected to an instrument of the type you specify in the instrument_type_id.
        """

        if isinstance(capability, Capability):
            capability = capability.value
        if isinstance(instrument_type_id, InstrumentTypeIdConstants):
            instrument_type_id = str(instrument_type_id)
        return self._context.GetPinNames(instrument_type_id, capability)  # TODO: Unable to return system pin?

    def filter_pins_by_instrument_type(self, pins, instrument_type_id, capability):
        """
        Filters pins by instrument_type_id.
        Pass a list of all pins or pin groups to return the pins connected to instruments of the type you specify in the instrument_type_id.
        If no pins are connected to instruments of the type you specify in instrument_type_id, this method returns an empty array.
        The return value is an array subset of pin names in pins that are connected to an instrument of the filtered instrument_type_id.

        Args:
            pins: An array of pins or pin groups to filter. The array must contain only pins or pin groups that are included in the Semiconductor Module Context.

            instrument_type_id: The type of instrument for which you want to return DUT and system pins.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.
                Pass InstrumentTypeIdConstants.Any to include pins from all instruments.

            capability: Limits the filtered pins to those connected to a channel that defines the capability you specify.
                Use capability to differentiate between pins in the same instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and PFI lines.
                If a pin is connected to channels in which the capability is defined only for a subset of sites, the method throws an exception.
                Pass Capability.All to return all elements in pins that match instrument_type_id.
                Returns an array subset of pin names in the pins that are connected to an instrument of the filtered instrument_type_id.

        Returns:
            Returns an array subset of pin names in the pins that are connected to an instrument of the filtered instrument_type_id.
        """

        if isinstance(instrument_type_id, InstrumentTypeIdConstants):
            instrument_type_id = str(instrument_type_id)
        return self._context.FilterPinsByInstrumentType(pins, instrument_type_id, capability)

    def get_pins_in_pin_group(self, pin_group):
        """
        Returns a list of pins contained in the pin group you specify in the pin_group.

        Args:
            pin_group: A pin group. The pin group must be included in the Semiconductor Module Context.
        """

        return self.get_pins_in_pin_groups([pin_group])

    def get_pins_in_pin_groups(self, pin_groups):
        """
        Returns a list of pins contained in the pin groups you specify in the pin_groups.

        Args:
            pin_groups: An array of pin groups. The array must contain only pin groups that are included in the Semiconductor Module Context.
        """

        return self.filter_pins_by_instrument_type(pin_groups, '', 'All')

    # NI-Digital

    def get_all_nidigital_instrument_names(self):
        """
        Returns an array of instrument names and comma-separated lists of instrument names that belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module Context.
        You can use the instrument names and comma-separated lists of instrument names to open driver sessions.
        """

        return self._context.GetNIDigitalPatternInstrumentNames()

    def set_nidigital_session(self, instrument_name, session):
        """
        Associates an instrument session with an NI-Digital Pattern instrument_name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.

            session: The instrument session for the corresponding instrument_name.
        """

        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDigitalPatternSession(instrument_name, session_id)

    def get_all_nidigital_sessions(self):
        """
        Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module Context.
        You can use instrument sessions to close driver sessions.
        Note: Calling the Close method on the returned session objects does not close the sessions if you did not open the session in .NET.
        """

        session_ids = self._context.GetNIDigitalPatternSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_nidigital_session(self, pin):
        """
        Returns the NI-Digital Pattern session and pin_set_string required to access the pin, as well as the site_list associated with the pin_set_string.
        If more than one session is required to access the pin, the method throws an exception.
        Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.

        Args:
            pin: The name of the pin or pin group to translate to session and pin_set_string.

        Returns:
            session: Returns the NI-Digital Pattern instrument session for the instrument(s) connected to pin for all sites in the Semiconductor Module Context.

            pin_set_string: Returns the pin set string for the instrument session required to access the pin for all sites in the Semiconductor Module Context. The pin set is specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern driver.
                If the pin is shared and there are multiple connections of the same channel to the pin, the channel only appears once in the string and is identified by one of the site/pin combinations to which it is connected.

            site_list: Returns a string that is a comma-separated list of sites (e.g. "site0,site1") that correspond to the sites associated with the channels in the channel_list. This site_list is needed as an input to certain NI-Digital Pattern driver calls.

            pin_query_context: An object that tracks the session and channels associated with this pin query. Use this object to publish measurements, to publish pattern results and to extract data from a set of measurements
        """

        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDigitalPatternSingleSessionPinQueryContext(self._context, pin)
        session_id, pin_set_string, site_list = self._context.GetNIDigitalPatternSession_2(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, pin_set_string, site_list

    def pins_to_nidigital_session(self, pins):
        """
        Returns the NI-Digital Pattern session and pin_set_string required to access the pins, as well as the siteList associated with the pin_set_string.
        If more than one session is required to access the pins, the method throws an exception.
        Each group of NI-Digital Pattern instruments in the pin map creates a single instrument session.

        Args:
            pins: The name of the pins or pin groups to translate to session and pin_set_string.

        Returns:
            session: Returns the NI-Digital Pattern instrument session for the instrument(s) connected to pins for all sites in the Semiconductor Module Context.

            pin_set_string: Returns the pin set string for the instrument session required to access the pins for all sites in the Semiconductor Module Context. The pin set is specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern driver.
                If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected.

            site_list: Returns a string that is a comma-separated list of sites (e.g. "site0,site1") that correspond to the sites associated with the channels in the channel_list. This site_list is needed as an input to certain NI-Digital Pattern driver calls.

            pin_query_context: An object that tracks the session and channels associated with this pin query. Use this object to publish measurements, to publish pattern results and to extract data from a set of measurements.
        """

        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDigitalPatternSingleSessionPinQueryContext(self._context, pins)
        session_id, pin_set_string, site_list = self._context.GetNIDigitalPatternSession(pins)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, pin_set_string, site_list

    def pin_to_nidigital_sessions(self, pin):
        """
        Returns the NI-Digital Pattern sessions and pin_set_strings required to access the pin, as well as the site_lists associated with the pin_set_strings.

        Args:
            pin: The name of the pin or pin group to translate to sessions and pin_set_strings.

        Returns:
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments connected to pin for all sites in the Semiconductor Module Context.

            pin_set_strings: Returns the pin set strings for each instrument session required to access the pin for all sites in the Semiconductor Module Context. The pin sets are specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern driver.
                If the pin is shared and there are multiple connections of the same channel to the pin, the channel only appears once in each string and is identified by one of the site/pin combinations to which it is connected.

            site_lists: Returns an array of comma-separated lists of sites (e.g. "site0,site1") that correspond to the sites associated with the channels in the channel_list. This site_list is needed as an input to certain NI-Digital Pattern driver calls.

            pin_query_context: An object that tracks the sessions and channels associated with this pin query. Use this object to publish measurements, to publish pattern results and to extract data from a set of measurements.
        """

        pin_query_context = nitsm.codemoduleapi.pinquerycontexts.NIDigitalPatternPinQueryContext(self._context, pin)
        session_ids, pin_set_strings, site_lists = self._context.GetNIDigitalPatternSessions_3(pin)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, pin_set_strings, site_lists

    def pins_to_nidigital_sessions(self, pins):
        """
        Returns the NI-Digital Pattern sessions and pin_set_strings required to access the pins, as well as the site_lists associated with the pin_set_strings.

        Args:
            pins: The name of the pins or pin groups to translate to sessions and pin_set_strings.

        Returns:
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments connected to pins for all sites in the Semiconductor Module Context.

            pin_set_strings: Returns the pin set strings for each instrument session required to access the pins for all sites in the Semiconductor Module Context. The pin sets are specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern driver.
                If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the string and is identified by one of the site/pin combinations to which it is connected.

            site_lists: Returns an array of comma-separated lists of sites (e.g. "site0,site1") that correspond to the sites associated with the channels in the channel_lists. This site_list is needed as an input to certain NI-Digital Pattern driver calls.

            pin_query_context: An object that tracks the sessions and channels associated with this pin query. Use this object to publish measurements, to publish pattern results and to extract data from a set of measurements.
        """

        pin_query_context = nitsm.codemoduleapi.pinquerycontexts.NIDigitalPatternPinQueryContext(self._context, pins)
        session_ids, pin_set_strings, site_lists = self._context.GetNIDigitalPatternSessions_2(pins)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, pin_set_strings, site_lists

    @property
    def pin_map_file_path(self):
        """
        The absolute path to the pin map file for this Semiconductor Module Context.
        """

        return self._context.PinMapPath

    @property
    def nidigital_project_specifications_file_paths(self):
        """
        The absolute paths to the Specifications files in the Digital Pattern Project associated with this Semiconductor Module Context.
        """

        return self._context.GetDigitalPatternProjectSpecificationsFilePaths()

    @property
    def nidigital_project_levels_file_paths(self):
        """
        The absolute paths to the Levels file in the Digital Pattern Project associated with this Semiconductor Module Context.
        """

        return self._context.GetDigitalPatternProjectLevelsFilePaths()

    @property
    def nidigital_project_timing_file_paths(self):
        """
        The absolute paths to the Timing files in the Digital Pattern Project associated with this Semiconductor Module Context.
        """

        return self._context.GetDigitalPatternProjectTimingFilePaths()

    @property
    def nidigital_project_pattern_file_paths(self):
        """
        The absolute paths to the Pattern files in the Digital Pattern Project associated with this Semiconductor Module Context.
        """

        return self._context.GetDigitalPatternProjectPatternFilePaths()

    @property
    def nidigital_project_source_waveform_file_paths(self):
        """
        The absolute paths to the Source Waveform files in the Digital Pattern Project associated with this Semiconductor Module Context.
        """

        return self._context.GetDigitalPatternProjectSourceWaveformFilePaths()

    @property
    def nidigital_project_capture_waveform_file_paths(self):
        """
        The absolute paths to the Capture Waveform files in the Digital Pattern Project associated with this Semiconductor Module Context.
        """

        return self._context.GetDigitalPatternProjectCaptureWaveformFilePaths()

    # NI-DCPower

    def get_all_nidcpower_instrument_names(self):
        """
        TODO: Summary
        Returns: tuple(instrument_names, channel_ids)
            instrument_names: tuple
            channel_strings: tuple
        """

        return self._context.GetNIDCPowerInstrumentNames()

    def get_all_nidcpower_resource_strings(self):
        """
        TODO: Summary
        Returns:

        """
        return self._context.GetNIDCPowerResourceStrings()

    def set_nidcpower_session(self, instrument_name, channel_id, session):
        """
        TODO: Summary
        Args:
            instrument_name:
            channel_id:
            session:

        Returns:

        """
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDCPowerSession(instrument_name, channel_id, session_id)

    def get_all_nidcpower_sessions(self):
        session_ids = self._context.GetNIDCPowerSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_nidcpower_session(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDCPowerSinglePinSingleSessionQueryContext(self._context, pin)
        session_id, channel_string = self._context.GetNIDCPowerSession(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_string

    def pins_to_nidcpower_session(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDCPowerMultiplePinSingleSessionQueryContext(self._context, pins)
        session_id, channel_string = self._context.GetNIDCPowerSession_2(pins)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_string

    def pin_to_nidcpower_sessions(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDCPowerSinglePinMultipleSessionQueryContext(self._context, pin)
        session_ids, channel_strings = self._context.GetNIDCPowerSessions_2(pin)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, channel_strings

    def pins_to_nidcpower_sessions(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDCPowerMultiplePinMultipleSessionQueryContext(self._context, pins)
        session_ids, channel_strings = self._context.GetNIDCPowerSessions_3(pins)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, channel_strings

    # NI-DAQmx

    def get_all_nidaqmx_task_names(self, task_type):
        return self._context.GetNIDAQmxTaskNames(task_type)

    def set_nidaqmx_task(self, task_name, task):
        task_id = id(task)
        SemiconductorModuleContext._sessions[task_id] = task
        return self._context.SetNIDAQmxTask(task_name, task_id)

    def get_all_nidaqmx_tasks(self, task_type):
        task_ids = self._context.GetNIDAQmxTasks(task_type)
        return tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)

    def pin_to_nidaqmx_task(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDAQmxSinglePinSingleTaskQueryContext(self._context, pin)
        task_id, channel_list = self._context.GetNIDAQmxTask(pin)
        task = SemiconductorModuleContext._sessions[task_id]
        return pin_query_context, task, channel_list

    def pins_to_nidaqmx_task(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDAQmxMultiplePinSingleTaskQueryContext(self._context, pins)
        task_id, channel_list = self._context.GetNIDAQmxTask_2(pins)
        task = SemiconductorModuleContext._sessions[task_id]
        return pin_query_context, task, channel_list

    def pin_to_nidaqmx_tasks(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDAQmxSinglePinMultipleTaskQueryContext(self._context, pin)
        task_ids, channel_lists = self._context.GetNIDAQmxTasks_2(pin)
        tasks = tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)
        return pin_query_context, tasks, channel_lists

    def pins_to_nidaqmx_tasks(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDAQmxMultiplePinMultipleTaskQueryContext(self._context, pins)
        task_ids, channel_lists = self._context.GetNIDAQmxTasks_3(pins)
        tasks = tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)
        return pin_query_context, tasks, channel_lists

    # NI-DMM

    def get_all_nidmm_instrument_names(self):
        return self._context.GetNIDmmInstrumentNames()

    def set_nidmm_session(self, instrument_name, session):
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDmmSession(instrument_name, session_id)

    def get_all_nidmm_sessions(self):
        session_ids = self._context.GetNIDmmSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_nidmm_session(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDmmSinglePinSingleSessionQueryContext(self._context, pin)
        session_id = self._context.GetNIDmmSession(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session

    def pin_to_nidmm_sessions(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDmmSinglePinMultipleSessionQueryContext(self._context, pin)
        session_ids = self._context.GetNIDmmSessions_2(pin)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions

    def pins_to_nidmm_sessions(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIDmmMultiplePinMultipleSessionQueryContext(self._context, pins)
        session_ids = self._context.GetNIDmmSessions_3(pins)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions

    # NI-FGEN

    def get_all_nifgen_instrument_names(self):
        return self._context.GetNIFGenInstrumentNames()

    def set_nifgen_session(self, instrument_name, session):
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIFGenSession(instrument_name, session_id)

    def get_all_nifgen_sessions(self):
        session_ids = self._context.GetNIFGenSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_nifgen_session(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIFGenSinglePinSingleSessionQueryContext(self._context, pin)
        session_id, channel_list = self._context.GetNIFGenSession(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pins_to_nifgen_session(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIFGenMultiplePinSingleSessionQueryContext(self._context, pins)
        session_id, channel_list = self._context.GetNIFGenSession_2(pins)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pin_to_nifgen_sessions(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIFGenSinglePinMultipleSessionQueryContext(self._context, pin)
        session_ids, channel_lists = self._context.GetNIFGenSessions_2(pin)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, channel_lists

    def pins_to_nifgen_sessions(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIFGenMultiplePinMultipleSessionQueryContext(self._context, pins)
        session_ids, channel_lists = self._context.GetNIFGenSessions_3(pins)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, channel_lists

    # NI-SCOPE

    def get_all_niscope_instrument_names(self):
        return self._context.GetNIScopeInstrumentNames()

    def set_niscope_session(self, instrument_name, session):
        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIScopeSession(instrument_name, session_id)

    def get_all_niscope_sessions(self):
        session_ids = self._context.GetNIScopeSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_niscope_session(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIScopeSinglePinSingleSessionQueryContext(self._context, pin)
        session_id, channel_list = self._context.GetNIScopeSession(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pins_to_niscope_session(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIScopeMultiplePinSingleSessionQueryContext(self._context, pins)
        session_id, channel_list = self._context.GetNIScopeSession_2(pins)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pin_to_niscope_sessions(self, pin):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIScopeSinglePinMultipleSessionQueryContext(self._context, pin)
        session_ids, channel_lists = self._context.GetNIScopeSessions_2(pin)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, channel_lists

    def pins_to_niscope_sessions(self, pins):
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.NIScopeMultiplePinMultipleSessionQueryContext(self._context, pins)
        session_ids, channel_lists = self._context.GetNIScopeSessions_3(pins)
        sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return pin_query_context, sessions, channel_lists

    # Relay Driver

    def get_relay_driver_module_names(self):
        return self._context.GetNIRelayDriverModuleNames()

    def set_relay_driver_niswitch_session(self, relay_driver_module_name, niswitch_session):
        session_id = id(niswitch_session)
        SemiconductorModuleContext._sessions[session_id] = niswitch_session
        return self._context.SetNIRelayDriverSession(relay_driver_module_name, session_id)

    def get_all_relay_driver_niswitch_sessions(self):
        session_ids = self._context.GetNIRelayDriverSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def relay_to_relay_driver_niswitch_session(self, relay):
        session_id, niswitch_relay_names = self._context.GetNIRelayDriverSession(relay)
        niswitch_session = SemiconductorModuleContext._sessions[session_id]
        return niswitch_session, niswitch_relay_names

    def relays_to_relay_driver_niswitch_session(self, relays):
        session_id, niswitch_relay_names = self._context.GetNIRelayDriverSession_2(relays)
        niswitch_session = SemiconductorModuleContext._sessions[session_id]
        return niswitch_session, niswitch_relay_names

    def relay_to_relay_driver_niswitch_sessions(self, relay):
        session_ids, niswitch_relay_names = self._context.GetNIRelayDriverSessions_2(relay)
        niswitch_sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return niswitch_sessions, niswitch_relay_names

    def relays_to_relay_driver_niswitch_sessions(self, relays):
        session_ids, niswitch_relay_names = self._context.GetNIRelayDriverSessions_3(relays)
        niswitch_sessions = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return niswitch_sessions, niswitch_relay_names

    @staticmethod
    def __apply_relay_action(session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close):
        for session_id_to_open, relay_name_to_open in session_ids_for_open, relay_names_to_open:
            session_to_open = SemiconductorModuleContext._sessions[session_id_to_open]
            session_to_open.relay_control(relay_name_to_open, 20)
        for session_id_to_close, relay_name_to_close in session_ids_for_close, relay_names_to_close:
            session_to_close = SemiconductorModuleContext._sessions[session_id_to_close]
            session_to_close.relay_control(relay_name_to_close, 21)
        return None

    def __relay_wait(self, wait_seconds):
        if wait_seconds == 0.0:
            return None
        elif wait_seconds > 0.0:
            time.sleep(wait_seconds)
        else:
            self._context.ReportInvalidTimeToWait('wait_seconds')
        return None

    def apply_relay_configuration(self, relay_configuration, wait_seconds=0.0):
        session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close = \
            self._context.GetRelayDriverSessionsFromRelayConfiguration(relay_configuration)
        self.__apply_relay_action(
            session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close
        )
        self.__relay_wait(wait_seconds)
        return None

    def control_relay_single_action(self, relay, relay_action, wait_seconds=0.0):
        niswitch_sessions_and_relay_names = self.relay_to_relay_driver_niswitch_sessions(relay)
        for niswitch_session, niswitch_relay_name in niswitch_sessions_and_relay_names:
            niswitch_session.relay_control(niswitch_relay_name, relay_action.value)
        self.__relay_wait(wait_seconds)
        return None

    def control_relays_single_action(self, relays, relay_action, wait_seconds=0.0):
        niswitch_sessions_and_relay_names = self.relays_to_relay_driver_niswitch_sessions(relays)
        for niswitch_session, niswitch_relay_name in niswitch_sessions_and_relay_names:
            niswitch_session.relay_control(niswitch_relay_name, relay_action.value)
        self.__relay_wait(wait_seconds)
        return None

    def control_relays_multiple_action(self, relays, relay_actions, wait_seconds=0.0):
        if len(relays) != len(relay_actions):
            self._context.ReportIncompatibleArrayLengths('relays', 'relay_actions')
        else:
            relay_actions = [relay_action.value for relay_action in relay_actions]
            session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close = \
                self._context.GetRelayDriverSessionsFromRelays(relays, relay_actions)
            self.__apply_relay_action(
                session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close
            )
            self.__relay_wait(wait_seconds)
        return None

    def get_relay_names(self):
        return self._context.GetRelayNames()

    # Custom Instruments

    def get_custom_instrument_names(self, instrument_type_id):
        """
        Returns the channel_group_ids and associated instrument_names and channel_lists of all instruments of type instrument_type_id defined in the Semiconductor Module Context.
        You can use instrument_names, channel_group_ids, and channel_lists to open driver sessions.
        The instrument_names, channel_group_ids, and channel_lists parameters always return the same number of elements. Instrument names repeat in instrument_names if the instrument has multiple channel groups.

        Args:
            instrument_type_id: The type of instrument for which you want to return instrument definitions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

        Returns:
            instrument_names: Returns the names of all instruments in the Semiconductor Module Context that are of type instrument_type_id.

            channel_group_ids: Returns the IDs of all channel groups in the Semiconductor Module Context that belong to an instrument of type instrument_type_id.
                For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            channel_lists: Returns the channel lists for each element of channel_group_ids. Each channel list is a comma-separated list of channels.
        """

        return self._context.GetAllInstrumentDefinitions(instrument_type_id)

    def set_custom_session(self, instrument_type_id, instrument_name, channel_group_id, session_data):
        """
        Associates a session with an instrument and channel group.

        Args:
            instrument_type_id: The type of instrument for which you want to set the session.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

            instrument_name: The instrument name in the pin map file for the corresponding session. The instrument must be of type instrument_type_id.

            channel_group_id: The channel group in the pin map file for the corresponding session.
                For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            session_data: The session for the corresponding instrumentName and channel_group_id.
        """

        session_id = id(session_data)
        SemiconductorModuleContext._sessions[session_id] = session_data
        return self._context.SetSessionData(instrument_type_id, instrument_name, channel_group_id, session_id)

    def get_all_custom_sessions(self, instrument_type_id):
        """
        Returns all set sessions in the Semiconductor Module Context that belong to instruments of type instrument_type_id.

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

            session_data: Returns an array of session data set in the Semiconductor Module Context.

            channel_group_ids: Returns the IDs of the channel groups on which sessionData was stored.
                 For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            channel_lists: Returns the channel lists for each of the channel_group_ids. Each channel list is a comma-separated list of channels.
        """

        session_ids, *channel_data = self._context.GetAllSessionData(instrument_type_id)
        session_data = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return (session_data, *channel_data)

    def pin_to_custom_session(self, instrument_type_id, pin):
        """
        Returns the session in the Semiconductor Module Context associated with pin.

        Args:
            instrument_type_id: The type of instrument for which you want to get a session.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

            pin: The name of the pin or pin group to translate to session_data, channel_group_id, and channel_list.
                The pin must be connected to an instrument of type instrument_type_id.

        Returns:
            session_data: Returns the session data associated with pin.

            channel_group_id: Returns the ID of the channel group that contains the channels connected to pin.
                For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            channel_list: Returns the channel list that correspond to pin associated with sessionData and channel_group_id. The channel list is a comma-separated list of channels.
                If the pin is shared and there are multiple connections of the same channel to the pin, the channel only appears once in the list.

            pin_query_context: An object that tracks the sessions and channels associated with this pin query.
                Use this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms.
        """

        pin_query_context = nitsm.codemoduleapi.pinquerycontexts.SinglePinSingleSessionQueryContext(self._context, pin)
        _, *session_and_channel_data = self.pins_to_custom_session(instrument_type_id, [pin])
        return (pin_query_context, *session_and_channel_data)

    def pins_to_custom_session(self, instrument_type_id, pins):
        """
        Returns all sessions in the Semiconductor Module Context associated with pins.

        Args:
            instrument_type_id: The type of instrument for which you want to get a session.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

            pins: The names of the pins or pin groups to translate to session_data, channel_group_id, and channel_list.
                The pins must be connected to instruments of type instrument_type_id.

        Returns:
            session_data: Returns the session data associated with pins.

            channel_group_id: Returns the ID of the channel groups that contain the channels connected to pins.
                For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            channel_list: Returns the channel list that corresponds to pins associated with session_data and channel_group_id. The channel list is a comma-separated list of channels.
                If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the list.

            pin_query_context: An object that tracks the sessions and channels associated with this pin query.
                Use this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms.
        """

        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.MultiplePinSingleSessionQueryContext(self._context, pins)
        session_id, *channel_data = self._context.GetSessionData_2(instrument_type_id, pins)
        session_data = SemiconductorModuleContext._sessions[session_id]
        return (pin_query_context, session_data, *channel_data)

    def pin_to_custom_sessions(self, instrument_type_id, pin):
        """
        Returns all sessions in the Semiconductor Module Context associated with pin.

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

            pin: The name of the pin or pin group to translate to session_data, channel_group_ids, and channel_lists.
                The pin must be connected to an instrument of type instrument_type_id.

        Returns:
            session_data: Returns an array of session data associated with pin.

            channel_group_ids: Returns the IDs of the channel groups that contain the channels connected to pin.
                For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            channel_lists: Returns the channel lists that correspond to pin associated with session_data and channel_group_ids. Each channel list is a comma-separated list of channels.
                If the pin is shared and there are multiple connections of the same channel to the pin, the channel only appears once in each list.

            pin_query_context: An object that tracks the sessions and channels associated with this pin query.
                Use this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms.
        """

        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.SinglePinMultipleSessionQueryContext(self._context, pin)
        _, *session_and_channel_data = self.pins_to_custom_sessions(instrument_type_id, [pin])
        return (pin_query_context, *session_and_channel_data)

    def pins_to_custom_sessions(self, instrument_type_id, pins):
        """
        Returns all sessions in the ISemiconductorModuleContext associated with pins.

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for instrument types that TSM
                supports natively. For all other types of instruments, you must define a type ID for the instrument in the pin map file. Typically, this type ID is an instrument driver
                name or other ID that is common for instruments that users program in a similar way.

            pins: The names of the pins or pin groups to translate to session_data, channel_group_ids, and channel_lists.
                The pins must be connected to instruments of type instrument_type_id.

        Returns:
            session_data: Returns an array of session data associated with pins.

            channel_group_ids: Returns the IDs of the channel groups that contain the channels connected to pins.
                For channels that do not belong to a channel group in the pin map, the Semiconductor Module creates a channel group with the same ID as the channel.

            channel_lists: Returns the channel lists that correspond to pins associated with session_data and channel_group_ids. Each channel list is a comma-separated list of channels.
                If any of the pins are connected to the same instrument channel for multiple sites, the channel appears only once in the list.

            pin_query_context:
                An object that tracks the sessions and channels associated with this pin query.
                Use this object to publish measurements, extract data from a set of measurements, and create or rearrange waveforms.
        """
        
        pin_query_context = \
            nitsm.codemoduleapi.pinquerycontexts.MultiplePinMultipleSessionQueryContext(self._context, pins)
        session_ids, *channel_data = self._context.GetSessionData(instrument_type_id, pins)
        session_data = tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)
        return (pin_query_context, session_data, *channel_data)
