#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
from models import HBNBCommand


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_EOF(self):
        """ Test for EOF """
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    def test_quit(self):
        """ Test for quit """
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_id(self):
        """Test id"""
        self.assertEqual(self.obj.id, id)

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_Access(self):
        """Test r-w-x access to file"""
        self.assertTrue(os.access("models/engine/file_storage.py", os.R_OK))
        self.assertTrue(os.access("models/engine/file_storage.py", os.W_OK))
        self.assertFalse(os.access("models/engine/file_storage.py", os.X_OK))

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_no_file(self):
        """Test save method when the file does not exist"""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        self.storage.new(self.obj)
        self.storage.save()
        key = self.obj.__class__.__name__ + "." + self.obj.id
        with open(self.storage._FileStorage__file_path, "r") as f:
            self.assertIn(key, f.read())

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_Access(self):
        """Test r-w-x access to file"""
        self.assertTrue(os.access("models/engine/file_storage.py", os.R_OK))
        self.assertTrue(os.access("models/engine/file_storage.py", os.W_OK))
        self.assertFalse(os.access("models/engine/file_storage.py", os.X_OK))

    def test_fundocs(self):
        """Test if funtions have documentation"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_do_create(self):
        """Test the do_create method"""
        # Test with no arguments
        with self.assertRaises(SystemExit):
            self.console.onecmd("create")

        # Test with valid arguments
        self.console.onecmd(
            'create BaseModel name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.77 longitude=122.41')
        all_objs = storage.all()
        test_obj = list(all_objs.values())[-1]
        self.assertEqual(test_obj.__class__.__name__, 'BaseModel')
        self.assertEqual(test_obj.name, 'My little house')
        self.assertEqual(test_obj.number_rooms, 4)
        self.assertEqual(test_obj.number_bathrooms, 2)
        self.assertEqual(test_obj.max_guest, 10)
        self.assertEqual(test_obj.price_by_night, 300)
        self.assertEqual(test_obj.latitude, 37.77)
        self.assertEqual(test_obj.longitude, 122.41)

    def test_docstrings(self):
        """Test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()
        self.file_storage = FileStorage()

    def test_all(self):
        """Test the all method"""
        self.console.onecmd('all BaseModel')
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_create(self):
        """Test the create method"""
        self.console.onecmd('create BaseModel')
        self.assertIsInstance(self.file_storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
