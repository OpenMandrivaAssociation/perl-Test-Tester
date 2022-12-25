%define module	Test-Tester
%define upstream_version 0.109

Summary:	Ease testing test modules built with Test::Builder
Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Test/Test-Tester-%{upstream_version}.tar.gz
Url:		http://search.cpan.org/dist/%{module}/

BuildRequires:	perl(Test::Builder)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%setup -qn %{module}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README TODO
%{_mandir}/*/*
%{perl_vendorlib}/Test/Tester
%{perl_vendorlib}/Test/Tester.pm
