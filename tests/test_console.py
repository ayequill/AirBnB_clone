import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.mock_stdout.close()
        self.patcher.stop()

    def test_create(self):
        with patch('builtins.input', side_effect=["create State"]):
            self.console.onecmd("create State")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_show(self):
        with patch('builtins.input', side_effect=["show State 12345"]):
            self.console.onecmd("show State 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_destroy(self):
        with patch('builtins.input', side_effect=["destroy State 12345"]):
            self.console.onecmd("destroy State 12345")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_all(self):
        with patch('builtins.input', side_effect=["all", "all State"]):
            self.console.onecmd("all")
            output_all = self.mock_stdout.getvalue().strip()

            self.console.onecmd("all State")
            output_state = self.mock_stdout.getvalue().strip()

            self.assertTrue(output_all)

    def test_update(self):
        with patch('builtins.input',
                   side_effect=["update State 12345 name Texas"]):
            self.console.onecmd("update State 12345 name Texas")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    def test_count(self):
        with patch('builtins.input', side_effect=["count State"]):
            self.console.onecmd("count State")
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

    # def test_quit(self):
    #     with self.assertRaises(SystemExit):
    #         self.console.onecmd("quit")

    # def test_eof(self):
    #     with self.assertRaises(SystemExit):
    #         self.console.onecmd("EOF")

    def test_emptyline(self):
        self.assertEqual(self.console.emptyline(), None)

    def test_help_quit(self):
        self.console.do_help("quit")
        output = self.mock_stdout.getvalue().strip()
        self.assertTrue(output)

    def test_help_create(self):
        self.console.do_help("create")
        output = self.mock_stdout.getvalue().strip()
        self.assertTrue(output)


# import unittest
# from unittest.mock import patch
# from io import StringIO
# from console import HBNBCommand

# class TestHBNBCommand(unittest.TestCase):

#     @patch('sys.stdout', new_callable=StringIO)
#     def test_create(self, mock_stdout):
#         cmd = HBNBCommand()
#         # Test create command with valid class name
#         cmd.do_create("BaseModel")
#         output = mock_stdout.getvalue().strip()
#         self.assertTrue(output)
#         self.assertTrue(len(output), 36)  # Assuming the output is the ID

#         # Test create command with missing class name
#         cmd.do_create("")
#         output = mock_stdout.getvalue().strip()
#         self.assertEqual(output, "** class name missing **")

#         # Test create command with non-existing class name
#         cmd.do_create("NonExistingClass")
#         output = mock_stdout.getvalue().strip()
#         self.assertEqual(output, "** class doesn't exist **")

#     @patch('sys.stdout', new_callable=StringIO)
#     def test_show(self, mock_stdout):
#         cmd = HBNBCommand()

#         # Test show command with valid class name and ID
#         cmd.do_show("BaseModel {}".format(mock_stdout.getvalue()))
#         output = mock_stdout.getvalue().strip()
#         self.assertTrue(output)
#         self.assertTrue("no instance found" not in output)

#         # Test show command with missing class name
#         cmd.do_show("")
#         output = mock_stdout.getvalue().strip()
#         self.assertEqual(output, "** class name missing **")

#         # Test show command with non-existing class name
#         cmd.do_show("NonExistingClass 1234-5678")
#         output = mock_stdout.getvalue().strip()
#         self.assertEqual(output, "** class doesn't exist **")

#         # Test show command with existing class name and missing ID
#         cmd.do_show("BaseModel")
#         output = mock_stdout.getvalue().strip()
#         self.assertEqual(output, "** instance id missing **")

#         # Test show command with existing class name and non-existing ID
#         cmd.do_show("BaseModel 1234-5678")
#         output = mock_stdout.getvalue().strip()
#         self.assertEqual(output, "** no instance found **")

# if __name__ == '__main__':
#     unittest.main()
