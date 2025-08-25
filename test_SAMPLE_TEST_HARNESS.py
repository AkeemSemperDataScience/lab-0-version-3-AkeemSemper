import pytest

'''
This is a sample test harness file for Quiz 0.

These test files will run automatically using pytest, and when using a repository that 
is setup for it, they will run automatically when you push to GitHub. This is commonly 
how code is tested in the real world, and it is a good idea to get used to it.

In your test files, you'll need to write some tests for each function you write in the
quiz_0_answer_sheet.py file. Each function should have multiple tests to ensure that it
works in all cases. Being able to write good tests is a skill that is important for any programmer, 
and it is something that can ultimately make it much easier to write good code, and tackle
more complex problems.

As a hint, before you start working, think about what would mean 'success' for each function.
If you can think of everything that function must do and not do, you can write tests to check
for those things. If you can write tests first, you can then write the function to make
those tests pass. This is called Test Driven Development (TDD) and is a common practice
in the software industry.

When you submit these, I'll add my own test file and run that instead. 
'''

# The functions below are imported from the quiz_0_answer_sheet.py file.
# This is the same as if you were to use these functions in a Jupyter notebook.
from quiz_0_answer_sheet import(
    numberAdder,
    vowelsInString
    )

#Functions that start with "test_" will be automatically run by pytest.
#The assert statement checks if the output of the function is equal to the expected value.
#If the assertion is false, pytest will report a failure.
#If the assertion is true, the test will pass.
def test_numberAdder_1():
    assert numberAdder(1, 2) == 3
def test_numberAdder_2():
    assert numberAdder(-56, 22) == -34
def test_numberAdder_3():
    assert numberAdder(0, 0) == 0
def test_numberAdder_4():
    assert numberAdder(100, 200) == 300

#You want to test each function with a variety of inputs to ensure it works in all cases.
#You want to make sure that you cover:
# - Each type of expected input (e.g., positive numbers, negative numbers, zero)
# - Edge cases (e.g., empty strings, very large numbers)
# - You'll cover this more later, but errors or unacceptable inputs (e.g., strings instead of numbers) 
def test_vowelsInString_1():
    assert vowelsInString("hello") == 2
def test_vowelsInString_2():
    assert vowelsInString("aeiou") == 5
def test_vowelsInString_3():
    assert vowelsInString("") == 0
def test_vowelsInString_4():
    assert vowelsInString("xyz") == 0
def test_vowelsInString_5():
    assert vowelsInString("I'm a student at Penn State") == 8
def test_vowelsInString_6():
    assert vowelsInString("921476") == 0
