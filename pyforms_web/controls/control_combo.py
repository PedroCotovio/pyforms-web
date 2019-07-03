import collections
import simplejson

from django.db.models import fields
from pyforms_web.controls.control_base import ControlBase


class ValueNotSet:
    pass


class ControlCombo(ControlBase):
    def __init__(self, *args, **kwargs):
        self._init_form_called = False

        self._types = []
        self._items = collections.OrderedDict()
<<<<<<< HEAD
        self._last_items = None
        items = kwargs.get('items', [])
=======
        items = kwargs.get("items", [])
>>>>>>> v4
        for item in items:
            self.add_item(*item)

        if not items and "default" in kwargs:
            del kwargs["default"]

        super(ControlCombo, self).__init__(*args, **kwargs)

    def init_form(self):
        self._init_form_called = True
        return "new ControlCombo('{0}', {1})".format(
            self._name, simplejson.dumps(self.serialize())
        )

    def add_item(self, label, value=ValueNotSet):
        if self._items == None:
<<<<<<< HEAD
            self._items=collections.OrderedDict()
        
        # The value for the item was not set, so it will use the label as a value 
=======
            self._items = collections.OrderedDict()

        # The value for the item was not set, so it will use the label as a value
>>>>>>> v4
        if isinstance(value, ValueNotSet):
            value = label
        else:
            value = value

        self._types.append(type(value))
        self._items[label] = value

        if hasattr(self, "_parent"):
            self.mark_to_update_client()

    def __add__(self, val):
        if isinstance(val, tuple):
            self.add_item(val[0], val[1])
        else:
            self.add_item(val)

<<<<<<< HEAD
=======
        return self

>>>>>>> v4
    def clear_items(self):
        self._items = collections.OrderedDict()
        self._types = []
        self._value = None

        self.mark_to_update_client()

    def delete(self, value):
        # allow removal of one or multiple items
        # save latest removed items in _last_items
        if isinstance(value, str):
            self._last_items = self._items.pop(value)
            self.mark_to_update_client()
        elif isinstance(value, list):
            for v in value:
                self._last_items = []
                if isinstance(v, str): 
                    self._last_items.append(self._items.pop(value))
            self.mark_to_update_client()                

    @property
    def items(self):
        return self._items.values()

    @property
    def values(self):
        return self._items.items()

    @property
<<<<<<< HEAD
    def value(self): 
=======
    def value(self):
>>>>>>> v4
        if self._value == fields.NOT_PROVIDED:
            return None
        return self._value

    @value.setter
    def value(self, value):
        for i, (key, val) in enumerate(self._items.items()):
            value = None if value is None or value=='' else self._types[i](value)
            if value == val:
                if self._value != value:
                    self._value = value
                    self.mark_to_update_client()
                    if self._init_form_called:
<<<<<<< HEAD
                        self.changed_event()
    
=======

                        self.changed_event()
                    break

>>>>>>> v4
    @property
    def text(self):
        return ""

    @text.setter
    def text(self, value):
        for key, val in self._items.items():
            self.mark_to_update_client()
            if value == key:
                self.value = val
                break

    def __convert(self, value):
        if value == fields.NOT_PROVIDED:
            return None

        if isinstance(value, ValueNotSet):
            return None
        """
        if isinstance(value, bool):
<<<<<<< HEAD
            if value == True:
                value = 'true'
            if value == False:
                value = 'false'
            if value == None:
                value = 'null'
=======
            if value==True:  value = 'true'
            if value==False: value = 'false'
            if value==None:  value = 'null'

>>>>>>> v4
        elif isinstance(value, ValueNotSet):
            value = 'null'
        elif value == fields.NOT_PROVIDED:
            value = 'null'
        else:
            value = str(value)
        """
        return value

    def serialize(self):
        data = ControlBase.serialize(self)
        items = []
        for key, value in self._items.items():
<<<<<<< HEAD
            items.append({'text': key, 'value': self.__convert(value), 'name': key }) 
=======
            items.append({"text": key, "value": self.__convert(value), "name": key})

>>>>>>> v4
        value = self._value

        data.update({"items": items, "value": self.__convert(value)})
        return data
