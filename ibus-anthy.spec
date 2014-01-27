%define api 1.0
%define major 5
%define libname %mklibname anthygobject %{api} %{major}
%define devname %mklibname -d anthygobject
%define girname %mklibname anthy-gir 9000

Summary:	ibus - Japanese Anthy engine
Name:		ibus-anthy
Version:	1.5.4
Release:	1
License:	GPLv2+
Group:		System/Internationalization
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	ibus
BuildRequires:	intltool
BuildRequires:	pkgconfig(anthy)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	python-gi
Requires:	ibus
Requires:	anthy
Requires:	python-gi
Requires:	%{girname} = %{EVRD}
Suggests:	kasumi

%description
ibus - Japanese Anthy engine.

%files -f %{name}.lang
%{_libexecdir}/ibus-engine-anthy
%{_libexecdir}/ibus-setup-anthy
%{_datadir}/%{name}
%{_datadir}/applications/ibus-setup-anthy.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/ibus/component/anthy.xml

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for anthygobject
Group:		System/Libraries

%description -n %{libname}
Shared library for anthygobject.

%files -n %{libname}
%{_libdir}/libanthygobject-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{girname}
Summary:	GObject Introspection interface description for anthy
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}

%description -n %{girname}
GObject Introspection interface description for anthy.

%files -n %{girname}
%{_libdir}/girepository-1.0/Anthy-9000.typelib

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for ibus-anthy
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for ibus-anthy.

%files -n %{devname}
%{_libdir}/libanthygobject-%{api}.so
%{_includedir}/ibus-anthy-%{api}
%{_datadir}/gir-1.0/*.gir

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

