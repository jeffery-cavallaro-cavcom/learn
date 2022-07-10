#!/usr/bin/env tclsh
#
# Tests the random distribution.

set samples 10000

proc next_sample {} {
    return [expr round(rand()*100)]
}

set total 0

for {set i 0} {$i < $samples} {incr i} {
    set x [next_sample]
    incr total $x
}

set avg [expr $total/$samples]
puts $avg
