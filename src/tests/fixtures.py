import pytest
import win32com.client
import win32com.client.selecttlb
import nitsm.codemoduleapi.tsmcontext


@pytest.fixture()
def standalone_tsm_context(request):
    published_data_reader_factory = win32com.client.Dispatch(
        'NationalInstruments.TestStand.SemiconductorModule.Restricted.PublishedDataReaderFactory'
    )
    standalone_tsm_context, published_data_reader = \
        published_data_reader_factory.NewSemiconductorModuleContext(request.param)
    tsm = nitsm.codemoduleapi.SemiconductorModuleContext(standalone_tsm_context)

    typelibs = win32com.client.selecttlb.FindTlbsWithDescription(
        'NI TestStand Semiconductor Module Standalone Semiconductor Module Context'
    )
    standalone_tsm_typelib = typelibs[0]

    published_data_reader = win32com.client.CastTo(
        published_data_reader, 'IPublishedDataReader', standalone_tsm_typelib
    )
    return tsm, published_data_reader
