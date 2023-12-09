import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
import os


class TestHBNBCommand(unittest.TestCase):
    """
    Test the HBNBCommand class
    """
    def setUp(self):
        """
        Redirect stdout to capture print statements
        """
        self.console_out = StringIO()
        sys.stdout = self.console_out

    def tearDown(self):
        """
        Reset stdout back to normal
        """
        self.console_out.close()
        sys.stdout = sys.__stdout__

    @classmethod
    def tearDownClass(cls):
        """
        Clean up: Remove the JSON file created during tests
        """
        try:
            os.remove('BaseModel.json')
        except FileNotFoundError:
            pass

    def test_prompt(self):
        """
        Test the prompt property of HBNBCommand
        """
        self.assertEqual(HBNBCommand.prompt, '(hbnb) ')

    @patch('sys.stdin', StringIO("quit\n"))
    def test_quit(self):
        """
        Test the quit command
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().cmdloop()
        output = self.console_out.getvalue().strip()
        self.assertEqual(output, '')

    @patch('sys.stdin', StringIO("EOF\n"))
    def test_EOF(self):
        """
        Test the EOF command
        """
        with self.assertRaises(SystemExit):
            HBNBCommand().cmdloop()
        output = self.console_out.getvalue().strip()
        self.assertEqual(output, '')

    def test_emptyline(self):
        """
        Test the emptyline command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '')

    def test_create(self):
        """
        Test the create command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel\n')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)
            self.assertTrue(output.isalnum())
            self.assertTrue(len(storage.all()) == 1)

    def test_create_invalid_class(self):
        """
        Test the create command with an invalid class
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create InvalidClass\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        """
        Test the show command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('show BaseModel\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_class(self):
        """
        Test the show command with an invalid class
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('show InvalidClass 123\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_invalid_id(self):
        """
        Test the show command with an invalid instance id
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('show BaseModel invalid_id\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """
        Test the destroy command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('destroy BaseModel\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_class(self):
        """
        Test the destroy command with an invalid class
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('destroy InvalidClass 123\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_invalid_id(self):
        """
        Test the destroy command with an invalid instance id
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('destroy BaseModel invalid_id\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """
        Test the all command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('all\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, '')

    def test_all_invalid_class(self):
        """
        Test the all command with an invalid class
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('all InvalidClass\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        """
        Test the update command
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('update BaseModel\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_class(self):
        """
        Test the update command with an invalid class
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('update InvalidClass 123\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_invalid_id(self):
        """
        Test the update command with an invalid instance id
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('update BaseModel invalid_id\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_invalid_attribute(self):
        """
        Test the update command with an invalid attribute
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('update BaseModel 123 invalid_attr value\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_invalid_value(self):
        """
        Test the update command with an invalid value
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('update BaseModel 123 attr\n')
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_create_city(self):
        """
        Test the create command for City class
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd('create City\n')
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36)
            self.assertTrue(output.isalnum())
            self.assertTrue(len(storage.all()) == 2)  

if __name__ == '__main__':
    unittest.main()
