%include	/usr/lib/rpm/macros.perl
Summary:	Chart perl module
Summary(pl):	Modu³ perla Chart
Name:		perl-Chart
Version:	0.99b
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Chart/Chart-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-GD
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Chart - a series of charting modules.

%description -l pl
Chart - zestaw modu³ów do tworzenia wykresów.

%prep
%setup -q -n Chart-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Chart
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,rgb.txt}.gz

%dir %{_perl_sitelib}/Chart
%{perl_sitelib}/Chart/*.pm
%{perl_sitearch}/auto/Chart

%{_mandir}/man3/*
