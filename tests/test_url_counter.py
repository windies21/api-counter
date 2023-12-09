"""Test Url Counter."""

import os
import pytest
from pathlib import Path
from yirgachefe import logger

from url_counter.main import url_counter, pretty

TEST_DIR = Path(__file__).parent.joinpath("./samples")


@pytest.fixture(params=os.listdir(TEST_DIR))
def target_file(request):
    with open(TEST_DIR.joinpath(request.param), "r") as f:
        logger.debug(f'Try test with ({request.param})')
        yield f


class TestUrlCounter:
    def test_url_counter_sample1(self, target_file):
        url_count: dict = url_counter(target_file)
        logger.debug(pretty(url_count))
        for count in url_count:
            assert url_count.get(count, 0) > 0
