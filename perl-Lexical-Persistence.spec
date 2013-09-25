%define upstream_name    Lexical-Persistence
%define upstream_version 1.023

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Bind lexicals to persistent data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lexical/Lexical-Persistence-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::LexAlias)
BuildRequires:	perl(PadWalker)
BuildArch:	noarch

%description
Lexical::Persistence does a few things, all related. Note that all the
behaviors listed here are the defaults. Subclasses can override nearly
every aspect of Lexical::Persistence's behavior.

Lexical::Persistence lets your code access persistent data through lexical
variables. This example prints "some value" because the value of $x perists
in the $lp object between setter() and getter().

	use Lexical::Persistence;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 654244
- rebuild for updated spec-helper

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 515750
- update to 1.020

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-2mdv2010.0
+ Revision: 408649
- force rebuild
- update to 1.01

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.980.0-1mdv2010.0
+ Revision: 401639
- rebuild using %%perl_convert_version
- fixed license field

* Wed Dec 03 2008 Jérôme Quelin <jquelin@mandriva.org> 0.98-1mdv2009.1
+ Revision: 309772
- import perl-Lexical-Persistence


* Wed Dec 03 2008 cpan2dist 0.98-1mdv
- initial mdv release, generated with cpan2dist


