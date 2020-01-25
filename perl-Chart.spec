#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Chart
Summary:	Chart - create .png or .jpg files with charts
Summary(pl.UTF-8):	Chart - tworzenie wykresów w formacie .png lub .jpg
Name:		perl-Chart
Version:	2.4.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	977026fa73c0fc1e900f1ebe5eee06b7
URL:		http://search.cpan.org/dist/Chart/
%{?with_tests:BuildRequires:	perl-GD}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chart - a series of charting modules.

%description -l pl.UTF-8
Chart - zestaw modułów do tworzenia wykresów.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Chart/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Chart.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorlib}/Chart/*.pm
%{_mandir}/man3/Chart.3pm*
