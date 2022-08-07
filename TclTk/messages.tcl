#!/usr/bin/env tclsh

package require msgcat

::msgcat::mcload [file join [file dirname [info script]] msgs]

proc show_messages {} {
    puts [::msgcat::mc hello]
    puts [::msgcat::mc goodbye]
}

set locales {en_US es he}
foreach locale $locales {
    puts $locale
    ::msgcat::mclocale $locale
    show_messages
}
