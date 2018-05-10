#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fwupdate
Version  : 11
Release  : 3
URL      : https://github.com/rhboot/fwupdate/releases/download/11/fwupdate-11.tar.bz2
Source0  : https://github.com/rhboot/fwupdate/releases/download/11/fwupdate-11.tar.bz2
Summary  : Tools to manage UEFI firmware updates
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: fwupdate-bin
Requires: fwupdate-config
Requires: fwupdate-lib
Requires: fwupdate-data
Requires: fwupdate-doc
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : pkgconfig(efiboot)
BuildRequires : pkgconfig(efivar)
BuildRequires : popt-dev

%description
fwupdate provides a simple command line interface to the UEFI firmware updates.

%package bin
Summary: bin components for the fwupdate package.
Group: Binaries
Requires: fwupdate-data
Requires: fwupdate-config

%description bin
bin components for the fwupdate package.


%package config
Summary: config components for the fwupdate package.
Group: Default

%description config
config components for the fwupdate package.


%package data
Summary: data components for the fwupdate package.
Group: Data

%description data
data components for the fwupdate package.


%package dev
Summary: dev components for the fwupdate package.
Group: Development
Requires: fwupdate-lib
Requires: fwupdate-bin
Requires: fwupdate-data
Provides: fwupdate-devel

%description dev
dev components for the fwupdate package.


%package doc
Summary: doc components for the fwupdate package.
Group: Documentation

%description doc
doc components for the fwupdate package.


%package lib
Summary: lib components for the fwupdate package.
Group: Libraries
Requires: fwupdate-data

%description lib
lib components for the fwupdate package.


%prep
%setup -q -n fwupdate-11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525542260
make  %{?_smp_mflags} EFIDIR=org.clearlinux GNUEFIDIR=/usr/lib64

%install
export SOURCE_DATE_EPOCH=1525542260
rm -rf %{buildroot}
%make_install EFIDIR=org.clearlinux GNUEFIDIR=/usr/lib64

%files
%defattr(-,root,root,-)
/boot/efi/EFI/org.clearlinux/fwupx64.efi

%files bin
%defattr(-,root,root,-)
/usr/bin/fwupdate
/usr/libexec/fwupdate/cleanup

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/fwupdate-cleanup.service

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/fwupdate
/usr/share/locale/en/fwupdate.po
/usr/share/locale/en/libfwup.po

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libfwup.so
/usr/lib64/pkgconfig/fwup.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfwup.so.1
/usr/lib64/libfwup.so.1.11
