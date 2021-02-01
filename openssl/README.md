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
