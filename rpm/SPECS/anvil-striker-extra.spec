%define debug_package %{nil}
%define anviluser     admin
%define anvilgroup    admin
Name:           anvil-striker-extra
Version:        3.0
Release:        6%{?dist}
Summary:        Alteeve Anvil! Striker dashboard extras

License:        GPLv2+
URL:            https://github.com/digimer/anvil-striker-extra
Source0:        https://www.alteeve.com/an-repo/f28/SOURCES/anvil-striker-extra-3.0.tar.gz
BuildArch:      noarch


%description
This package provides files provided by upstream projects, like 'vmlinuz', 
'initrd.img' and 'install.img' from upstream netinstall media used for 
Striker's "Install Target" feature. 

The version of this package is not kept in step with the main anvil repository.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/tftpboot/
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/www/html/
cp -Rp tftpboot/rhel8 $RPM_BUILD_ROOT/%{_sharedstatedir}/tftpboot/
cp -Rp tftpboot/bios/* $RPM_BUILD_ROOT/%{_sharedstatedir}/tftpboot/
cp -Rp html/* $RPM_BUILD_ROOT/%{_localstatedir}/www/html/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md 
%{_sharedstatedir}/tftpboot/rhel8/*
%{_sharedstatedir}/tftpboot/pxelinux.0
%{_localstatedir}/www/html/rhel8/*

%changelog
* Thu Jul 16 2020 Madison Kelly <mkelly@alteeve.ca> 3.0-6
- Updated to RHEL 8.2 official release.

* Tue Jan 07 2020 Madison Kelly <mkelly@alteeve.ca> 3.0-5
- Updated to RHEL 8.1 official release.
- Added modules.yaml

* Tue Jul 02 2019 Madison Kelly <mkelly@alteeve.ca> 3.0-4
- Updated to RHEL 8.0 official release.

* Fri Jan 25 2019 Madison Kelly <mkelly@alteeve.ca> 3.0-3
- Started migration to RHEL8.

* Mon Nov 05 2018 Madison Kelly <mkelly@alteeve.ca> 3.0-2
- Added the install.img file.
- Added a custome comps.xml for fedora28.

* Thu Nov 01 2018 Madison Kelly <mkelly@alteeve.ca> 3.0-1
- First release, includes tftpboot files from Fedora28.
