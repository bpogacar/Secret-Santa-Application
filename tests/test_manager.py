import pytest
from app.manager import NameListManager

def test_add_name():
    manager = NameListManager()
    manager.add_name("Alice")
    assert "Alice" in manager.get_names()

def test_remove_name():
    manager = NameListManager(nameList={"Alice"})
    manager.remove_name("Alice")
    assert "Alice" not in manager.get_names()

def test_add_constraint():
    manager = NameListManager(nameList={"Alice", "Bob"})
    manager.add_constraint("Alice", "Bob")
    assert ("Alice", "Bob") in manager.get_constraints()

def test_generate_pairs():
    manager = NameListManager(nameList={"Alice", "Bob", "Charlie"})
    pairs = manager.generate_pairs()
    assert pairs is not None
    assert len(pairs) == len(manager.get_names())