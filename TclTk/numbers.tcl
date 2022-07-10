#!/usr/bin/env tclsh

set numbers(zero) 0
set numbers(one) 1
set numbers(two) 2
set numbers(three) 3
set numbers(four) 4
set numbers(five) 5
set numbers(six) 6
set numbers(seven) 7
set numbers(eight) 8
set numbers(nine) 9

foreach number [lsort [array names numbers]] {
    puts "numbers($number) = $numbers($number)"
}
