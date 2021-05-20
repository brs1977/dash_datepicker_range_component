// @flow

import { addDays,parseISO } from 'date-fns';
import 'rsuite/dist/styles/rsuite-default.css'
import React, {Component} from 'react';
import { DateRangePicker,IntlProvider } from 'rsuite'; 
import PropTypes from 'prop-types';
import ru from 'date-fns/locale/ru';
import ruRU from 'rsuite/lib/IntlProvider/locales/ru_RU';
import format from 'date-fns/format';


function formatDate(data, formatStr) {
    if (typeof(data) === 'string')
        data = parseISO(data)
    console.log(data)
    // fix YYYY to yyyy and DD to dd 
    return format(data, formatStr.replace("YYYY", "yyyy").replace("DD","dd"), { locale: ru });
}

export default class DatepickerRange extends Component {
    render() {
        const {
            allowedRange
        } = DateRangePicker;

        const {id, startDate, endDate, setProps} = this.props;

        return (
        <IntlProvider locale={ruRU} formatDate={formatDate}>
            <div id={id} className={className}>

                <DateRangePicker

                    format="DD.MM.YYYY"
/*                    locale={{
                        sunday: 'Вс',
                        monday: 'Пн',
                        tuesday: 'Вт',
                        wednesday: 'Ср',
                        thursday: 'Чт',
                        friday: 'Пт',
                        saturday: 'Сб',
                        ok: 'OK',
                        today: 'Сегодня',
                        yesterday: 'Вчера',
                        last7Days: 'Последние 7 дней',
                        formattedMonthPattern: 'MMM, YYYY',
                        formattedDayPattern: 'MMM DD, YYYY'				      
                    }}    */

                    ranges={[{
                        label: 'Сегодня',
                        value: [new Date(), new Date()]
                    }, {
                        label: 'Вчера',
                        value: [addDays(new Date(), -1), addDays(new Date(), -1)]
                    }, {
                        label: '7 дней',
                        value: [addDays(new Date(), -6), new Date()]
                    }, {
                        label: '30 дней',
                        value: [addDays(new Date(), -30), new Date()]
                    } ]}

                    // disabledDate={allowedRange('01.01.2010', Date().toLocaleDateString())}

                    // placeholder='дд.мм.гггг'
                    // value={[ new Date(startDate), new Date(endDate)]}
                    value={[ startDate, endDate]}
                    onChange={value => {
                    //   this.setState({ value });
                      setProps({ startDate: value[0].toISOString(), endDate: value[1].toISOString() })
                      console.log(value);
                    }}                    
                /> 
            </div>
            </IntlProvider>
        );
    }
}

DatepickerRange.defaultProps = {};

DatepickerRange.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A className that will be printed when this component is rendered.
     */
    className: PropTypes.string,

    /**
     * A startDate that will be printed when this component is rendered.
     */
    startDate: PropTypes.string,

    /**
     * A endDate that will be printed when this component is rendered.
     */
     endDate: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
