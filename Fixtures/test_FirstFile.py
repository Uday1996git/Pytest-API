import pytest
import LeetFixtureCode


#Before and After actions of test case can be put in to fixtures
#Write a method and all the required fixture code within that method and then tag it with below tag
#tag - @pytest.fixture() -->  use to define fixtures
#Pass the fixture method name as a argument for the test case to whcih you want the fixture to get executed
#Any code that is written before the yield that gets executed before the test case and anything after yield will be executed after that test case
#Mentioning the scope of the fixture "scope = "module", This tells that the before code needs to be executed only once at thet start of the module and once after end of the module

def pass_fixtureCode():
    LeetFixtureCode.demo_fixtures()
    return


def end_fixture():
    LeetFixtureCode.afterDemo_fixture()
    return


@pytest.fixture(scope='module')
def fixture_code():
    LeetFixtureCode.demo_fixtures()
    yield
    LeetFixtureCode.afterDemo_fixture()


@pytest.mark.Smoke
def test_TCF001(fixture_code):
    print("This is our Fixture test case")


@pytest.mark.Smoke
def test_TCF002(fixture_code):
    print("")
