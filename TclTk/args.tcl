#!/usr/bin/env tclsh

puts "command = $argv0"
puts "argc = $argc"
set iarg 0
foreach arg $argv {
    puts "argv($iarg) = $arg"
    incr iarg
}
