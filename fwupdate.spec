#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fwupdate
Version  : 12
Release  : 9
URL      : https://github.com/rhboot/fwupdate/releases/download/12/fwupdate-12.tar.bz2
Source0  : https://github.com/rhboot/fwupdate/releases/download/12/fwupdate-12.tar.bz2
Summary  : Tools to manage UEFI firmware updates
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: fwupdate-bin = %{version}-%{release}
Requires: fwupdate-data = %{version}-%{release}
Requires: fwupdate-lib = %{version}-%{release}
Requires: fwupdate-libexec = %{version}-%{release}
Requires: fwupdate-license = %{version}-%{release}
Requires: fwupdate-man = %{version}-%{release}
Requires: fwupdate-services = %{version}-%{release}
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
BuildRequires : pkgconfig(efiboot)
BuildRequires : pkgconfig(efivar)
BuildRequires : popt-dev

%description
fwupdate provides a simple command line interface to the UEFI firmware updates.

%package bin
Summary: bin components for the fwupdate package.
Group: Binaries
Requires: fwupdate-data = %{version}-%{release}
Requires: fwupdate-libexec = %{version}-%{release}
Requires: fwupdate-license = %{version}-%{release}
Requires: fwupdate-services = %{version}-%{release}

%description bin
bin components for the fwupdate package.


%package data
Summary: data components for the fwupdate package.
Group: Data

%description data
data components for the fwupdate package.


%package dev
Summary: dev components for the fwupdate package.
Group: Development
Requires: fwupdate-lib = %{version}-%{release}
Requires: fwupdate-bin = %{version}-%{release}
Requires: fwupdate-data = %{version}-%{release}
Provides: fwupdate-devel = %{version}-%{release}
Requires: fwupdate = %{version}-%{release}

%description dev
dev components for the fwupdate package.


%package lib
Summary: lib components for the fwupdate package.
Group: Libraries
Requires: fwupdate-data = %{version}-%{release}
Requires: fwupdate-libexec = %{version}-%{release}
Requires: fwupdate-license = %{version}-%{release}

%description lib
lib components for the fwupdate package.


%package libexec
Summary: libexec components for the fwupdate package.
Group: Default
Requires: fwupdate-license = %{version}-%{release}

%description libexec
libexec components for the fwupdate package.


%package license
Summary: license components for the fwupdate package.
Group: Default

%description license
license components for the fwupdate package.


%package man
Summary: man components for the fwupdate package.
Group: Default

%description man
man components for the fwupdate package.


%package services
Summary: services components for the fwupdate package.
Group: Systemd services

%description services
services components for the fwupdate package.


%prep
%setup -q -n fwupdate-12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568738087
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags} EFIDIR=org.clearlinux GNUEFIDIR=/usr/lib64


%install
export SOURCE_DATE_EPOCH=1568738087
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fwupdate
cp COPYING %{buildroot}/usr/share/package-licenses/fwupdate/COPYING
%make_install EFIDIR=org.clearlinux GNUEFIDIR=/usr/lib64
## install_append content
install -m 0755 -d %{buildroot}/usr/lib/fwupd
mv %{buildroot}/boot/efi/EFI/org.clearlinux/fwupx64.efi %{buildroot}/usr/lib/fwupd/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/fwupd/fwupx64.efi

%files bin
%defattr(-,root,root,-)
/usr/bin/fwupdate

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/fwupdate
/usr/share/locale/en/fwupdate.po
/usr/share/locale/en/libfwup.po

%files dev
%defattr(-,root,root,-)
/usr/include/fwup-version.h
/usr/include/fwup.h
/usr/lib64/libfwup.so
/usr/lib64/pkgconfig/fwup.pc
/usr/share/man/man3/fwup_clear_status.3
/usr/share/man/man3/fwup_get_fw_type.3
/usr/share/man/man3/fwup_get_fw_version.3
/usr/share/man/man3/fwup_get_guid.3
/usr/share/man/man3/fwup_get_last_attempt_info.3
/usr/share/man/man3/fwup_get_lowest_supported_version.3
/usr/share/man/man3/fwup_get_ux_capsule_info.3
/usr/share/man/man3/fwup_resource_free.3
/usr/share/man/man3/fwup_resource_iter_create.3
/usr/share/man/man3/fwup_resource_iter_destroy.3
/usr/share/man/man3/fwup_resource_iter_next.3
/usr/share/man/man3/fwup_set_guid.3
/usr/share/man/man3/fwup_set_guid_forced.3
/usr/share/man/man3/fwup_set_up_update.3
/usr/share/man/man3/fwup_supported.3
/usr/share/man/man3/libfwup.3
/usr/share/man/man3/libfwup.h.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfwup.so.1
/usr/lib64/libfwup.so.1.12

%files libexec
%defattr(-,root,root,-)
/usr/libexec/fwupdate/cleanup

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fwupdate/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fwupdate.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fwupdate-cleanup.service
