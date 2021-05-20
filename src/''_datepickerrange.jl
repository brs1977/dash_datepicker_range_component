# AUTO GENERATED FILE - DO NOT EDIT

export ''_datepickerrange

"""
    ''_datepickerrange(;kwargs...)

A DatepickerRange component.

Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `endDate` (String; optional): A endDate that will be printed when this component is rendered.
- `startDate` (String; optional): A startDate that will be printed when this component is rendered.
"""
function ''_datepickerrange(; kwargs...)
        available_props = Symbol[:id, :endDate, :startDate]
        wild_props = Symbol[]
        return Component("''_datepickerrange", "DatepickerRange", "datepicker_range_component", available_props, wild_props; kwargs...)
end

