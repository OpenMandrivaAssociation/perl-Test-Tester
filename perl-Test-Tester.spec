%define module	Test-Tester
%define version	0.107
%define release %mkrel 6

Summary:	Ease testing test modules built with Test::Builder
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%{name}-buildroot/
BuildArch:	noarch

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README TODO
%{_mandir}/*/*
%{perl_vendorlib}/Test/Tester
%{perl_vendorlib}/Test/Tester.pm


