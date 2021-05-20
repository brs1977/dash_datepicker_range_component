# AUTO GENERATED FILE - DO NOT EDIT

''DatepickerRange <- function(id=NULL, endDate=NULL, startDate=NULL) {
    
    props <- list(id=id, endDate=endDate, startDate=startDate)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DatepickerRange',
        namespace = 'datepicker_range_component',
        propNames = c('id', 'endDate', 'startDate'),
        package = 'datepickerRangeComponent'
        )

    structure(component, class = c('dash_component', 'list'))
}
