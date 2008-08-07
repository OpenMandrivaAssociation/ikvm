%define name ikvm
%define version 0.36.0.11
%define release %mkrel 2
%define classpath 0.95
%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif

Summary: Java implementation for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/ikvm/%{name}-%{version}.zip
Source1: http://www.frijters.net/classpath-%classpath-stripped.zip
Source2: ikvm
Source3: ikvmc
Source4: ikvmstub
Source5: ikvm.pc
Source6: http://www.frijters.net/openjdk-b13-stripped.zip
Patch: classpath-0.95-awt-image-raster-fix.patch
License: GPL-like
Group: Development/Java
Url: http://www.ikvm.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: nant
BuildRequires: java-1.7.0-icedtea-devel
Requires: mono

%description
IKVM.NET is a JVM for Mono and the Microsoft .NET framework.

%prep
%setup -q -a 1 -a 6
%patch -p0
perl -pi -e "s^\.\./\.\.^..^" classpath/allsources.lst classpath/classpath.build openjdk/allsources.lst openjdk/openjdk.build

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
%doc LICENSE THANKYOU website/build/site
%_bindir/*
%_prefix/lib/%name
%pkgconfigdir/*.pc


