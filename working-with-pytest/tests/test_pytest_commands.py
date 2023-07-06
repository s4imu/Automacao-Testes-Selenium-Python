import pytest

# test.py -m @pytest.mark.mark_name
@pytest.mark.simulation
# Test Methods
class TestSimulation:
    def test_simulation_1(self):
        assert 1 == 1

    @pytest.mark.skip # To skip some tests in case
    def test_simulation_2(self):
        assert 1 == 1

# pytest -v to had more information about the test execution
# pytest test.py::func to run a single test
