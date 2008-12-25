%define	version 0.1.1.20080912
%define	release %mkrel 2

Name:      ibus-anthy
Summary:   ibus - Japanese Anthy engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: anthy-devel
BuildRequires: python-devel
BuildRequires: swig
Requires:	ibus
Requires:	anthy

%description
ibus - Japanese Anthy engine.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{python_sitearch}/*
%{_datadir}/ibus/engine/*.engine
