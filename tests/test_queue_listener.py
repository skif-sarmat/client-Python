from multiprocessing import Queue
from unittest import mock

import pytest

from reportportal_client.service_async import QueueListener


@pytest.fixture
def queue():
    return Queue()


@pytest.fixture
def queue_listener(queue):
    ql = QueueListener(queue, mock.MagicMock())
    ql.start()
    yield ql
    if ql._proccess is not None:
        ql.stop()


class TestQueueListener:

    def test_start__passed_right_argument__process_start(self, queue_listener):
        assert queue_listener._proccess.is_alive()

    def test_stop__passed_right_argument__process_stop(self, queue_listener):
        queue_listener.stop()

        assert queue_listener._proccess is None

    def test_monitor__send_message__message_consumed(self, queue_listener, queue):
        queue.put_nowait('Message')

        assert queue.empty()

    def test_monitor_send_message__handler_called(self, queue):
        q = Queue()
        client_mock = mock.MagicMock()
        client_mock.process_item.side_effect = lambda x: q.put_nowait(x)
        queue_listener = QueueListener(queue, client_mock)
        message = "test message"
        queue_listener.start()
        queue.put_nowait(message)

        received_message = q.get(timeout=5)

        assert received_message == message

        queue_listener.stop()
