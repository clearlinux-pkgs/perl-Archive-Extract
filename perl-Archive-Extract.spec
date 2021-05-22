#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Archive-Extract
Version  : 0.88
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Extract-0.88.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Archive-Extract-0.88.tar.gz
Summary  : 'Generic archive extracting mechanism'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Archive-Extract-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
generic archive extraction
Please refer to 'perldoc Archive::Extract' after installation for details.

%package dev
Summary: dev components for the perl-Archive-Extract package.
Group: Development
Provides: perl-Archive-Extract-devel = %{version}-%{release}
Requires: perl-Archive-Extract = %{version}-%{release}

%description dev
dev components for the perl-Archive-Extract package.


%package perl
Summary: perl components for the perl-Archive-Extract package.
Group: Default
Requires: perl-Archive-Extract = %{version}-%{release}

%description perl
perl components for the perl-Archive-Extract package.


%prep
%setup -q -n Archive-Extract-0.88
cd %{_builddir}/Archive-Extract-0.88

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Archive::Extract.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Archive/Extract.pm
