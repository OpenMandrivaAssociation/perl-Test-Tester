%define module	Test-Tester

Summary:	Ease testing test modules built with Test::Builder
Name:		perl-%{module}
Version:	0.107
Release:	13
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%setup -qn %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README TODO
%{perl_vendorlib}/Test/Tester
%{perl_vendorlib}/Test/Tester.pm
%{_mandir}/man3/*

