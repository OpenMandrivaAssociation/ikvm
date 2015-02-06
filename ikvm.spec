%define name ikvm
%define version 0.46.0.2
%define release 2
%define openjdk b22
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif

Summary: Java implementation for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.frijters.net/%{name}src-%{version}.zip
Source2: ikvm
Source3: ikvmc
Source4: ikvmstub
Source5: ikvm.pc
Source6: http://www.frijters.net/openjdk6-%openjdk-stripped.zip
License: GPL-like
Group: Development/Java
Url: http://www.ikvm.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: nant
BuildRequires: java-1.7.0-icedtea-devel
BuildRequires: glib2-devel
Requires: mono

%description
IKVM.NET is a JVM for Mono and the Microsoft .NET framework.

%prep
%setup -q -a 6
#gw fix paths for our source directory layout
perl -pi -e "s^\.\./\.\.^..^" classpath/allsources.lst classpath/classpath.build openjdk/allsources.lst openjdk/openjdk.build openjdk/response.txt
mkdir bin
cp %_prefix/lib/mono/2.0/ICSharpCode.SharpZipLib.dll bin/

%build
export PATH=`pwd`/bin:$PATH
nant -nologo clean
nant -nologo

%install
rm -rf $RPM_BUILD_ROOT
install -D %SOURCE2 -m 755 %buildroot%_bindir/ikvm
install -D %SOURCE3 -m 755 %buildroot%_bindir/ikvmc
install -D %SOURCE4 -m 755 %buildroot%_bindir/ikvmstub
install -D %SOURCE5 -m 644 %buildroot%pkgconfigdir/ikvm.pc
perl -pi -e "s^0.14^%version^" %buildroot%pkgconfigdir/ikvm.pc
mkdir -p %buildroot%_prefix/lib/%name
cp bin/*.exe bin/IKVM*.dll %buildroot%_prefix/lib/%name


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE TH* HOWTO
%_bindir/*
%_prefix/lib/%name
%pkgconfigdir/*.pc




%changelog
* Wed Dec 21 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.46.0.2-1mdv2012.0
+ Revision: 744102
- new version

* Thu Mar 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.46.0.1-1
+ Revision: 648268
- new version
- update openjdk to b22
- remove unneeded classpath sources

* Fri Oct 22 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.44.0.6-1mdv2011.0
+ Revision: 587238
- update build deps
- new version

* Mon Aug 23 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.44.0.5-1mdv2011.0
+ Revision: 572418
- new version

* Tue Aug 10 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.44.0.4-1mdv2011.0
+ Revision: 568309
- new version

* Thu Aug 05 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.44.0.3-0mdv2011.0
+ Revision: 566280
- new version
- new openjdk b18
- fix build

* Tue Jul 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.42.0.7-1mdv2011.0
+ Revision: 560904
- new version (security update)

* Sun Jul 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.42.0.6-1mdv2011.0
+ Revision: 550987
- new version

* Mon Jan 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.42.0.3-1mdv2010.1
+ Revision: 489588
- new version
- new openjdk source

* Thu Jun 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.40.0.1-1mdv2010.0
+ Revision: 385032
- new version
- fix build
- update openjdk snapshot

* Mon Dec 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.38.0.2-1mdv2009.1
+ Revision: 320995
- new version
- new openjdk

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.36.0.11-2mdv2009.0
+ Revision: 267113
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.36.0.11-1mdv2009.0
+ Revision: 192449
- new version
- add classpath awt fix
- fix pkgconfig file
- it is buildable on x86_64 again

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.36.0.5-1mdv2008.1
+ Revision: 117572
- don't try to build on x86_64
- new version
- replace classpath with classpath-stripped and openjdk-stripped
- build with icedtea instead of ecj

* Tue Sep 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.34.0.4-2mdv2008.0
+ Revision: 89507
- remove excludearch tag

* Mon Aug 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.34.0.4-1mdv2008.0
+ Revision: 59276
- new version

* Thu May 31 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.34.0.3-1mdv2008.0
+ Revision: 33443
- new version

* Sun May 06 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.34.0.2-1mdv2008.0
+ Revision: 23687
- new version
- new classpath


* Sat Dec 30 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.32.0.0-2mdv2007.0
+ Revision: 102778
- exclude x86_64 for bug 27871
- Import ikvm

* Fri Dec 29 2006 Götz Waschk <waschk@mandriva.org> 0.32.0.0-1mdv2007.1
- drop patch
- classpath 0.93
- 0.32.0.0

* Sat Aug 19 2006 Götz Waschk <waschk@mandriva.org> 0.30.0.0-1mdv2007.0
- drop source 2
- patch out unsupported preprocessor directive
- drop patch
- new classpath
- new version

* Fri Jul 28 2006 Götz Waschk <waschk@mandriva.org> 0.28.0.1-1mdv2007.0
- patch classpath
- new classpath 0.91
- New release 0.28.0.0

* Thu Mar 23 2006 Götz Waschk <waschk@mandriva.org> 0.26.0.1-1mdk
- new classpath 0.90
- New release 0.26.0.1

* Mon Jan 30 2006 Götz Waschk <waschk@mandriva.org> 0.24.0.1-1mdk
- upgrade classpath
- New release 0.24.0.1
- use mkrel

* Mon Dec 12 2005 Götz Waschk <waschk@mandriva.org> 0.22.0.0-1mdk
- new classpath 0.19
- new release 0.22.0.0

* Mon Sep 12 2005 Götz Waschk <waschk@mandriva.org> 0.20.0.0-1mdk
- new classpath 0.18
- New release 0.20.0.0

* Tue Jul 26 2005 Götz Waschk <waschk@mandriva.org> 0.18.0.0-2mdk
- remove the prebuilt binaries

* Tue Jul 26 2005 Götz Waschk <waschk@mandriva.org> 0.18.0.0-1mdk
- buildrequires ecj
- update classpath to 0.17
- drop patch
- new version

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 0.14.0.1-1mdk
- initial package

