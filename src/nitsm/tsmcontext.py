"""
NI TestStand Semiconductor Module Context Python Wrapper
"""

import time
import typing
import pythoncom
import nitsm._pinmapinterfaces
import nitsm.pinquerycontexts
import nitsm.enums

__all__ = ["SemiconductorModuleContext"]

if typing.TYPE_CHECKING:
    from typing import Any as _Any
    from typing import Tuple as _Tuple
    from typing import Union as _Union
    from typing import Sequence as _Sequence
    import nidigital
    import nidcpower
    import nidaqmx
    import nidmm
    import nifgen
    import niscope
    import niswitch

    _PinQueryContext = nitsm.pinquerycontexts.PinQueryContext
    _InstrTypeIdArg = _Union[nitsm.enums.InstrumentTypeIdConstants, str]
    _CapabilityArg = _Union[nitsm.enums.Capability, str]
    _PinsArg = _Union[str, _Sequence[str]]  # argument that accepts 1 or more pins
    _StringTuple = _Tuple[str, ...]

    _NIDigitalSingleSessionQuery = _Tuple[_PinQueryContext, nidigital.Session, str]
    _NIDigitalMultipleSessionQuery = _Tuple[
        _PinQueryContext,
        _Tuple[nidigital.Session, ...],
        _StringTuple,
    ]

    _NIDCPowerSingleSessionQuery = _Tuple[_PinQueryContext, nidcpower.Session, str]
    _NIDCPowerMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[nidcpower.Session, ...], _StringTuple
    ]

    _NIDAQmxSingleSessionQuery = _Tuple[_PinQueryContext, nidaqmx.Task, str]
    _NIDAQmxMultipleSessionQuery = _Tuple[_PinQueryContext, _Tuple[nidaqmx.Task, ...], _StringTuple]

    _NIDmmSingleSessionQuery = _Tuple[_PinQueryContext, nidmm.Session]
    _NIDmmMultipleSessionQuery = _Tuple[_PinQueryContext, _Tuple[nidmm.Session, ...]]

    _NIFGenSingleSessionQuery = _Tuple[_PinQueryContext, nifgen.Session, str]
    _NIFGenMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[nifgen.Session, ...], _StringTuple
    ]

    _NIScopeSingleSessionQuery = _Tuple[_PinQueryContext, niscope.Session, str]
    _NIScopeMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[niscope.Session, ...], _StringTuple
    ]

    _RelayDriverSingleSessionQuery = _Tuple[niswitch.Session, str]
    _RelayDriverMultipleSessionQuery = _Tuple[_Tuple[niswitch.Session, ...], _StringTuple]

    _CustomSingleSessionQuery = _Tuple[_PinQueryContext, _Any, str, str]
    _CustomMultipleSessionQuery = _Tuple[
        _PinQueryContext, _Tuple[_Any, ...], _StringTuple, _StringTuple
    ]


