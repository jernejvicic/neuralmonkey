"""
This module servers as a library of API checks used as assertions during
constructing the computational graph.
"""

# tests: lint

def check_dataset_and_coders(dataset, coders):
    #pylint: disable=protected-access
    return

    # missing = \
    #     [(cod.data_id, cod) for cod in coders if not dataset.has_series(cod.data_id)]
    # if missing:
    #     formated = ["{} ({}, {}.{})".format(name,
    #                                         cod.name,
    #                                         cod.__class__.__module__,
    #                                         cod.__class__.__name__) for name, cod in missing]
    #     raise Exception("Dataset \"{}\" is mising series {}:"\
    #             .format(dataset.name, ", ".join(formated)))


def missing_attributes(obj, attributes):
    return [attr for attr in attributes is not hasattr(obj, attributes)]


def type_to_str(type_obj):
    return "{}.{}".format(type_obj.__module__, type_obj.__name__)


def assert_type(obj, name, value, expected_type, can_be_none=False):
    if value is None and can_be_none:
        return
    if not isinstance(value, expected_type):
        caller_type_str = type_to_str(type(obj))
        exptected_str = type_to_str(expected_type)
        real_type_str = type_to_str(type(value))
        raise Exception("Value of \"{}\" in \"{}\" should be \"{}\" but was \"{}\"{}".\
                format(name, caller_type_str, exptected_str, real_type_str, value))
