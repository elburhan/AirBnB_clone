Airbnb Clone Project
Project Description
The Airbnb Clone Project is a web application development endeavor that aims to create a simplified copy of the Airbnb website. The project spans over the course of a year, with the goal of deploying a fully functional web application composed of a command interpreter, a front-end website, data storage, and an API for communication.

Command Interpreter
Description
The command interpreter is a crucial component of the Airbnb clone project. It provides a tool for manipulating data without a visual interface, similar to a Shell. The command interpreter allows users to interact with the system through commands, enabling the creation, updating, and deletion of objects.

How to Start
To start the command interpreter, run the console.py script.


$ ./console.py

How to Use
In interactive mode, you can enter commands directly into the console. In non-interactive mode, you can pass commands through standard input. The command interpreter recognizes various commands for managing objects, and the available commands can be displayed using the help command.

Examples
Interactive Mode
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
(hbnb) show User 1
(hbnb) update User 1 name "John Doe"
(hbnb) all
(hbnb) quit
Non-Interactive Mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

$ cat test_commands | ./console.py
(hbnb) create Place
(hbnb) show Place 1
(hbnb) quit

Unit Tests
All unit tests for the project are organized within the tests folder. The unittest module is used for writing tests. To execute all tests, use the following command:
$ python3 -m unittest discover tests

Alternatively, individual test files can be executed:
$ python3 -m unittest tests/test_models/test_base_model.py

Project Structure
The project follows a structured organization:

console.py: Entry point for the command interpreter.
models: Directory containing classes for different objects.
tests: Directory containing unit tests mirroring the project structure.
Execution Environment
Python Version: 3.8.5
Operating System: Ubuntu 20.04 LTS
Code Style
The code adheres to the PEP 8 style guidelines. Code style can be validated using the pycodestyle tool.


$ pycodestyle *.py models/ tests/

