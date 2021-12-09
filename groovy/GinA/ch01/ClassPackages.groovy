def classes = [String, List, File]
for (clazz in classes) {
    println "${clazz.simpleName} is in package ${clazz.package.name}"
}
