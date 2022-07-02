#!/usr/bin/env wish

set enabled 0

proc toggle {} {
    set state [.done cget -state]
    if {$state == "disabled"} {
        .done configure -background green -state normal
        .enabler configure -text "disable"
    } else {
        .done configure -background red -state disabled
        .enabler configure -text "enable"
    }
}

button .enabler -text "enable" -command toggle
button .done -text "done" -background red -state disabled -command exit
grid .enabler .done -padx 0.25i -pady 0.25i

