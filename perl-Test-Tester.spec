%define module	Test-Tester

Summary:	Ease testing test modules built with Test::Builder
Name:		perl-%{module}
Version:	0.109
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Tester-%{version}.tar.gz
Url:		https://search.cpan.org/dist/%{module}/

BuildRequires:	perl(Test::Builder)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%autosetup -p1 -n %{module}-%{version}
%__perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make_build test

%install
%make_install

%files
%doc CHANGES README TODO
%{_mandir}/*/*
%{perl_vendorlib}/Test/Tester
%{perl_vendorlib}/Test/Tester.pm
