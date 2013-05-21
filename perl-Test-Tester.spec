%define module	Test-Tester

Summary:	Ease testing test modules built with Test::Builder
Name:		perl-%{module}
Version:	0.107
Release:	10
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/

BuildRequires:	perl-devel
BuildArch:	noarch

%description
If you have written a test module based on Test::Builder then Test::Tester
allows you to test it with the minimum of effort.

%prep
%setup -q -n %{module}-%{version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.107-8mdv2012.0
+ Revision: 765751
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.107-7
+ Revision: 764256
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.107-6
+ Revision: 667391
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.107-5mdv2011.0
+ Revision: 430600
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.107-4mdv2009.0
+ Revision: 258580
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.107-3mdv2009.0
+ Revision: 246558
- rebuild

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.107-1mdv2008.1
+ Revision: 177898
- update to new version 0.107

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.106-1mdv2008.0
+ Revision: 78721
- update to new version 0.106

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.105-1mdv2008.0
+ Revision: 75232
- update to new version 0.105


* Tue Jan 09 2007 Olivier Thauvin <nanardon@mandriva.org> 0.104-1mdv2007.0
+ Revision: 106250
- 0.104

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Test-Tester

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.103-3mdk
- Fix SPEC according to Perl Policy
	- Source URL
- Remove perl Require

* Mon Mar 06 2006 Buchan Milne <bgmilne@mandriva.org> 0.103-2mdk
- Rebuild
- use mkrel

* Wed Oct 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.103-1mdk
- Initial MDV release

