import pytest
from app.manager import NameListManager

# Fixture to set up the NameListManager
@pytest.fixture
def manager():
    return NameListManager()

@pytest.fixture
def populated_manager():
    return NameListManager(
        nameList={"Alice", "Bob", "Charlie", "David"},
        constraints={("Alice", "Bob"), ("David", "Alice")},
    )

# Test: add_name
@pytest.mark.parametrize("name, expected", [
    (None, None),                     # Adding None (invalid input)
    ("", None),                       # Adding an empty string
    ("Alice", "Alice"),               # Adding a valid name
    ("A" * 1000, "A" * 1000),         # Adding a very long name
    ("Alice", None),                  # Adding a duplicate name
])
def test_add_name(manager, name, expected):
    result = manager.add_name(name)
    assert result == expected
    if expected:
        assert name in manager.get_names()
    else:
        assert name not in manager.get_names()

# Test: remove_name
@pytest.mark.parametrize("name_to_remove, expected", [
    ("Alice", "Alice"),      # Removing a valid name
    ("Eve", None),           # Removing a non-existent name
    (None, None),            # Removing None (invalid input)
])
def test_remove_name(populated_manager, name_to_remove, expected):
    result = populated_manager.remove_name(name_to_remove)
    assert result == expected
    if expected:
        assert name_to_remove not in populated_manager.get_names()
        

# Test: remove_associated_constraints
@pytest.mark.parametrize("name, remaining_constraints", [
    ("Alice", {("Bob", "Bob"), ("Charlie", "Charlie"), ("David", "David")}),
    ("Bob", {("Alice", "Alice"), ("Charlie", "Charlie"), ("David", "David"), ("David", "Alice")}),
    ("Eve", {("Alice", "Bob"), ("David", "Alice"), ("Alice", "Alice"),
             ("Bob", "Bob"), ("Charlie", "Charlie"), ("David", "David")}),
])
def test_remove_associated_constraints(populated_manager, name, remaining_constraints):
    populated_manager.remove_associated_constraints(name)
    assert populated_manager.get_constraints() == remaining_constraints

# Test: add_constraint
@pytest.mark.parametrize("giver, receiver, expected", [
    ("Alice", "Charlie", ("Alice", "Charlie")),  # Adding a valid constraint
    ("Alice", "Alice", None),                    # Adding a self-giving constraint (already exists)
    ("Alice", "Eve", None),                      # Adding a constraint with a non-existent name
])
def test_add_constraint(populated_manager, giver, receiver, expected):
    result = populated_manager.add_constraint(giver, receiver)
    assert result == expected
    if expected:
        assert (giver, receiver) in populated_manager.get_constraints()
    else:
        assert (giver, receiver) not in populated_manager.get_constraints()

# Test: remove_constraint
@pytest.mark.parametrize("giver, receiver, expected", [
    ("Alice", "Bob", ("Alice", "Bob")),       # Removing an existing constraint
    ("David", "Alice", ("David", "Alice")),   # Removing another existing constraint
    ("Alice", "Charlie", None),               # Removing a non-existent constraint
    ("Alice", "Eve", None),                   # Removing a constraint with a non-existent receiver
    ("Eve", "Bob", None),                     # Removing a constraint with a non-existent giver
])
def test_remove_constraint(populated_manager, giver, receiver, expected):
    result = populated_manager.remove_constraint(giver, receiver)
    assert result == expected
    if expected:
        assert (giver, receiver) not in populated_manager.get_constraints()


# Test: generate_pairs
@pytest.mark.parametrize("names, constraints", [
    ({"Alice", "Bob", "Charlie"}, set()),                                  # Simple valid case
    ({"Alice", "Bob", "Charlie"}, {("Alice", "Bob")}),                     # With one constraint
    ({"Alice", "Bob", "Charlie"}, {("Alice", "Bob"), ("Bob", "Charlie")}), # Multiple constraints
    ({"Alice", "Bob"}, {("Alice", "Bob"), ("Bob", "Alice")}),              # Impossible case
])
def test_generate_pairs(names, constraints):
    manager = NameListManager(nameList=names, constraints=constraints)
    pairs = manager.generate_pairs()
    if len(names) == 2 and constraints == {("Alice", "Bob"), ("Bob", "Alice")}:
        assert pairs is None  # Should not be able to generate pairs
    else:
        assert pairs is not None
        assert len(pairs) == len(names)
        for giver, receiver in pairs:
            assert giver != receiver
            assert (giver, receiver) not in constraints