class SemiconductorModuleContext:
    _sessions = {}

    def __init__(self, tsm_com_obj):
        """
        Args:
            tsm_com_obj: TestStand Semiconductor Module context object passed to Python from
                TestStand
        """

        self._context = nitsm._pinmapinterfaces.ISemiconductorModuleContext(tsm_com_obj)
        self._context._oleobj_ = tsm_com_obj._oleobj_.QueryInterface(
            self._context.CLSID, pythoncom.IID_IDispatch
        )

    # General and Advanced

    def get_pin_names(
        self,
        instrument_type_id: "_InstrTypeIdArg" = nitsm.enums.InstrumentTypeIdConstants.ANY,
        capability: "_CapabilityArg" = nitsm.enums.Capability.ALL,
    ) -> "_Tuple[_StringTuple, _StringTuple]":
        """
        Returns all DUT and system pins available in the Semiconductor Module context that are
        connected to an instrument of the type you specify in the instrument_type_id. This method
        returns only the pins specified on the Options tab of the Semiconductor Multi Test step.
        Pass an empty string to instrument_type_id to return all available pins.

        Args:
            instrument_type_id: Specifies the type of instrument for which you want to return DUT
                and system pins. All instruments defined in the pin map specify an associated type
                ID. The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type
                IDs for instrument types that TSM supports natively. For all other types of
                instruments, you must define a type ID for the instrument in the pin map file.
                Typically, this type ID is an instrument driver name or other ID that is common for
                instruments that users program in a similar way. Pass InstrumentTypeIdConstants.ANY
                to include pins from all instruments.
            capability: Limits the filtered pins to those connected to a channel that defines the
                capability you specify. Use capability to differentiate between pins in the same
                instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and
                PFI lines. If a pin is connected to channels in which the capability is defined only
                for a subset of sites, the method raises an exception. Pass Capability.ALL to return
                all pins that match instrument_type_id.

        Returns:
            dut_pins: Returns a tuple of strings that contains the DUT pins in the Semiconductor
                Module context that are connected to an instrument of the type you specify in the
                instrument_type_id.
            system_pins: Returns a tuple of strings that contains the system pins in the
                Semiconductor Module context that are connected to an instrument of the type you
                specify in the instrument_type_id.
        """

        if isinstance(instrument_type_id, nitsm.enums.InstrumentTypeIdConstants):
            instrument_type_id = instrument_type_id.value
        if isinstance(capability, nitsm.enums.Capability):
            capability = capability.value
        return self._context.GetPinNames(instrument_type_id, capability, [], [])

    def filter_pins_by_instrument_type(
        self,
        pins: "_Sequence[str]",
        instrument_type_id: "_InstrTypeIdArg",
        capability: "_CapabilityArg",
    ) -> "_StringTuple":
        """
        Filters pins by instrument_type_id. Pass a list of all pins or pin groups to return the pins
        connected to instruments of the type you specify in the instrument_type_id. If no pins are
        connected to instruments of the type you specify in instrument_type_id, this method returns
        an empty tuple. The return value is a tuple subset of pin names in pins that are connected
        to an instrument of the filtered instrument_type_id.

        Args:
            pins: A sequence of pins or pin groups to filter. The sequence must contain only pins or
                pin groups that are included in the Semiconductor Module context.
            instrument_type_id: The type of instrument for which you want to return DUT and system
                pins. All instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way. Pass InstrumentTypeIdConstants.ANY to include pins
                from all instruments.
            capability: Limits the filtered pins to those connected to a channel that defines the
                capability you specify. Use capability to differentiate between pins in the same
                instrument with different capabilities, such as NI-HSDIO Dynamic DIO channels and
                PFI lines. If a pin is connected to channels in which the capability is defined only
                for a subset of sites, the method raises an exception. Pass Capability.ALL to return
                all elements in pins that match instrument_type_id.

        Returns:
            Returns a tuple subset of pin names in the pins that are connected to an instrument of
            the filtered instrument_type_id.
        """

        if isinstance(instrument_type_id, nitsm.enums.InstrumentTypeIdConstants):
            instrument_type_id = instrument_type_id.value
        if isinstance(capability, nitsm.enums.Capability):
            capability = capability.value
        return self._context.FilterPinsByInstrumentType(pins, instrument_type_id, capability)

    def get_pins_in_pin_groups(self, pin_groups: "_PinsArg") -> "_StringTuple":
        """
        Returns a tuple of pins contained in the pin group(s) you specify in the pin_group(s).

        Args:
            pin_groups: A pin group or a sequence of pin groups. The pin group(s) must contain only
                pin groups that are included in the Semiconductor Module context.
        """

        if isinstance(pin_groups, str):
            pin_groups = [pin_groups]
        return self.filter_pins_by_instrument_type(pin_groups, "", "")

    @property
    def site_numbers(self) -> "_Tuple[int, ...]":
        """
        Returns the site numbers in the Semiconductor Module context. The site numbers can be
        different each time a step executes because some sites might not be active. The site numbers
        are in numerical order.
        """

        return self._context.SiteNumbers

    # Site and Global Data

    def set_site_data(self, data_id: str, data: "_Sequence[_Any]") -> None:
        """
        Associates a data item with each site. You can associate data with all sites or with the
        sub-set of sites in the Semiconductor Module context. You can use this method to store
        per-site data you initialize in a central location but access within each site. The data
        item is accessible from a process model controller execution and the site with which the
        data is associated. This method supports only basic data types and sequences of basic
        data types that can be represented by a COM VARIANT.

        Args:
            data_id: A unique ID to distinguish the data.
            data: A sequence of data with one element for each site in the system or one element for
                each site in the Semiconductor Module context. If the sequence is None or empty, the
                method deletes any data with the specified data_id if it exists. If the sequence
                contains data for each site in the Semiconductor Module context, each item in the
                sequence contains data for the site specified by the corresponding item in the
                site_numbers property.
        """

        return self._context.SetSiteData(data_id, data)

    def get_site_data(self, data_id: str) -> "_Tuple[_Any, ...]":
        """
        Returns per-site data that a previous call to the set_site_data method stores. The returned
        tuple contains the data the Semiconductor Module context stores for each site in the same
        order as the sites that the site_numbers property returns. Raises an exception if a data
        item with the specified data_id does not exist for every site in the Semiconductor Module
        context. Use the site_data_exists method to determine if the specified data_id exists.

        Args:
            data_id: The unique ID to distinguish the data. This parameter must match a value you
                specify in a call to the set_site_data method.
        """

        return self._context.GetSiteData(data_id)

    def site_data_exists(self, data_id: str) -> bool:
        """
        Returns a Boolean value indicating whether site data exists for the data ID specified by the
        data_id . Raises an exception if a data item with the specified data_id exists for some, but
        not all, sites in the Semiconductor Module context.

        Args:
            data_id: A unique ID to distinguish the data.
        """

        return self._context.SiteDataExists(data_id)

    def set_global_data(self, data_id: str, data: "_Any") -> None:
        """
        Associates a data item with a data_id. You can use this method to store data you initialize
        in a central location but access from multiple sites. The data item is accessible from a
        process model controller execution and all of its test socket executions. This method
        supports only basic data types and sequences of basic data types that can be represented by
        a COM VARIANT.

        Args:
            data_id: A unique ID to distinguish the data.
            data: A data item to store and later retrieve using the specified data_id . If the data
                item is None, the method deletes the data with the specified data_id if it exists.
        """

        return self._context.SetGlobalData(data_id, data)

    def get_global_data(self, data_id: str) -> "_Any":
        """
        Returns a global data item that a previous call to the set_global_data method stores. Throws
        an exception if no data item with the specified data_id exists. Use the global_data_exists
        method to determine if the specified data_id exists.

        Args:
            data_id: The unique ID to distinguish the data. This parameter must match a value you
                specify in a call to the set_global_data method.
        """

        return self._context.GetGlobalData(data_id)

    def global_data_exists(self, data_id: str) -> bool:
        """
        Returns a Boolean value indicating whether global data exists for the data ID specified by
        the data_id.

        Args:
            data_id: A unique ID to distinguish the data.
        """

        return self._context.GlobalDataExists(data_id)

    # NI-Digital

    def get_all_nidigital_instrument_names(self) -> "_StringTuple":
        """
        Returns a tuple of instrument names and comma-separated lists of instrument names that
        belong to the same group for all NI-Digital Pattern instruments in the Semiconductor Module
        context. You can use the instrument names and comma-separated lists of instrument names to
        open driver sessions.
        """

        return self._context.GetNIDigitalPatternInstrumentNames()

    def set_nidigital_session(self, instrument_name: str, session: "nidigital.Session") -> None:
        """
        Associates an instrument session with an NI-Digital Pattern instrument_name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument_name.
        """

        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDigitalPatternSession(instrument_name, session_id)

    def get_all_nidigital_sessions(self) -> "_Tuple[nidigital.Session, ...]":
        """
        Returns all NI-Digital Pattern instrument sessions in the Semiconductor Module context. You
        can use instrument sessions to close driver sessions.
        """

        session_ids = self._context.GetNIDigitalPatternSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_nidigital_session_for_ppmu(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalSingleSessionQuery":
        """
        Returns the NI-Digital Pattern session and pin_set_string required to perform PPMU
        operations on pin(s). If more than one session is required to access the pin(s), the method
        raises an exception. Each group of NI-Digital Pattern instruments in the pin map creates a
        single instrument session.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to session and pin_set_string.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-Digital Pattern instrument session for the instruments connected
                to pin(s) for all sites in the Semiconductor Module context.
            pin_set_string: Returns the pin set string for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. The pin set is
                specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern
                driver. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the string and is identified by one
                of the site/pin combinations to which it is connected.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, pin_set_string, _ = self._context.GetNIDigitalPatternSession_2(
                pins, 0, "", ""
            )
        else:
            session_id, pin_set_string, _ = self._context.GetNIDigitalPatternSession(
                pins, 0, "", ""
            )
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, pin_set_string

    def pins_to_nidigital_sessions_for_ppmu(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalMultipleSessionQuery":
        """
        Returns the NI-Digital Pattern sessions and pin_set_strings required to perform PPMU
        operations on pin(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to sessions and
                pin_set_strings.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            pin_set_strings: Returns the pin set strings for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. The pin sets
                are specified by site and pin e.g. "site0/A" as expected by the NI-Digital Pattern
                driver. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the string and is identified by one
                of the site/pin combinations to which it is connected.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, pin_set_strings, _ = self._context.GetNIDigitalPatternSessions_3(
                pins, [], [], []
            )
        else:
            session_ids, pin_set_strings, _ = self._context.GetNIDigitalPatternSessions_2(
                pins, [], [], []
            )
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, pin_set_strings

    def pins_to_nidigital_session_for_pattern(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalSingleSessionQuery":
        """
        Returns the NI-Digital Pattern session and site_list required to perform pattern operations
        for patterns that use the pin(s). If more than one session is required to access the pin(s),
        the method raises an exception. Each group of NI-Digital Pattern instruments in the pin map
        creates a single instrument session.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to session and site_list.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-Digital Pattern instrument session for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            site_list: Returns a string that is a comma-separated list of sites (e.g. "site0,site1")
                that correspond to the sites in the Semiconductor Module context. This site_list is
                needed as an input to certain NI-Digital Pattern driver calls.
        """

        if isinstance(pins, str):
            session_id, _, site_list = self._context.GetNIDigitalPatternSession_2(pins, 0, "", "")
        else:
            session_id, _, site_list = self._context.GetNIDigitalPatternSession(pins, 0, "", "")
        pin_query_context = nitsm.pinquerycontexts.DigitalPatternPinQueryContext(
            self._context, pins, site_list
        )
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, site_list

    def pins_to_nidigital_sessions_for_pattern(
        self, pins: "_PinsArg"
    ) -> "_NIDigitalMultipleSessionQuery":
        """
        Returns the NI-Digital Pattern sessions and site_lists required to perform pattern
        operations for patterns that use the pin(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to sessions and site_lists.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-Digital Pattern instrument sessions for the instruments
                connected to pin(s) for all sites in the Semiconductor Module context.
            site_lists: Returns a tuple of comma-separated lists of sites (e.g. "site0,site1") that
                correspond to the sites in the Semiconductor Module context. This site_list is
                needed as an input to certain NI-Digital Pattern driver calls.
        """

        if isinstance(pins, str):
            session_ids, _, site_lists = self._context.GetNIDigitalPatternSessions_3(
                pins, [], [], []
            )
        else:
            session_ids, _, site_lists = self._context.GetNIDigitalPatternSessions_2(
                pins, [], [], []
            )
        pin_query_context = nitsm.pinquerycontexts.DigitalPatternPinQueryContext(
            self._context, pins, site_lists
        )
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, site_lists

    @property
    def pin_map_file_path(self) -> str:
        """
        The absolute path to the pin map file for this Semiconductor Module context.
        """

        return self._context.PinMapPath

    @property
    def nidigital_project_specifications_file_paths(self) -> "_StringTuple":
        """
        The absolute paths to the Specifications files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        """

        return self._context.GetDigitalPatternProjectSpecificationsFilePaths()

    @property
    def nidigital_project_levels_file_paths(self) -> "_StringTuple":
        """
        The absolute paths to the Levels file in the Digital Pattern Project associated with this
        Semiconductor Module context.
        """

        return self._context.GetDigitalPatternProjectLevelsFilePaths()

    @property
    def nidigital_project_timing_file_paths(self) -> "_StringTuple":
        """
        The absolute paths to the Timing files in the Digital Pattern Project associated with this
        Semiconductor Module context.
        """

        return self._context.GetDigitalPatternProjectTimingFilePaths()

    @property
    def nidigital_project_pattern_file_paths(self) -> "_StringTuple":
        """
        The absolute paths to the Pattern files in the Digital Pattern Project associated with this
        Semiconductor Module context.
        """

        return self._context.GetDigitalPatternProjectPatternFilePaths()

    @property
    def nidigital_project_source_waveform_file_paths(self) -> "_StringTuple":
        """
        The absolute paths to the Source Waveform files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        """

        return self._context.GetDigitalPatternProjectSourceWaveformFilePaths()

    @property
    def nidigital_project_capture_waveform_file_paths(self) -> "_StringTuple":
        """
        The absolute paths to the Capture Waveform files in the Digital Pattern Project associated
        with this Semiconductor Module context.
        """

        return self._context.GetDigitalPatternProjectCaptureWaveformFilePaths()

    # NI-DCPower

    def get_all_nidcpower_resource_strings(self) -> "_StringTuple":
        """
        Returns the resource strings associated with each channel group in the Semiconductor Module
        context. A resource string is a comma-separated list of NI-DCPower resources, where each
        resource is defined by the <instrument>/<channel> associated with the NI-DCPower channel
        group. You can use the resource strings to open driver sessions. The same session controls
        all resources within the same resource string. This method supports only DC Power
        instruments defined with ChannelGroups in the pin map.

        Returns:
            Returns a tuple of the NI-DCPower resource strings.
        """

        return self._context.GetNIDCPowerResourceStrings()

    def set_nidcpower_session(self, resource_string: str, session: "nidcpower.Session"):
        """
        Associates an NI-DCPower session with all resources of an NI-DCPower resource_string. This
        method supports only DC Power instruments defined with ChannelGroups in the pin map.

        Args:
            resource_string: The resource string associated with the corresponding session. The
                resource string is a comma-separated list of resources, where each resource is
                defined as <instrument>/<channel>.
            session: The NI-DCPower session for the corresponding resource_string.
        """

        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        # Instrument alarms are not yet supported in Python
        self._context.SetNIDCPowerSession_2(resource_string, session_id, [], 0)

    def get_all_nidcpower_sessions(self) -> "_Tuple[nidcpower.Session, ...]":
        """
        Returns all NI-DCPower instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """

        session_ids = self._context.GetNIDCPowerSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_nidcpower_session(self, pins: "_PinsArg") -> "_NIDCPowerSingleSessionQuery":
        """
        Returns the NI-DCPower session and channel_string required to access the pin(s) on all sites
        in the Semiconductor Module context. If multiple sessions are required to access the
        pin(s), the method raises an exception.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session and
                channel_string.

        Returns:
            pin_query_context: An object that tracks the session and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            session: Returns the NI-DCPower instrument session for the instruments and channels
                connected to pin(s) for all sites in the Semiconductor Module context.
            channel_string: Returns the channel string for the NI-DCPower session required to access
                the pin(s) for all sites in the Semiconductor Module context. The channel string is
                a comma-separated list of resources, where each resource is defined as
                <instrument>/<channel>.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_string = self._context.GetNIDCPowerSession(pins, 0, "")
        else:
            session_id, channel_string = self._context.GetNIDCPowerSession_2(pins, 0, "")
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_string

    def pins_to_nidcpower_sessions(self, pins: "_PinsArg") -> "_NIDCPowerMultipleSessionQuery":
        """
        Returns the NI-DCPower sessions and channel_strings required to access the pin(s).

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to sessions and
                channel_strings.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements and extract data from a set of
                measurements.
            sessions: Returns the NI-DCPower instrument sessions for the instruments and channel
                resources connected to pin(s) for all sites in the Semiconductor Module context.
            channel_strings: Returns the channel strings for each instrument session required to
                access the pin(s) for all sites in the Semiconductor Module context. Each channel
                string is a comma-separated list of channels, where each channel is defined as
                <instrument>/<channel>.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_strings = self._context.GetNIDCPowerSessions_2(pins, [], [])
        else:
            session_ids, channel_strings = self._context.GetNIDCPowerSessions_3(pins, [], [])
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, channel_strings

    # NI-DAQmx

    def get_all_nidaqmx_task_names(self, task_type: str) -> "_Tuple[_StringTuple, _StringTuple]":
        """
        Returns a tuple of all NI-DAQmx task names and channel lists in the Semiconductor Module
        context. You can use the task names to create DAQmx tasks.

        Args:
            task_type: Specifies the type of NI-DAQmx task to return. Use an empty string to obtain
                the names of all tasks regardless of task type.

        Returns:
            task_names: Returns a tuple of the NI-DAQmx task names.
            channel_lists: Returns a tuple of the NI-DAQmx physical channel names for all channels
                in the Semiconductor Module context.
        """

        return self._context.GetNIDAQmxTaskNames(task_type, [])

    def set_nidaqmx_task(self, task_name: str, task: "nidaqmx.Task") -> None:
        """
        Associates an NI-DAQmx task with an NI-DAQmx task name defined in the pin map.

        Args:
            task_name: The task name in the pin map file for the corresponding task.
            task: The DAQmx task for the corresponding task name.
        """

        task_id = id(task)
        SemiconductorModuleContext._sessions[task_id] = task
        return self._context.SetNIDAQmxTask(task_name, task_id)

    def get_all_nidaqmx_tasks(self, task_type: str) -> "_Tuple[nidaqmx.Task, ...]":
        """
        Returns a tuple of all NI-DAQmx tasks in the Semiconductor Module context whose task type
        matches task_type. You can use tasks to perform NI-DAQmx operations.

        Args:
            task_type: Specifies the type of NI-DAQmx task to return. Use an empty string to obtain
                the names of all tasks regardless of task type.
        """

        task_ids = self._context.GetNIDAQmxTasks(task_type)
        return tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)

    def pins_to_nidaqmx_task(self, pins: "_PinsArg") -> "_NIDAQmxSingleSessionQuery":
        """
        Returns the NI-DAQmx task and available channels list required to access the pin(s). If more
        than one task is required, the method raises an exception.

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to a task.

        Returns:
            pin_query_context: An object that tracks the task associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            task: Returns the NI-DAQmx task associated with the pin(s) or pin group(s) for all sites
                in the Semiconductor Module context.
            channel_list: Returns the comma-separated list of channels in the task associated with
                the pin(s) or pin group(s) for all sites in the Semiconductor Module context. Use
                the channel list to set the channels to read from for an input task or as an input
                to one of the per task data methods associated with this pin query context for an
                output task. If any of the pins are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            task_id, channel_list = self._context.GetNIDAQmxTask(pins, 0, "")
        else:
            task_id, channel_list = self._context.GetNIDAQmxTask_2(pins, 0, "")
        task = SemiconductorModuleContext._sessions[task_id]
        return pin_query_context, task, channel_list

    def pins_to_nidaqmx_tasks(self, pins: "_PinsArg") -> "_NIDAQmxMultipleSessionQuery":
        """
        Returns the NI-DAQmx tasks and available channels lists required to access the pin(s) or pin
        group(s).

        Args:
            pins: The name of the pin(s) or pin group(s) to translate to a set of tasks.

        Returns:
            pin_query_context: An object that tracks the tasks associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            tasks: Returns the NI-DAQmx tasks associated with the pin(s) or pin group(s) for all
                sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated lists of channels in the tasks associated
                with the pin(s) or pin group(s) for all sites in the Semiconductor Module context.
                Use the channel lists to set the channels to read from for input tasks or as an
                input to one of the per task data methods associated with this pin query context for
                output tasks. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            task_ids, channel_lists = self._context.GetNIDAQmxTasks_2(pins, [], [])
        else:
            task_ids, channel_lists = self._context.GetNIDAQmxTasks_3(pins, [], [])
        tasks = tuple(SemiconductorModuleContext._sessions[task_id] for task_id in task_ids)
        return pin_query_context, tasks, channel_lists

    # NI-DMM

    def get_all_nidmm_instrument_names(self) -> "_StringTuple":
        """
        Returns a tuple of all NI-DMM instrument names in the Semiconductor Module context. You can
        use instrument names to open driver sessions.
        """

        return self._context.GetNIDmmInstrumentNames()

    def set_nidmm_session(self, instrument_name: str, session: "nidmm.Session") -> None:
        """
        Associates an instrument session with an NI-DMM instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        """

        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIDmmSession(instrument_name, session_id)

    def get_all_nidmm_sessions(self) -> "_Tuple[nidmm.Session, ...]":
        """
        Returns a tuple of all NI-DMM instrument sessions in the Semiconductor Module context. You
        can use instrument sessions to close driver sessions.
        """

        session_ids = self._context.GetNIDmmSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pin_to_nidmm_session(self, pin: str) -> "_NIDmmSingleSessionQuery":
        """
        Returns the NI-DMM session required to access the pin. If more than one session is required,
        the method raises an exception.

        Args:
            pin: The name of the pin to translate to an instrument session. If more than one session
            is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-DMM instrument session for the instrument connected to the pin
                for all sites in the Semiconductor Module context.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pin)
        session_id = self._context.GetNIDmmSession(pin)
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session

    def pins_to_nidmm_sessions(self, pins: "_PinsArg") -> "_NIDmmMultipleSessionQuery":
        """
        Returns the NI-DMM instrument sessions required to access the pin(s).

        Args:
            pins: The names of the pin(s) or pin group(s) to translate to instrument sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-DMM instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids = self._context.GetNIDmmSessions_2(pins)
        else:
            session_ids = self._context.GetNIDmmSessions_3(pins)
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions

    # NI-FGEN

    def get_all_nifgen_instrument_names(self) -> "_StringTuple":
        """
        Returns a tuple of all NI-FGEN instrument names in the Semiconductor Module context. You can
        use the instrument names to open driver sessions.
        """

        return self._context.GetNIFGenInstrumentNames()

    def set_nifgen_session(self, instrument_name: str, session: "nifgen.Session") -> None:
        """
        Associates an instrument session with an NI-FGEN instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        """

        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIFGenSession(instrument_name, session_id)

    def get_all_nifgen_sessions(self) -> "_Tuple[nifgen.Session, ...]":
        """
        Returns a tuple of all NI-FGEN instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """

        session_ids = self._context.GetNIFGenSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_nifgen_session(self, pins: "_PinsArg") -> "_NIFGenSingleSessionQuery":
        """
        Returns the NI-FGEN session and channel list required to access the pin(s). If more than one
        session is required, the method raises an exception.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session. If more than
                one session is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the session associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-FGEN instrument session for the instrument connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_list: Returns the comma-separated channel list for the instrument connected to
                the pin(s) for all sites in the Semiconductor Module context. If any of the pin(s)
                are connected to the same instrument channel for multiple sites, the channel appears
                only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_list = self._context.GetNIFGenSession(pins, 0, "")
        else:
            session_id, channel_list = self._context.GetNIFGenSession_2(pins, 0, "")
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pins_to_nifgen_sessions(self, pins: "_PinsArg") -> "_NIFGenMultipleSessionQuery":
        """
        Returns the NI-FGEN sessions and channel lists required to access the pin(s).

        Args:
            pins: The names of the pin(s) or pin group(s) to translate to sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-FGEN instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated channel lists for the instruments connected
                to the pin(s) for all sites in the Semiconductor Module context. If any of the
                pin(s) are connected to the same instrument channel for multiple sites, the channel
                appears only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_lists = self._context.GetNIFGenSessions_2(pins, [], [])
        else:
            session_ids, channel_lists = self._context.GetNIFGenSessions_3(pins, [], [])
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, channel_lists

    # NI-SCOPE

    def get_all_niscope_instrument_names(self) -> "_StringTuple":
        """
        Returns a tuple of instrument names and comma-separated lists of instrument names that
        belong to the same group for all NI-SCOPE instruments in the Semiconductor Module context.
        You can use the instrument names and comma-separated lists of instrument names to open
        driver sessions.
        """

        return self._context.GetNIScopeInstrumentNames()

    def set_niscope_session(self, instrument_name: str, session: "niscope.Session") -> None:
        """
        Associates an instrument session with an NI-SCOPE instrument name.

        Args:
            instrument_name: The instrument name in the pin map file for the corresponding session.
            session: The instrument session for the corresponding instrument name.
        """

        session_id = id(session)
        SemiconductorModuleContext._sessions[session_id] = session
        return self._context.SetNIScopeSession(instrument_name, session_id)

    def get_all_niscope_sessions(self) -> "_Tuple[niscope.Session, ...]":
        """
        Returns a tuple of all NI-SCOPE instrument sessions in the Semiconductor Module context.
        You can use instrument sessions to close driver sessions.
        """

        session_ids = self._context.GetNIScopeSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def pins_to_niscope_session(self, pins: "_PinsArg") -> "_NIScopeSingleSessionQuery":
        """
        Returns the NI-SCOPE session and channel list required to access the pin(s). If more than
        one session is required to access the pin(s), the method raises an exception. Each group of
        NI-SCOPE instruments in the pin map creates a single instrument session.

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to a session. If more than
                one session is required, the method raises an exception.

        Returns:
            pin_query_context: An object that tracks the session associated with this pin query. Use
                this object to publish measurements and extract data from a set of measurements.
            session: Returns the NI-SCOPE instrument session for the instrument connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_list: Returns the comma-separated channel list for the instrument connected to
                the pin(s) for all sites in the Semiconductor Module context. If any of the pin(s)
                are connected to the same instrument channel for multiple sites, the channel appears
                only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_list = self._context.GetNIScopeSession(pins, 0, "")
        else:
            session_id, channel_list = self._context.GetNIScopeSession_2(pins, 0, "")
        session = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session, channel_list

    def pins_to_niscope_sessions(self, pins: "_PinsArg") -> "_NIScopeMultipleSessionQuery":
        """
        Returns the NI-SCOPE sessions and channel lists required to access the pin(s).

        Args:
            pins: The name(s) of the pin(s) or pin group(s) to translate to sessions.

        Returns:
            pin_query_context: An object that tracks the sessions associated with this pin query.
                Use this object to publish measurements and extract data from a set of measurements.
            sessions: Returns the NI-SCOPE instrument sessions for the instruments connected to the
                pin(s) for all sites in the Semiconductor Module context.
            channel_lists: Returns the comma-separated channel lists for the instruments connected
                to the pin(s) for all sites in the Semiconductor Module context. If any of the
                pin(s) are connected to the same instrument channel for multiple sites, the channel
                appears only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_lists = self._context.GetNIScopeSessions_2(pins, [], [])
        else:
            session_ids, channel_lists = self._context.GetNIScopeSessions_3(pins, [], [])
        sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, sessions, channel_lists

    # Relay Driver

    def get_relay_driver_module_names(self) -> "_StringTuple":
        """
        Returns a tuple of all relay driver module names in the Semiconductor Module context. You
        can use the relay driver module names to open NI-SWITCH driver sessions for the relay driver
        modules.
        """

        return self._context.GetNIRelayDriverModuleNames()

    def get_relay_names(self) -> "_Tuple[_StringTuple, _StringTuple]":
        """
        Returns all site and system relays available in the Semiconductor Module context.

        Returns:
            site_relays: Returns a tuple of strings that contains the site relays in the
                Semiconductor Module context.
            system_relays: Returns a tuple of strings that contains the system relays in the
                Semiconductor Module context.
        """

        return self._context.GetRelayNames([], [])

    def set_relay_driver_niswitch_session(
        self, relay_driver_module_name: str, niswitch_session: "niswitch.Session"
    ) -> None:
        """
        Associates an NI-SWITCH session with a relay driver module.

        Args:
            relay_driver_module_name: The relay driver module name in the pin map file for the
                corresponding session.
            niswitch_session: The NI-SWITCH session for the corresponding relay driver module name.
        """

        session_id = id(niswitch_session)
        SemiconductorModuleContext._sessions[session_id] = niswitch_session
        return self._context.SetNIRelayDriverSession(relay_driver_module_name, session_id)

    def get_all_relay_driver_niswitch_sessions(self) -> "_Tuple[niswitch.Session, ...]":
        """
        Returns a tuple of NI-SWITCH sessions for all relay driver modules in the Semiconductor
        Module context. You can use the NI-SWITCH sessions to close the relay driver module
        sessions.
        """

        session_ids = self._context.GetNIRelayDriverSessions()
        return tuple(SemiconductorModuleContext._sessions[session_id] for session_id in session_ids)

    def relays_to_relay_driver_niswitch_session(
        self, relays: "_PinsArg"
    ) -> "_RelayDriverSingleSessionQuery":
        """
        Returns the NI-SWITCH session and relay names required to access the relay(s) connected to a
        relay driver module. If more than one session is required to access the relay(s), the method
        raises an exception.

        Args:
            relays: The name(s) of the relay(s) or relay group(s) to translate to an NI-SWITCH
                session and NI-SWITCH relay names.

        Returns:
            niswitch_session: Returns the NI-SWITCH session for the relay driver module connected to
                the relay(s) for all sites in the Semiconductor Module context.
            niswitch_relay_names: Returns a comma-separated list of NI-SWITCH relay names for the
                relay driver module session connected to the relay(s) for all sites in the
                Semiconductor Module context.
        """

        if isinstance(relays, str):
            session_id, niswitch_relay_names = self._context.GetNIRelayDriverSession(relays, 0, "")
        else:
            session_id, niswitch_relay_names = self._context.GetNIRelayDriverSession_2(
                relays, 0, ""
            )
        niswitch_session = SemiconductorModuleContext._sessions[session_id]
        return niswitch_session, niswitch_relay_names

    def relays_to_relay_driver_niswitch_sessions(
        self, relays: "_PinsArg"
    ) -> "_RelayDriverMultipleSessionQuery":
        """
        Returns the NI-SWITCH sessions and relay names required to access the relay(s) connected to
        a relay driver module.

        Args:
            relays: The name(s) of the relay(s) or relay group(s) to translate to NI-SWITCH sessions
                and NI-SWITCH relay names.

        Returns:
            niswitch_sessions: Returns NI-SWITCH sessions for the relay driver modules connected to
                the relay(s) for all sites in the Semiconductor Module context.
            niswitch_relay_names: Returns comma-separated lists of NI-SWITCH relay names for the
                relay driver module sessions connected to the relay(s) for all sites in the
                Semiconductor Module context.
        """

        if isinstance(relays, str):
            session_ids, niswitch_relay_names = self._context.GetNIRelayDriverSessions_2(
                relays, [], []
            )
        else:
            session_ids, niswitch_relay_names = self._context.GetNIRelayDriverSessions_3(
                relays, [], []
            )
        niswitch_sessions = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return niswitch_sessions, niswitch_relay_names

    @staticmethod
    def _apply_relay_action(
        session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close
    ):
        from niswitch.enums import RelayAction

        for session_id_to_open, relay_name_to_open in zip(
            session_ids_for_open, relay_names_to_open
        ):
            session_to_open = SemiconductorModuleContext._sessions[session_id_to_open]
            session_to_open.relay_control(relay_name_to_open, RelayAction.OPEN)
        for session_id_to_close, relay_name_to_close in zip(
            session_ids_for_close, relay_names_to_close
        ):
            session_to_close = SemiconductorModuleContext._sessions[session_id_to_close]
            session_to_close.relay_control(relay_name_to_close, RelayAction.CLOSE)
        return None

    def _relay_wait(self, wait_seconds):
        if wait_seconds == 0.0:
            return None
        elif wait_seconds > 0.0:
            time.sleep(wait_seconds)
        else:
            self._context.ReportInvalidTimeToWait("wait_seconds")
        return None

    def apply_relay_configuration(self, relay_configuration: str, wait_seconds=0.0) -> None:
        """
        Performs the relay actions on the relays in the relay configuration.

        Args:
            relay_configuration: The name of the relay configuration to apply.
            wait_seconds: The time to wait, in seconds, for the relays to settle after performing
                all relay actions.
        """

        (
            session_ids_for_open,
            relay_names_to_open,
            session_ids_for_close,
            relay_names_to_close,
        ) = self._context.GetRelayDriverSessionsFromRelayConfiguration(
            relay_configuration, [], [], [], []
        )
        self._apply_relay_action(
            session_ids_for_open, relay_names_to_open, session_ids_for_close, relay_names_to_close
        )
        self._relay_wait(wait_seconds)
        return None

    def _control_relays_single_action(self, relays, relay_action, wait_seconds=0.0):
        niswitch_sessions, relay_names = self.relays_to_relay_driver_niswitch_sessions(relays)
        for niswitch_session, niswitch_relay_name in zip(niswitch_sessions, relay_names):
            niswitch_session.relay_control(niswitch_relay_name, relay_action)
        self._relay_wait(wait_seconds)
        return None

    def _control_relays_multiple_action(self, relays, relay_actions, wait_seconds=0.0):
        if len(relays) != len(relay_actions):
            self._context.ReportIncompatibleArrayLengths("relays", "relay_actions")
        else:
            relay_actions = [relay_action.value for relay_action in relay_actions]
            (
                session_ids_for_open,
                relay_names_to_open,
                session_ids_for_close,
                relay_names_to_close,
            ) = self._context.GetRelayDriverSessionsFromRelays(
                relays, relay_actions, [], [], [], []
            )
            self._apply_relay_action(
                session_ids_for_open,
                relay_names_to_open,
                session_ids_for_close,
                relay_names_to_close,
            )
            self._relay_wait(wait_seconds)
        return None

    def control_relays(
        self,
        relays: "_PinsArg",
        relay_actions: "_Union[niswitch.RelayAction, _Sequence[niswitch.RelayAction]]",
        wait_seconds=0.0,
    ) -> None:
        """
        Performs the relay action(s) on the relay(s).

        Args:
            relays: The name(s) of the relay(s) or relay group(s) that identify the relays.
            relay_actions: The action(s) to perform on all identified relays.
            wait_seconds: The time to wait, in seconds, for the relay(s) to settle after performing
                the relay action(s).
        """

        if isinstance(relay_actions, (list, tuple)):
            return self._control_relays_multiple_action(relays, relay_actions, wait_seconds)
        else:
            return self._control_relays_single_action(relays, relay_actions, wait_seconds)

    # Custom Instruments

    def get_custom_instrument_names(
        self, instrument_type_id: "_InstrTypeIdArg"
    ) -> "_Tuple[_StringTuple, _StringTuple, _StringTuple]":
        """
        Returns the channel_group_ids and associated instrument_names and channel_lists of all
        instruments of type instrument_type_id defined in the Semiconductor Module context. You can
        use instrument_names, channel_group_ids, and channel_lists to open driver sessions. The
        instrument_names, channel_group_ids, and channel_lists return values always return the same
        number of elements. Instrument names repeat in instrument_names if the instrument has
        multiple channel groups.

        Args:
            instrument_type_id: The type of instrument for which you want to return instrument
                definitions. All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs
                for instrument types that TSM supports natively. For all other types of instruments,
                you must define a type ID for the instrument in the pin map file. Typically, this
                type ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.

        Returns:
            instrument_names: Returns the names of all instruments in the Semiconductor Module
                context that are of type instrument_type_id.
            channel_group_ids: Returns the IDs of all channel groups in the Semiconductor Module
                context that belong to an instrument of type instrument_type_id. For channels that
                do not belong to a channel group in the pin map, the Semiconductor Module creates a
                channel group with the same ID as the channel.
            channel_lists: Returns the channel lists for each element of channel_group_ids. Each
                channel list is a comma-separated list of channels.
        """

        return self._context.GetAllInstrumentDefinitions(instrument_type_id, [], [], [])

    def set_custom_session(
        self,
        instrument_type_id: str,
        instrument_name: str,
        channel_group_id: str,
        session_data: "_Any",
    ) -> None:
        """
        Associates a session with an instrument and channel group.

        Args:
            instrument_type_id: The type of instrument for which you want to set the session. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            instrument_name: The instrument name in the pin map file for the corresponding session.
                The instrument must be of type instrument_type_id.
            channel_group_id: The channel group in the pin map file for the corresponding session.
                For channels that do not belong to a channel group in the pin map, the Semiconductor
                Module creates a channel group with the same ID as the channel.
            session_data: The session for the corresponding instrument_name and channel_group_id.
        """

        session_id = id(session_data)
        SemiconductorModuleContext._sessions[session_id] = session_data
        self._context.SetSessionData(
            instrument_type_id, instrument_name, channel_group_id, session_id
        )
        return None

    def get_all_custom_sessions(
        self, instrument_type_id: "_InstrTypeIdArg"
    ) -> "_Tuple[_Tuple[_Any, ...], _StringTuple, _StringTuple]":
        """
        Returns all set sessions in the Semiconductor Module context that belong to instruments of
        type instrument_type_id.

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions.
                All instruments defined in the pin map specify an associated type ID.
                The nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs
                for instrument types that TSM supports natively. For all other types of instruments,
                you must define a type ID for the instrument in the pin map file. Typically, this
                type ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.

        Returns:
            session_data: Returns a tuple of session data set in the Semiconductor Module context.
            channel_group_ids: Returns the IDs of the channel groups on which session_data was
                stored. For channels that do not belong to a channel group in the pin map, the
                Semiconductor Module creates a channel group with the same ID as the channel.
            channel_lists: Returns the channel lists for each of the channel_group_ids. Each channel
                list is a comma-separated list of channels.
        """

        session_ids, channel_group_ids, channel_lists = self._context.GetAllSessionData(
            instrument_type_id, [], [], []
        )
        session_data = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return session_data, channel_group_ids, channel_lists

    def pins_to_custom_session(
        self, instrument_type_id: "_InstrTypeIdArg", pins: "_PinsArg"
    ) -> "_CustomSingleSessionQuery":
        """
        Returns the session in the Semiconductor Module context associated with pin(s).

        Args:
            instrument_type_id: The type of instrument for which you want to get a session. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            pins: The name(s) of the pin(s) or pin group(s) to translate to session_data,
                channel_group_id, and channel_list. The pin(s) must be connected to an instrument of
                type instrument_type_id.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements, extract data from a set of
                measurements, and create or rearrange waveforms.
            session_data: Returns the session data associated with pin(s).
            channel_group_id: Returns the ID of the channel group(s) that contain(s) the channels
                connected to pin(s). For channels that do not belong to a channel group in the pin
                map, the Semiconductor Module creates a channel group with the same ID as the
                channel.
            channel_list: Returns the channel list that corresponds to pin(s) associated with
                session_data and channel_group_id. The channel list is a comma-separated list of
                channels. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_id, channel_group_id, channel_list = self._context.GetSessionData_2(
                instrument_type_id, [pins], 0, "", ""
            )
        else:
            session_id, channel_group_id, channel_list = self._context.GetSessionData_2(
                instrument_type_id, pins, 0, "", ""
            )
        session_data = SemiconductorModuleContext._sessions[session_id]
        return pin_query_context, session_data, channel_group_id, channel_list

    def pins_to_custom_sessions(
        self, instrument_type_id: "_InstrTypeIdArg", pins: "_PinsArg"
    ) -> "_CustomMultipleSessionQuery":
        """
        Returns all sessions in the Semiconductor Module context associated with pin(s).

        Args:
            instrument_type_id: The type of instrument for which you want to get sessions. All
                instruments defined in the pin map specify an associated type ID. The
                nitsm.codemoduleapi.InstrumentTypeIdConstants class contains instrument type IDs for
                instrument types that TSM supports natively. For all other types of instruments, you
                must define a type ID for the instrument in the pin map file. Typically, this type
                ID is an instrument driver name or other ID that is common for instruments that
                users program in a similar way.
            pins: The name(s) of the pin(s) or pin group(s) to translate to session_data,
                channel_group_ids, and channel_lists. The pin(s) must be connected to instruments of
                type instrument_type_id.

        Returns:
            pin_query_context: An object that tracks the sessions and channels associated with this
                pin query. Use this object to publish measurements, extract data from a set of
                measurements, and create or rearrange waveforms.
            session_data: Returns a tuple of session data associated with pin(s).
            channel_group_ids: Returns the IDs of the channel groups that contain the channels
                connected to pin(s). For channels that do not belong to a channel group in the pin
                map, the Semiconductor Module creates a channel group with the same ID as the
                channel.
            channel_lists: Returns the channel lists that correspond to the pin(s) associated with
                session_data and channel_group_ids. Each channel list is a comma-separated list of
                channels. If any of the pin(s) are connected to the same instrument channel for
                multiple sites, the channel appears only once in the list.
        """

        pin_query_context = nitsm.pinquerycontexts.PinQueryContext(self._context, pins)
        if isinstance(pins, str):
            session_ids, channel_group_ids, channel_lists = self._context.GetSessionData(
                instrument_type_id, [pins], [], [], []
            )
        else:
            session_ids, channel_group_ids, channel_lists = self._context.GetSessionData(
                instrument_type_id, pins, [], [], []
            )
        session_data = tuple(
            SemiconductorModuleContext._sessions[session_id] for session_id in session_ids
        )
        return pin_query_context, session_data, channel_group_ids, channel_lists
