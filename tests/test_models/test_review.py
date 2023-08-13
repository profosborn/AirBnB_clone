#!/usr/bin/python3
"""defines all unnittest tests for the models/review.py module"""
import unittest
import os
import models
import pep8
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """unittest tests for the Review model class"""

    def test_style_check(self):
        """Test for pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
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

    def test_review_is_subclass_of_BaseModel(self):
        self.assertTrue(issubclass(Review().__class__, BaseModel), True)

    def test_review_for_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_review_instantiation_no_args(self):
        """Tests the Review instantiation with no parameters"""
        self.assertEqual(Review, type(Review()))

    def test_review_instance_stored(self):
        """Tests that a new Review instance is stored"""
        self.assertIn(Review(), models.storage.all().values())

    def test_review_id(self):
        """tests the type of a Review instance id"""
        self.assertEqual(str, type(Review().id))

    def test_review_created_at_is_datetime(self):
        """test that the Review class attribute created_at is an instance
            of datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_review_updated_at_is_datetime(self):
        """test that the Review attribute updated_at is an
            instance of datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_name_attr_is_public_class_attr(self):
        """test that the Review class attribute,
            name is public class attribute"""
        model = Review()
        self.assertNotIn("name", model.__dict__)
        self.assertIn("id", dir(model))

    def test_review_instance_id_is_unique(self):
        """test that the Review instances ids are unique"""
        self.assertNotEqual(Review().id, Review().id)

    def test_review_created_at_attr_are_different(self):
        """tests that the Review created_at attributes for two
            instances are different"""
        self.assertLess(Review().created_at, Review().created_at)

    def test_review_updated_at_attr_are_different(self):
        """tests that the Review updated_at attribute for two
            instances are different"""
        self.assertLess(Review().updated_at, Review().updated_at)

    def test_unused_args(self):
        """test for unused args"""
        model = Review(None)
        self.assertNotIn(None, model.__dict__.values())

    def test_review_instantiation_with_kwargs(self):
        "tests the instantiation of the Review class with kwargs"
        dt = datetime.now().isoformat()
        kwargs = {"id": "121212", "created_at": dt, "updated_at": dt}
        model = Review(**kwargs)
        self.assertEqual(model.id, "121212")
        self.assertEqual(model.created_at.isoformat(), dt)
        self.assertEqual(model.updated_at.isoformat(), dt)

    def test_review_instantiation_with_None_kwargs(self):
        """test Review instatiation with a dictionary whose values are None"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_review_save_method_once(self):
        model = Review()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_review_save_method_twice(self):
        model = Review()
        updated_at_1 = model.updated_at
        model.save()
        updated_at_2 = model.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        model.save()
        updated_at_3 = model.updated_at
        self.assertLess(updated_at_2, updated_at_3)

    def test_review_save_method_with_None_arg(self):
        """tests the save method with None as argument"""
        model = Review()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_review_save_to_update_file(self):
        model = Review()
        model.save()
        model_id = f'{model.__class__.__name__}.{model.id}'
        with open("file.json", "r") as f:
            self.assertIn(model_id, f.read())

    def test_review_dict_type(self):
        self.assertTrue(dict, type(Review().to_dict()))

    def test_review_to_dict_has_valid_keys(self):
        model = Review()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())

    def test_review_to_dict_has_new_attrs(self):
        model = Review()
        model.added_name = "Holberton"
        model.added_number = 12345
        self.assertEqual("Holberton", model.added_name)
        self.assertEqual(12345, model.added_number)

    def test_review_to_dict_attrs_are_str(self):
        _dict = Review().to_dict()
        self.assertEqual(str, type(_dict["id"]))
        self.assertEqual(str, type(_dict["created_at"]))
        self.assertEqual(str, type(_dict["updated_at"]))

    def test_review_correct_dict_output(self):
        model = Review()
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

    def test_review_to_dict_and_magic_dict_methods(self):
        model = Review()
        self.assertNotEqual(model.to_dict(), model.__dict__)

    def test_review_to_dict_method_with_None_arg(self):
        model = Review()
        with self.assertRaises(TypeError):
            model.to_dict(None)


if __name__ == '__main__':
    unittest.main()
