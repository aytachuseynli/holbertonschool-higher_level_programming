===================================================
Tests for matrix_divided in 3-say_my_name.txt
===================================================

:param first_name: str
:param last_name: str
:return: str

>>> say_my_name = __import__('3-say_my_name').say_my_name

>>> say_my_name("John", "Smith")
My name is John Smith

>>> say_my_name("Walter", "White")
My name is Walter White

>>> say_my_name("Bob")
My name is Bob

>>> try:
...     say_my_name(12, "White")
... except Exception as e:
...     print(e)
first_name must be a string
