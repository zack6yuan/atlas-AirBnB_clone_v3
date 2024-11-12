#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
import unittest

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id

class TestStorageMethods(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.state = State(name="California")
        self.state.save()

    def tearDown(self):
        """Tear down after tests"""
        storage.delete(self.state)

    def test_count_all(self):
        """Test count method for all objects"""
        all_objects_count = storage.count()
        self.assertIsInstance(all_objects_count, int)
        self.assertGreaterEqual(all_objects_count, 1)

    def test_count_state(self):
        """Test count method for State objects"""
        state_objects_count = storage.count(State)
        self.assertIsInstance(state_objects_count, int)
        self.assertGreaterEqual(state_objects_count, 1)

    def test_get_state(self):
        """Test get method for State object"""
        first_state_id = list(storage.all(State).values())[0].id
        state = storage.get(State, first_state_id)
        self.assertIsNotNone(state)
        self.assertEqual(state.id, first_state_id)

if __name__ == "__main__":
    unittest.main()
