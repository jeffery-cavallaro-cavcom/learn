#!/usr/bin/env tclsh

set seasons [list \
             "January" \
             "February" \
             "March" \
             "April" \
             "May" \
             "June" \
             "July" \
             "August" \
             "September" \
             "October" \
             "November" \
             "December" \
             "Dummy" ]

foreach month $seasons {
    switch -- $month {
        "December" -
        "January" -
        "February" {
            set season "Winter"
        }

        "March" -
        "April" -
        "May" {
            set season "Spring"
        }

        "June" -
        "July" -
        "August" {
            set season "Summer"
        }

        "September" -
        "October" -
        "November" {
            set season "Fall"
        }

        default {
            set season "Unknown"
        }
    }
    puts "The month of $month is during the $season"
}
