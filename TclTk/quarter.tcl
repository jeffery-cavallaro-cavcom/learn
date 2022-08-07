#!/usr/bin/env tclsh

set value [expr round(rand()*100)]

if {$value <= 25} {
    set quarter "first"
} elseif {$value <= 50} {
    set quarter "second"
} elseif {$value <= 75} {
    set quarter "third"
} else {
    set quarter "fourth"
}

puts "$value is in the $quarter quarter"
