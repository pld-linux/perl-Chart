%include	/usr/lib/rpm/macros.perl
Summary:	Chart perl module
Summary(pl):	Modu³ perla Chart
Name:		perl-Chart
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Chart/Chart-%{version}.tar.gz
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
%setup -q -n Chart-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO *txt
%dir %{perl_sitelib}/Chart
%{perl_sitelib}/Chart/*.pm
%{perl_sitelib}/Chart.pod
%{_mandir}/man3/*
