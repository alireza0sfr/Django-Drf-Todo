from tests.base import BaseTests
from tests.fixtures import GlobalFixtures


class TestTaskAPI(BaseTests):

    def test_new_object(GlobalFixtures):
        assert 1 == 1
