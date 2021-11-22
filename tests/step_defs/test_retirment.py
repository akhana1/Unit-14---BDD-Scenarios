import pytest
from pytest_bdd import scenarios, given, when, then, parser
import calculator


EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'birthYear': int,
    'birthMonth': int,
    'ageYear': int,
    'ageMonth': int,
    'retireMonth': int,
    'retireYear': int,
    'invalid inputs': int,
}


scenarios('../features/retirement.feature', example_converters=CONVERTERS)


@when(parsers.cfparse('Enter "{birthYear:Number}" for the birth year',
                      extra_types=EXTRA_TYPES))
@when('Enter "<birthYear>" for the birth year')
def birth_year(birthYear):
    age, month = retirement(birthYear)
    return age, month


@then(parsers.cfparse('Retirement age is "{ageYear:Number}" and '
                      '"{ageMonth}" months', extra_types=EXTRA_TYPES))
@then('Retirement age is "<ageYear>" years and "<ageMonth>" months')
def retire_age(ageYear, ageMonth):
    assert ageYear, ageMonth == birth_year


@when(parsers.cfparse('Enter "{invalid_inputs:Number}" for birth year', extra_types=EXTRA_TYPES))
@when('Enter "<invalid_inputs>" for birth year')
def invalid_inputs(invalid_inputs):
    return retirement(invalid_inputs)


@then("the program will raise an exception")
def raise_error():
    with pytest.raises(TypeError):
        invalid_inputs()
