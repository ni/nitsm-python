import coverage


def pre_sequence_call(sequence_file_path, entry_point):
    coverage.process_startup()


def post_sequence_call():
    pass
