from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority = PriorityQueue()

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority.search(22)
