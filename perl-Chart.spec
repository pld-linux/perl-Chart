#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir    Chart
%define		pnam    Chart
Summary:	Chart Perl module
Summary(cs):	Modul Chart pro Perl
Summary(da):	Perlmodul Chart
Summary(de):	Chart Perl Modul
Summary(es):	Módulo de Perl Chart
Summary(fr):	Module Perl Chart
Summary(it):	Modulo di Perl Chart
Summary(ja):	Chart Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Chart ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Chart
Summary(pl):	Modu³ Perla Chart
Summary(pt):	Módulo de Perl Chart
Summary(pt_BR):	Módulo Perl Chart
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Chart
Summary(sv):	Chart Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Chart
Summary(zh_CN):	Chart Perl Ä£¿é
Name:		perl-Chart
Version:	1.0.1
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-GD
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chart - a series of charting modules.

%description -l pl
Chart - zestaw modu³ów do tworzenia wykresów.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *txt
%{perl_sitelib}/Chart/*.pm
%{_mandir}/man3/*
