#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-tv4
Version  : 1.2.7.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/2b/26/b07115af27b339c861b8c9a775a621524b421c898e26e015880dfb888c49/XStatic-tv4-1.2.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/26/b07115af27b339c861b8c9a775a621524b421c898e26e015880dfb888c49/XStatic-tv4-1.2.7.0.tar.gz
Summary  : tv4 1.2.7 (XStatic packaging standard)
Group    : Development/Tools
License  : Public-Domain
Requires: XStatic-tv4-python = %{version}-%{release}
Requires: XStatic-tv4-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
---------------
        
        Angular JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-tv4 package.
Group: Default
Requires: XStatic-tv4-python3 = %{version}-%{release}
Provides: xstatic-tv4-python

%description python
python components for the XStatic-tv4 package.


%package python3
Summary: python3 components for the XStatic-tv4 package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_tv4)

%description python3
python3 components for the XStatic-tv4 package.


%prep
%setup -q -n XStatic-tv4-1.2.7.0
cd %{_builddir}/XStatic-tv4-1.2.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583696304
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
