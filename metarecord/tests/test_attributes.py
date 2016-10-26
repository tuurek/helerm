import pytest
from django.core.exceptions import ValidationError

from metarecord.models.attribute import reload_attribute_schema


@pytest.mark.django_db
def test_choice_attribute_validation(function, choice_attribute, choice_value_1):
    reload_attribute_schema()

    # valid choice value
    function.attributes = {choice_attribute.identifier: choice_value_1.value}
    function.full_clean()

    # invalid choice value
    function.attributes = {choice_attribute.identifier: 'some random value'}
    with pytest.raises(ValidationError):
        function.full_clean()


@pytest.mark.django_db
def test_free_text_attribute_validation(function, free_text_attribute):
    reload_attribute_schema()

    # free text attributes should allow any string
    function.attributes = {free_text_attribute.identifier: 'some random value'}
    reload_attribute_schema()
    function.full_clean()

    # just to verify that our reload schema function works, this should be too long value
    function.attributes = {free_text_attribute.identifier: 'x' * 1025}
    reload_attribute_schema()

    with pytest.raises(ValidationError):
        function.full_clean()
