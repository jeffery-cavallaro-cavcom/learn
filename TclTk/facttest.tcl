#!/usr/bin/env tclsh
#
# Computes factorials from 0 to 10.
source factorial.tcl

set i 0
while {$i <= 10} {
    puts "$i! = [factorial $i]"
    incr i
}
