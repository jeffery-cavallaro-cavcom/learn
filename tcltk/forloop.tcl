#!/usr/bin/env tclsh
#
# Defines a for loop.
proc forloop {init guard next script} {
    eval $init
    while {[expr $guard]} {
        eval $script
        eval $next
    }
}

forloop {set i 0} {$i < 10} {incr i} {
    puts $i
}
