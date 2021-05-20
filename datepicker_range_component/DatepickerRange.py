# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DatepickerRange(Component):
    """A DatepickerRange component.


Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- endDate (string; optional):
    A endDate that will be printed when this component is rendered.

- startDate (string; optional):
    A startDate that will be printed when this component is rendered."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, startDate=Component.UNDEFINED, endDate=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'endDate', 'startDate']
        self._type = 'DatepickerRange'
        self._namespace = 'datepicker_range_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'endDate', 'startDate']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DatepickerRange, self).__init__(**args)
