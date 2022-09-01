#!/usr/bin/env tclsh

proc alter {a c} {
    upvar $c b
    lset a 1 changed
    lset b 0 changed
}

set a {1 2 3}
set r {4 5 6}
set x r

alter $a $x

puts $a
puts $r
