#!/usr/bin/env tclsh

set x 1

proc xplus {{n 1} args} {
    global x
    set x [expr $x + $n]
    puts "x = $x"
    foreach s $args {
        puts $s
    }
}

xplus 0
xplus 2 added two
xplus 5 added five to result
xplus

