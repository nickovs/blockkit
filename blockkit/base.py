# BlockKit: A Pythonic library for constructing Slack Block Kit API structures.

# Copyright 2021 Nicko van Someren
#
# Licensed under the Apache License, Version 2.0 (the "License")
# See the LICENSE.txt file for details

# SPDX-License-Identifier: Apache-2.0

# pylint: disable=too-few-public-methods

"""Base types for blocks and the components they are made of"""

import json
import typing
import inspect

def _validate_value(value, annotation):
    # pylint: disable=too-many-return-statements, invalid-name
    if typing.get_origin(annotation) == list:
        if not isinstance(value, list):
            return (False, None)
        result = []
        item_type = annotation.__args__[0]
        for item in value:
            ok, item = _validate_value(item, item_type)
            if not ok:
                return (False, None)
            result.append(item)
        return (True, result)

    if typing.get_origin(annotation) == typing.Union:
        for item_type in annotation.__args__:
            ok, new_value = _validate_value(value, item_type)
            if ok:
                return (True, new_value)
        return (False, None)

    if getattr(annotation, "validate_value", None) is not None:
        return annotation.validate_value(value)

    if isinstance(value, annotation):
        return (True, value)

    return (False, None)


class Component:
    """The base component for JSON parts that make up blocks"""
    def __init_subclass__(cls, *args, **kwargs):
        params = [inspect.Parameter("self", inspect.Parameter.POSITIONAL_ONLY)]
        annos = getattr(cls, "__annotations__", {})
        dummy = object()
        for name, annotation in annos.items():
            default=getattr(cls, name, inspect.Parameter.empty)
            params.append(inspect.Parameter(name, inspect.Parameter.POSITIONAL_OR_KEYWORD,
                                            default=default,
                                            annotation=annotation))
        def __init__(self, *init_args, **init_kwargs):
            # pylink objects to the use of 'ok' as a variable name...
            # pylint: disable=invalid-name
            bound = self.__init__.__signature__.bind(self, *init_args, **init_kwargs)
            super().__init__()
            for name, value in bound.arguments.items():
                if name != "self":
                    ok, value = _validate_value(value, annos[name])
                    if not ok:
                        raise ValueError("Paramter {} must be of type {}".format(name, annos[name]))
                    self.__dict__[name] = value
        __init__.__qualname__ = f"{cls.__qualname__}.__init__"
        __init__.__signature__ = inspect.Signature(params)
        setattr(cls, "__init__", __init__)
        super().__init_subclass__(*args, **kwargs)

    def __init__(self, bound):
        print(f"Superclass init with args: {bound}")

    def __repr__(self):
        annos = getattr(self.__class__, "__annotations__", {})
        parts = []
        value_dict = self.__dict__
        for name in annos:
            if name in value_dict and value_dict[name] is not None:
                parts.append("{0}={1!r}".format(name, value_dict[name]))
        return "{}({})".format(self.__class__.__name__, ", ".join(parts))

    def asdict(self):
        """Convert structure to a dictionary representation"""
        result = {}
        annos = getattr(self.__class__, "__annotations__", {})
        value_dict = self.__dict__
        _type = getattr(self, "_type", None)
        if _type is not None:
            result["type"] = _type
        for name in annos:
            if name != "_type" and name in value_dict and value_dict[name] is not None:
                value = value_dict[name]
                if isinstance(value, Component):
                    value = value.asdict()
                elif isinstance(value, list):
                    value = [i.asdict() if isinstance(i, Component) else i for i in value]
                result[name] = value
        return result

    def json(self):
        """Convert structure to a JSON representation"""
        return json.dumps(self.asdict())


class Element(Component):
    """Base class for typed elements"""
    def __init_subclass__(cls, *args, **kwargs):
        # All elements need a type name
        if "_type" not in cls.__dict__:
            cls._type = cls.__name__.lower()
        super().__init_subclass__(*args, **kwargs)


class Block(Element):
    """Base class for typed blocks"""
    def __init_subclass__(cls, *args, **kwargs):
        # All blocks need an optional block_id
        if not hasattr(cls, "__annotations__"):
            cls.__annotations__ = dict()
        cls.__annotations__['block_id'] = str
        cls.block_id = None
        super().__init_subclass__(*args, **kwargs)
