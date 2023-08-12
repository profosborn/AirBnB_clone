#!/usr/bin/python3
"""defines all unnittest tests for the models/base_model.py module"""
import unittest
import os
import models
import pep8
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest tests for the BaseModel model class"""

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, 'fix pep8')

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_place_for_doc(self):
        self.assertIsNotNone(BaseModel.__doc__)

    def test_base_model_instantiation_no_args(self):
        """Tests the BaseModel instantiation with no parameters"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_base_model_instance_stored(self):
        """Tests that a new BaseModel instance is stored"""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_base_model_id(self):
        """tests the type of a BaseModel instance id"""
        self.assertEqual(str, type(BaseModel().id))

    def test_base_model_created_at_is_datetime(self):
        """test that the BaseModel class attribute created_at is an instance
        of datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_base_model_updated_at_is_datetime(self):
        """test that the BaseModel class attribute updated_at is an
        instance of datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_base_model_name_attr_is_public_class_attr(self):
        """test that the BaseModel class attribute,
            name is public class attribute"""
        model = BaseModel()
        self.assertNotIn("name", model.__dict__)
        self.assertEqual(str, type(model.id))
        self.assertIn("id", dir(model))

    def test_base_model_instance_id_is_unique(self):
        """test that the BaseModel instances ids are unique"""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_base_model_created_at_attr_are_different(self):
        """tests that the BaseModel created_at attributes for two
            instances are different"""
        self.assertLess(BaseModel().created_at, BaseModel().created_at)

    def test_base_model_updated_at_attr_are_different(self):
        """tests that the BaseModel updated_at attribute for two
            instances are different"""
        self.assertLess(BaseModel().updated_at, BaseModel().updated_at)

    def test_unused_args(self):
        """test for unused args"""
        model = BaseModel(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_base_model_instantiation_with_kwargs(self):
        "tests the instantiation of the BaseModel class with kwargs"
        dt = datetime.now().isoformat()
        kwargs = {"id": "121212", "created_at": dt, "updated_at": dt}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "121212")
        self.assertEqual(model.created_at.isoformat(), dt)
        self.assertEqual(model.updated_at.isoformat(), dt)

    def test_base_model_instantiation_with_None_kwargs(self):
        """test BaseModel class instatiation with a dictionary
            whose values are None"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_base_model_save_method_once(self):
        model = BaseModel()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_base_model_save_method_twice(self):
        model = BaseModel()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        model.save()
        updated_at_3 = model.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_base_model_save_method_with_None_arg(self):
        """tests the save method with None as argument"""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_base_model_save_to_update_file(self):
        model = BaseModel()
        model.save()
        model_id = f'{model.__class__.__name__}.{model.id}'
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

    def test_base_model_dict_type(self):
        self.assertTrue(dict, type(BaseModel().to_dict()))

    def test_base_model_to_dict_has_valid_keys(self):
        model = BaseModel()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_base_model_to_dict_has_new_attrs(self):
        model = BaseModel()
        model.added_name = "Holberton"
        model.added_number = 12345
        self.assertEqual("Holberton", model.added_name)
        self.assertEqual(12345, model.added_number)

    def test_base_model_to_dict_attrs_are_str(self):
        _dict = BaseModel().to_dict()
        self.assertEqual(str, type(_dict["id"]))
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_base_model_correct_dict_output(self):
        model = BaseModel()
        dt = datetime.now()
        model.id = '121212'
        model.created_at = model.updated_at = dt

        new_dict = {
            'id': '121212',
            '__class__': model.__class__.__name__,
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertEqual(model.to_dict(), new_dict)

    def test_base_model_to_dict_and_magic_dict_methods(self):
        model = BaseModel()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_base_model_to_dict_method_with_None_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == '__main__':
    unittest.main()
