%define debug_package %{nil}
%define anviluser     admin
%define anvilgroup    admin
Name:           anvil-striker-extra
Version:        3.0
Release:        1%{?dist}
Summary:        Alteeve Anvil! Striker dashboard extras

License:        GPLv2+
URL:            https://github.com/digimer/anvil-striker-extra
Source0:        https://github.com/digimer/anvil-striker-extra/archive/master.tar.gz
BuildArch:      noarch


%description
This package provides files provided by upstream projects, like 'vmlinuz' and 
'initrd.img' from upstream netinstall media used for Striker's "Install Target"
feature.

The version of this package is not kept in step with the main anvil repository.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/tftpboot/
cp -Rp tftpboot/* $RPM_BUILD_ROOT/%{_sharedstatedir}/tftpboot/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md 
%{_sharedstatedir}/tftpboot/fedora28/*

%changelog
* Thu Nov 01 2018 Madison Kelly <mkelly@alteeve.ca> 3.0-1
- First release, includes tftpboot files from Fedora28.
