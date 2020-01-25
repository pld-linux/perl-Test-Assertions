#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Assertions
Summary:	Test::Assertions - a simple set of building blocks for both unit and runtime testing
Summary(pl.UTF-8):	Test::Assertions - prosty zestaw klocków do testów jednostkowych i czasu uruchomienia
Name:		perl-Test-Assertions
Version:	1.054
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71359868674fd4290bd7d9da407c1cda
URL:		http://search.cpan.org/dist/Test-Assertions/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Log::Trace)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Assertions provides a convenient set of tools for constructing
tests, such as unit tests or run-time assertion checks (like C's
ASSERT macro). Unlike some of the Test:: modules available on CPAN,
Test::Assertions is not limited to unit test scripts; for example it
can be used to check output is as expected within a benchmarking
script. When it is used for unit tests, it generates output in the
standard form for CPAN unit testing (under Test::Harness).

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Assertions
%{_mandir}/man3/*
