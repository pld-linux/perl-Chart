#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Chart
%define		pnam	Chart
Summary:	Chart - create .png or .jpg files with charts
Summary(pl):	Chart - tworzenie wykresów w formacie .png lub .jpg
Name:		perl-Chart
Version:	2.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	809540667dd703353af30147ef27b67d
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-GD}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chart - a series of charting modules.

%description -l pl
Chart - zestaw modu³ów do tworzenia wykresów.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/*.pdf
%{perl_vendorlib}/Chart/*.pm
