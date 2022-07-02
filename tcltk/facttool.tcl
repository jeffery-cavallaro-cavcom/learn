#!/usr/bin/env wish

source factorial.tcl

entry .value -width 6 -relief sunken -textvariable value
label .description -text "! = "
label .result -textvariable result
button .calculate -text "Calculate" \
    -command {set result [factorial $value]}
button .quit -text "Quit" -command exit
bind .value <Return> {
    .calculate flash
    .calculate invoke
}
set value 0
set result [factorial $value]
grid .value .description .result -padx 1m -pady 1m
grid .calculate .quit - -padx 1m -pady 1m
