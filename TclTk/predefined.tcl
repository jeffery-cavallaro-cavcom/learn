#!/usr/bin/env tclsh
#
# Display a predefined variable/array value.

foreach name $argv {
    if [array exists $name] {
        foreach varname [lsort [array names $name]] {
            set value $name
            append value "($varname)"
            puts "$varname = [set $value]"
        }
    } else {
        puts "$name = [set $name]"
    }
}
