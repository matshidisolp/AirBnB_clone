import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.user import User
import json

class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up method to clean up the storage before each test."""
        storage._FileStorage__objects = {}
        storage.save()

    def tearDown(self):
        """Tear down method to clean up the storage after each test."""
        storage._FileStorage__objects = {}
        storage.save()

    def test_create_missing_class(self):
        """Test create command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create command with valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            self.assertIn("User." + output, storage.all().keys())

    def test_show_missing_class(self):
        """Test show command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show command with invalid instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid(self):
        """Test show command with valid class name and instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {user_id}")
            self.assertIn(user_id, f.getvalue().strip())

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy command with invalid instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid(self):
        """Test destroy command with valid class name and instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        self.assertIn("User." + user_id, storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {user_id}")
        self.assertNotIn("User." + user_id, storage.all().keys())

    def test_all_invalid_class(self):
        """Test all command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid_class(self):
        """Test all command with valid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn("User." + user_id, f.getvalue().strip())

    def test_all_no_class(self):
        """Test all command without class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertIn("User." + user_id, f.getvalue().strip())

    def test_update_missing_class(self):
        """Test update command with missing class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update InvalidClass")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update command with invalid instance ID."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attr_name(self):
        """Test update command with missing attribute name."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234")
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update command with missing attribute value."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234 first_name")
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_valid(self):
        """Test update command with valid attributes."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {user_id} first_name John")
        obj = storage.all()["User." + user_id]
        self.assertEqual(obj.first_name, "John")

    def test_update_dict(self):
        """Test update command with dictionary attributes."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f'update User {user_id} {{"first_name": "John", "age": 30}}')
        obj = storage.all()["User." + user_id]
        self.assertEqual(obj.first_name, "John")
        self.assertEqual(obj.age, 30)

if __name__ == '__main__':
    unittest.main()
