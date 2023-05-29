# Hashicorp Consul

## Installation

### Consul
``` bash
yum install yum-utils
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
yum install consul
```

### Envoy
``` bash
rpm --import 'https://rpm.dl.getenvoy.io/public/gpg.CF716AF503183491.key'
curl -sL 'https://rpm.dl.getenvoy.io/public/config.rpm.txt?distro=el&codename=7' > /tmp/tetrate-getenvoy-rpm-stable.repo
yum-config-manager --add-repo '/tmp/tetrate-getenvoy-rpm-stable.repo'
yum makecache --disablerepo='*' --enablerepo='tetrate-getenvoy-rpm-stable'
yum install getenvoy-envoy
```

## Server Configuration

Set the data directory [here](consul.hcl).  Then add the server-specific
configuration [here](server.hcl).

## Start

Consul can be started by systemd or manually:
``` bash
/usr/bin/consul agent -config-dir=/etc/consul.d/
```

## UI

Go [here](http://localhost:8500).

## CLI

### Catalog

To see the running services or nodes:
``` bash
/usr/bin/consul catalog {services|nodes}
```

### Register

To register a service:
``` bash
/usr/bin/consul services register -name <name> -id=<id> -address <address> -port <port>
```

### Deregister

To deregister a service, it must be deregisterd on the same node that it was
registered:
``` bash
/usr/bin/consul services deregister id=<id>
```
