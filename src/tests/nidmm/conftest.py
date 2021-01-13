import pytest
import nidmm


@pytest.fixture
def simulated_nidmm_sessions(standalone_tsm_context):
    instrument_names = standalone_tsm_context.get_all_nidmm_instrument_names()
    sessions = [nidmm.Session(instrument_name, options={'Simulate': True})
                for instrument_name in instrument_names]
    for instrument_name, session in zip(instrument_names, sessions):
        standalone_tsm_context.set_nidmm_session(instrument_name, session)
    yield sessions
    for session in sessions:
        session.close()
