# Ubuntu and Tools

## Partitions

disk|partition|size
---|---|---
1|/boot/efi|500 Mb
1|/|500 Gb
1|swap|10 Gb
1|/tmp|10 Gb
1|/var|100 Gb
2|/home|rest

## Accounts

On first login, connect to Ubuntu, Google, and Microsoft accounts.

## Groups

Change the user-specific group to `users`.

## Sudoers

Change the following line in `/etc/sudoers`:

```
%sudo	ALL=(ALL:ALL) NOPASSWD:ALL
```

## Firefox

Log into firefox account.  This should install add-ons and favorites registered
with the account.

## Lastpass

This is the preferred password vault.  It should be installed upon the first
firefox login.  If not, then install as a firefox add-on.

## Emacs

### Installation

The snap version (27) is built with an older fontconfig, resulting in warnings
and errors on startup.  Use the apt-get version (26).

``` bash
apt-get update
apt-get install emacs
```

### Configuration

Copy the file [`emacs.conf`](emacs.conf) to `~/.emacs`.

### Clean

This is a shell script to clean up emacs turds.  Copy [`clean`](clean) to
`~/bin`.

### Default

Set emacs as the default editor by adding the following line to `~/.profile`:

``` bash
export EDITOR=/usr/bin/emacs
```

## Markdown

### Viewer

Almost all of the markdown viewers for linux are out-of-date and produce
warnings and errors if they work at all.  The best solution is to use the
GitHub markdown viewer add-on for firefox.  This add-on should have been
installed upon the first login to firefox.  Otherwise, install the add-on
manually.

### Configuration

To get the markdown viewer to work, copy the file
[`text-markdown.xml`](text-markdown.xml) to
`~/.local/share/mime/packages/text-markdown.xml`.

Then update the MIME database:

``` bash
update-mime-database ~/.local/share/mime
```

### emacs

Install (package-install) the `markdown-mode` package for emacs.  This will
add two modes: `markdown-mode` for standard markdown and `gfm-mode` for
git-flavored markdown.

Add the following line to `~\.emacs` so that GFM mode is the default for
`README.md` files:

``` emacs-lisp
(add-to-list 'auto-mode-alist '("\\.md\\'" . gfm-mode))
```

## Git

### Installation

Install Git and all of its associated GUIs and tools:

``` bash
apt-get install git
apt-get install gitk
apt-get install git-gui
```

### Global Configuration

The following commands will write global settings to `~/.gitconfig`:

``` bash
git config --global user.name "Jeffery Cavallaro"
git config --global user.email "jeffery@cavcom.com"
git config --global core.editor "/usr/bin/emacs"
```

## Brasero

This is the standard tool for cd/dvd rom write and copy operations:

``` bash
apt-get install brasero
```

## Codecs

Most of the needed codecs for A/V are in proprietary packages and must be
installed separately:

``` bash
apt-get install ubuntu-restricted-extras
```

Accept all license agreements during the installation.

## Development

Install the compilers and debuggers:

``` bash
apt-get install build-essential
```

## ssh

If not installed, install and enable ssh support:

``` bash
# apt-get install ssh
# systemctl enable ssh
```

## DNS

The presence of connection manager makes things a little different.  First,
make sure that the basic network settings are correct using the connection
manager icon in the upper right corner.  Then, for additional settings like
the search domain, access the connection manager editor:

``` bash
# nm-connection-editor
```

## Chrome

The following procedure will add the distribution site to the apt sources list:

``` bash
$ cd ~/Downloads
$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo apt install ./google-chrome-stable_current_amd64.deb
$ rm google-chrome-stable_current_amd64.deb
```

## Opera

``` bash
# snap install opera
```

## JetBrains

``` bash
# snap install pycharm-professional --classic
# snap install webstorm --classic
```

## Virtualbox

The use of VirtualBox is under review due to its need to invasively patch the
kernel and because it is an Oracle product.  A shift to vanilla KVM is being
contemplated.

``` bash
# wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
# sudo add-apt-repository "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib"
# apt-get update
# apt-get install build-essential
# apt-get install virtualbox
```

If EFI secure boot is enabled then the system will walk through the steps to
install a new MOK.

## Thunderbird

|NAME|VALUE|
|----|-----|
|Username|jeffery@cavcom.com|
|IMAP Server|mail.cavcom.com|
|IMAP Port|993|
|IMAP Connection Security|SSL/TLS|
|IMAP Authentication Method|Normal Password|
|SMTP Server|smtp.cavcom.com|
|SMTP Port|587|
|SMTP Connection Security|STARTTLS|
|SMTP Authentication Method|Encrypted Password|
