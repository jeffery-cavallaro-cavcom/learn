#!/usr/bin/env wish
#
# Follow the mouse.
button .quit -text "Done" -command exit
bind . <Motion> {puts "X=%x Y=%y"}
grid .quit
