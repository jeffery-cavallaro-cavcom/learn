# OpenSSL

## Creating a Certificate Authority (CA)

This procedure is for creating a self-signed root certificate.  CRL issues are
ignored.  Due to the protected nature of the resulting artifacts, this
procedure should be performed as root with a strict umask (e.g., 077).

1. Create a directory structure for the new CA:
    ``` bash
    # mkdir /opt/ca
    # mkdir /opt/ca/private
    # mkdir /opt/ca/index
    # mkdir /opt/ca/serial
    # mkdir /opt/ca/certs
    # touch /opt/ca/index/index.txt
    # echo '01' > /opt/ca/serial/serial
    ```
1. Copy the configuration file `ca.cnf` to the root directory:

    ``` bash
    # cp ca.cnf /opt/ca/
    # chmod 400 ca.cnf
    ```
1. Generate a new unencrypted private key and the root certificate:
    ``` bash
    # cd /opt/ca
    # openssl req -x509 -config ca.cnf -newkey rsa -days 3650 -nodes -out cacert.pem
    ```
    If an encrypted key is desired then omit the `-nodes` argument, which will
    result in a prompt for a passphrase.
1. Lock down the public cert and private key:
    ``` bash
    # chmod 444 cacert.pem
    # chmod 400 private/privkey.pem
    ```
1. To view the details of the new cert:
    ``` bash
    # openssl x509 -text -noout -in cacert.pem
    ```

## Requesting and Issuing a New Server Certificate

1. Create a separate request directory for the new server cert:
   ```bash
   # cd /opt/ca
   # mkdir -p reqs/cavcom
   # cd reqs/cavcom
   ```
1. Copy the server request configuration to this directory and update as
necessary to specify the actual domain.
    ```bash
    # cp cavcom.cnf /opt/ca/reqs/cavcom/
    ```
1. Generate the server request:
    ```bash
    # openssl req -config cavcom.cnf -new -newkey rsa -days 3650 -nodes -out cavcomreq.pem
    ```
1. Use the new request to generate the new server cert:
    ```bash
    # cd /opt/ca
    # openssl ca -config ca.cnf -notext -in reqs/cavcom/cavcomreq.pem -out reqs/cavcom/cavcomcert.pem
    ```
1. Lock down the new server cert information.

    ``` bash
    # chmod 500 reqs/cavcom
    # chmod 400 reqs/cavcom/*
    ```

## Adding the Root Key to the Java Trust Store

Java applications that use the Java PKI facility will need to have the root
CA public key added to the default trust store.  The trust store is a JKS
trust store file located in `$JAVA_HOME/lib/security/cacerts`.  Note that
this is probably a link to something like the following:

``` bash
# keytool -import -trustcacerts -alias cavcom -file /opt/ca/cacert.pem -keystore /etc/ssl/certs/java/cacerts
```

## Convert Private Key to RSA Format

Some applications require that the PKCS#8 formatted private key be in
PKCS#1 format - this means that the PEM file must start and end with:
`BEGIN RSA PRIVATE KEY` instead of `BEGIN PRIVATE KEY`.  This can be
accomplished with the following command:

``` bash
openssl rsa -in key.pem -out key-rsa.pem
```
