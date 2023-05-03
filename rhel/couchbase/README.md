# Couchbase

## Python API

At this point in time, pypi only provides wheels for up to python 3.10.  For
python 3.11, the API is built from source.  In order to do this correctly on
RHEL 8 and later, the CXX_CLIENT_STATIC_STDLIB environment variable must be
set to 0.  Otherwise, the build will attempt to link to the the static
libstdc++, which RHEL no longer supports (nor supplies).

To properly build and install:

``` bash
export COUCHBASE_CXX_CLIENT_STATIC_STDLIB=OFF
pip3 install couchbase
```

## Server

To install the server, download the latest RPM from the couchbase website.
To install:

``` bash
yum install <rpm-file>
```

When done, got to `http://localhost:8091` to configure the new cluster.
