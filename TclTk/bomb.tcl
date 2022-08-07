#!/usr/bin/env tclsh

for {set i 10} {$i > 0} {incr i -1} {
    puts $i
    after 1000
}

puts "BOOM !!!"
