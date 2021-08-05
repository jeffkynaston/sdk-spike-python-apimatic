# -*- coding: utf-8 -*-

"""
plastiqpublicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from plastiqpublicapi.api_helper import APIHelper
from plastiqpublicapi.models.contact_1 import Contact1
from plastiqpublicapi.models.recipient_address import RecipientAddress


class Recipient(object):

    """Implementation of the 'Recipient' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        business_name (string): TODO: type description here.
        category_id (uuid|string): TODO: type description here.
        business_address (RecipientAddress): TODO: type description here.
        contact (Contact1): TODO: type description here.
        receiving_method (object): TODO: type description here.
        created_at (datetime): TODO: type description here.
        status (StatusEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "business_name": 'businessName',
        "category_id": 'categoryId',
        "business_address": 'businessAddress',
        "contact": 'contact',
        "receiving_method": 'receivingMethod',
        "created_at": 'createdAt',
        "status": 'status'
    }

    def __init__(self,
                 id=None,
                 business_name=None,
                 category_id=None,
                 business_address=None,
                 contact=None,
                 receiving_method=None,
                 created_at=None,
                 status=None):
        """Constructor for the Recipient class"""

        # Initialize members of the class
        self.id = id
        self.business_name = business_name
        self.category_id = category_id
        self.business_address = business_address
        self.contact = contact
        self.receiving_method = receiving_method
        self.created_at = APIHelper.RFC3339DateTime(created_at) if created_at else None
        self.status = status

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        id = dictionary.get('id')
        business_name = dictionary.get('businessName')
        category_id = dictionary.get('categoryId')
        business_address = RecipientAddress.from_dictionary(dictionary.get('businessAddress')) if dictionary.get('businessAddress') else None
        contact = Contact1.from_dictionary(dictionary.get('contact')) if dictionary.get('contact') else None
        receiving_method = dictionary.get('receivingMethod')
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdAt")).datetime if dictionary.get("createdAt") else None
        status = dictionary.get('status')

        # Return an object of this model
        return cls(id,
                   business_name,
                   category_id,
                   business_address,
                   contact,
                   receiving_method,
                   created_at,
                   status)
