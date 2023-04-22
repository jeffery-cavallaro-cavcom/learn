# RHEL

I am staying on RHEL8 for now since that is what I use at work.

## Groups

Upon installation, the initial user is given his/her own group with number
1000.  Remove this group and change the initial user to be in the 'users'
group.  be sure to change group ownership of all of the initial user's files.
A reboot seems to be required to be the OS to forget about the old group.

## Sudoers

Uncomment the wheel line that allows no-password.

## Firefox

Log into firefox account.  This should install add-ons and favorites registered
with the account.

## Lastpass

This is the preferred password vault.  It should be installed upon the first
firefox login.  If not, then install as a firefox add-on.

## Development

For gcc, install the development tools:

``` bash
subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
yum install "Development tools"
yum install gcc
yum install gcc-c++
yum install gdb
yum install make
```

## Emacs

The emacs provided on RHEL8 is too old and has communication problems with
elpa.

### Installation

1. Grab a current tarball.

1. Install the following packages:
``` bash
yum install libXaw-devel
yum install libjpeg-devel
yum install giflib-devel
yum install libtiff.devel
yum install gnutls.devel
```

1. Make it:
``` bash
./configure
make
make check
make install
```

1. Copy the file [`emacs.conf`](emacs.conf) to `~/.emacs`.

1. Copy [`clean`](clean) to `~/bin`.  This is a shell script to clean up emacs
turds.

1. Set emacs as the default editor by adding the following line to `~/.bashrc`:
``` bash
export EDITOR=/usr/local/bin/emacs
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

RHEL uses VLS:

``` bash
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
yum install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm
yum install vlc
```

## Thunderbird

### Installation

``` bash
yum install thunderbird
```

### Configuration

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

## Python

The Python version supplied with RHEL 8 is too old.  These are the instructions
to build from source.  It is best to just build and install in /usr/local.

1. Get the source tarball from python.org.

1. Install the following packages:
``` bash
yum install openssl-devel
yum install libffi-devel
yum install bzip2-devel
yum install ncurses-devel
yum install gdbm-devel
yum install lzma
yum install xz-devel
yum install tcl-devel
yum install tk-devel
yum install python3-tkinter
yum install uuid
yum install uuid-devel
yum install readline-devel
yum install sqlite-devel
```

1. Build it:
``` bash
./configure --enable-shared
make
make test
make install
```

1. Copy the [local ld config](local.conf) to `/etc/ld.so.conf.d` and update
   the config:
``` bash
ldconfig
```

## Vscode

1. Enable the RPM:

``` bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
```

1. Install it:

``` bash
yum install code
```
