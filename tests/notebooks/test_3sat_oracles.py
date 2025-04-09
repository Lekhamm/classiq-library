from tests.utils_for_testbook import (
    validate_quantum_program_size,
    validate_quantum_model,
    wrap_testbook,
)
from testbook.client import TestbookNotebookClient


@wrap_testbook("3sat_oracles", timeout_seconds=1800)
def test_notebook(tb: TestbookNotebookClient) -> None:

    for qmod in tb.ref("qmods"):
        validate_quantum_model(qmod)
        # TODO test quantum programs with transpilation is "none"

    # test notebook content
    for cl_time in tb.ref("cl_times"):
        assert cl_time < 30  # actual time is less than 15 sec for all models
