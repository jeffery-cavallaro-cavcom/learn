import static groovyx.gpars.GParsPool.withPool

def urls = [
    'http://www.groovy-lang.org',
    'http://gpars.codehaus.org',
    'http://gr8conf.org'
]*.toURL()

println withPool {
    urls.connectParallel {
        it.text.findAll(~/[Gg]roovy/).size()
    }
}
