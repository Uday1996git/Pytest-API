import pytest

#Make sure you have the test case names different
#To control the test execution we have the concept of tagging
#Use @pytest.mark."$(userDefinedName) for example - @pytest.mark.Smoke"
# to run a specific tagged test cases use the command - "pytest -s -v -m Smoke"
# To execute all the test cases that are not belonging to the mentioned tag the use = "pytest -s -v -m "not Smoke"" this command will run all the test cases that are not belonging to smoke
#Writing nultiple tags for a test vase - Yes you can have multiple tags for a test case
# To run more than one tag use - pytest -v -s -m "Smoke or Sanity"
#To run those test cases which have two tags for sure, for example in the test cases below I want to execute the test case which have both regression and smoke - pytest -v -s -m "Smoke or Regression"


# WHne the test cases are ran, we are seeinf few warning as the tags are custom tags and not registered with pytest
#To get rid of these warnings, we can use either "--disable-pytest-warnings" or by registering all these tags with pytest
#To register all the custom tags with pytest, Create a file called pytest.ini and make a section called [pytest] and under that section write all the custom tags declared
# for example :
#[pytest]
# markers =
#   Smoke: This is for smoke test tag
#   Sanity:  This is for Sanity Test Cases
# After that you can just run the tests without having to use --disable....

#Assertions -
# assert actual_result == expected_result, "Custom message if test fails"

actual_result = 'Testing'


@pytest.mark.Smoke
@pytest.mark.Regression
def test_TC001():
    print("This is my TC001_smoke and Regression test case")
    assert actual_result != 'Testing', "Both the fields are same"
    return

@pytest.mark.Sanity
def test_TC002():
    print("This is my TC002_Sanity test case")
    return

@pytest.mark.Smoke
def test_TC003():
    print("This is my TC003_smoke test case")
    return