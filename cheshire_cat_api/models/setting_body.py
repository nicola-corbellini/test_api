# coding: utf-8

"""
    😸 Cheshire-Cat API

    Open source and customizable AI architecture

    The version of the OpenAPI document: 1.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from cheshire_cat_api.models.value import Value

class SettingBody(BaseModel):
    """
    SettingBody
    """
    name: StrictStr = Field(...)
    value: Value = Field(...)
    category: Optional[StrictStr] = None
    __properties = ["name", "value", "category"]

    class Config:
        """Pydantic configuration"""
        populate_by_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SettingBody:
        """Create an instance of SettingBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SettingBody:
        """Create an instance of SettingBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SettingBody.parse_obj(obj)

        _obj = SettingBody.parse_obj({
            "name": obj.get("name"),
            "value": Value.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "category": obj.get("category")
        })
        return _obj


