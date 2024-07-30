import requests
import pytest


#In pytest the method name should always start with test and every test case should be inside a method
#Python file name should also strat with test
#To det more detailed output on the console use verbose -v
#Print statements are by default omitted by pytest, however if you want to print them use -s example "pytest -v -s"
#pytest.mark.skip is used to forcefully skip a test case
#pytest.mark.skipif(condition, reason = "")--> Skips if the condition fails
# Using pytest if you want to run any one specific test case use -k followed by the test case name# for example - pytest -s -v -k test_TC001,
#To run those test for which the test case name has TC00 then you should write command as mentioned - "pytest -v -s -k TC0"(minimum three letters are required to pick the pattern like TC0)cd
a = 19

# @pytest.mark.skip("Skipping for demo purpose")
def test_TC001():
    print("This is our pytest case code")
    return

# @pytest.mark.skipif(a<20, reason="Skipping as a value is less than 20")
def test_TC002():
    print("This is a second test case in first file")
    return

def test_C003():
    print("this is the third test case in the first file")
    return