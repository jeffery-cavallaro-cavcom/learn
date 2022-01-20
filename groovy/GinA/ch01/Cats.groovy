def cats = new XmlSlurper().parse(new File("cats.xml"))
for (cat in cats.cat) {
    println "${cat.@name} is ${cat.@color}"
}
