%define	version 1.2.6
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.2.6-1mdv2011.0
+ Revision: 675871
- new version 1.2.6

* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.2.5-3
+ Revision: 669826
- rebuild

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 1.2.5-2
+ Revision: 659281
- rebuild for new ibus

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 1.2.5-1mdv2011.0
+ Revision: 604304
- update to new version 1.2.5

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 1.2.4-1mdv2011.0
+ Revision: 598543
- update to new version 1.2.4

* Wed Nov 03 2010 Funda Wang <fwang@mandriva.org> 1.2.3-2mdv2011.0
+ Revision: 592713
- rebuild for py2.7

* Mon Oct 25 2010 Funda Wang <fwang@mandriva.org> 1.2.3-1mdv2011.0
+ Revision: 589210
- update to new version 1.2.3

* Sun Apr 25 2010 Funda Wang <fwang@mandriva.org> 1.2.1-1mdv2010.1
+ Revision: 538613
- update to new version 1.2.1

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20100115-1mdv2010.1
+ Revision: 492371
- update to new version 1.2.0.20100115

* Sat Nov 28 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20091127-1mdv2010.1
+ Revision: 470765
- BR intltool
- New version 1.2.0.20091127

* Mon Sep 21 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090917-1mdv2010.0
+ Revision: 446417
- New version 1.2.0.20090917

* Tue Sep 15 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090907-1mdv2010.0
+ Revision: 441926
- New version 1.2.0.20090907

* Tue Aug 04 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090804-1mdv2010.0
+ Revision: 408861
- new version 1.2.0.20090804
- new version 1.2.0

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090603-1mdv2010.0
+ Revision: 382431
- update file list
- New version 1.1.0.20090603

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090402-1mdv2010.0
+ Revision: 369490
- New version 1.1.0.20090402

* Fri Feb 13 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090211-1mdv2009.1
+ Revision: 339994
- update to new version 1.1.0.20090211

* Thu Feb 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090205-1mdv2009.1
+ Revision: 337876
- New version 1.1.0.20090205

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080912-2mdv2009.1
+ Revision: 318668
- rebuild for new python

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080912-1mdv2009.1
+ Revision: 292260
- New version 0.1.1.20080912

* Fri Sep 05 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080901-1mdv2009.0
+ Revision: 281257
- new version

* Sun Aug 31 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080828-1mdv2009.0
+ Revision: 277704
- update to new version 0.1.1.20080828

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080823-1mdv2009.0
+ Revision: 275836
- fix pythondir
- import ibus-anthy


