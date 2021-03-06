# -*- coding: utf-8 -*-

"""
 This file defines the entities needed by our legislation.
 """
from openfisca_core.entities import build_entity

Organisation = build_entity(
    key = "organisation",
    plural = "organisations",
    label = u'Organisation',
    doc = '''
    ''',
    roles = [
        {
            'key': 'representative',
            'plural': 'representatives',
            'label': u'Representative',
            'doc': u'The representatives authorised on behalf of an organisation'
            },
        {
            'key': 'other',
            'plural': 'others',
            'label': u'Other',
            'doc': u'Other members of an organisation who are not representatives'
            }
        ]
    )

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'An individual. The minimal legal entity on which a legislation might be applied.',
    doc = '''
    Variables like 'salary' and 'income_tax' are usually defined for the entity 'Person'.
    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with
    person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent'
    in a 'Family' entity with person.has_role(Family.PARENT)).
    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True
    )

entities = [Building, Organisation, Family, Person]
