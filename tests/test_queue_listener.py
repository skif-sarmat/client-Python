from multiprocessing import Queue
from unittest import mock

import pytest

from reportportal_client.service_async import QueueListener


@pytest.fixture
def queue():
    return Queue()


@pytest.fixture
def queue_listener(queue):
    ql = QueueListener(queue, mock.MagicMock)
    ql.start()
    yield ql
    if ql._proccess is not None:
        ql.stop(nowait=True)


class TestQueueListener:

    def test_start__passed_right_argument__process_start(self, queue_listener):
        assert queue_listener._proccess.is_alive()

    def test_stop__passed_right_argument__process_stop(self, queue_listener):
        queue_listener.stop(nowait=True)

        assert queue_listener._proccess is None

    def test_monitor__send_message__message_consumed(self, queue_listener, queue):
        queue.put_nowait('Message')

        assert queue.empty()
