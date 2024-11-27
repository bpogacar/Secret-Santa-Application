import pytest
from app.manager import NameListManager

'''
For each test run a case with bad input, extreme inputs (array size, 
constraint size, etc.), and normal level inputs.
'''

def test_add_name():
    '''
    Case 1: adding something that is not a string
    Case 2: adding an empty string
    Case 3: adding a normal name
    Case 4: adding a very long string
    Case 5: adding a name twice (adding a name that is already in the list)
    '''
    manager = NameListManager()
    manager.add_name("Alice")
    assert "Alice" in manager.get_names()

def test_remove_name():
    '''
    Case 1: removing something that is not a string
    Case 3: removing a name that is in the namelist
    Case 4: removing a name that is not in the namelist 
    '''
    manager = NameListManager(nameList={"Alice"})
    manager.remove_name("Alice")
    assert "Alice" not in manager.get_names()

def test_add_constraint():
    '''
    Case 1: 
    '''
    manager = NameListManager(nameList={"Alice", "Bob"})
    manager.add_constraint("Alice", "Bob")
    assert ("Alice", "Bob") in manager.get_constraints()

def test_generate_pairs():
    manager = NameListManager(nameList={"Alice", "Bob", "Charlie"})
    pairs = manager.generate_pairs()
    assert pairs is not None
    assert len(pairs) == len(manager.get_names())