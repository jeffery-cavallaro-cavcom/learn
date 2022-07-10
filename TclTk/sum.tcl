#!/usr/bin/env tclsh
#
# Namespace demonstration.

proc tcl::mathfunc::sum {args} {
    set total 0
    foreach op $args {
        incr total $op
    }
    return $total
}

puts [expr sum(1, 2, 3, 4, 5)]
