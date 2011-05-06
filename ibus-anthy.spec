%define	version 1.2.5
%define	release %mkrel 3

Name:      ibus-anthy
Summary:   ibus - Japanese Anthy engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: ibus-devel >= 1.3.5-9
BuildRequires: anthy-devel
BuildRequires: python-devel
BuildRequires: intltool
BuildRequires: swig
Requires:	ibus >= 1.2.0
Requires:	anthy
Requires(post,preun): GConf2

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

%post
%post_ibus_register_engine anthy ja

%preun
%preun_ibus_unregister_engine anthy

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/ibus-engine-anthy
%{_libexecdir}/ibus-setup-anthy
%{_datadir}/%{name}
%{_datadir}/ibus/component/anthy.xml
%{python_sitearch}/*
