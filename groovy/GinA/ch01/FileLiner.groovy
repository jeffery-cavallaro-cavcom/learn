def lineNumber = 0
new File(args[0]).eachLine { line ->
    ++lineNumber
    println "$lineNumber: $line"
}
