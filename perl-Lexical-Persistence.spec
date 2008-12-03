
%define realname   Lexical-Persistence
%define version    0.98
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Bind lexicals to persistent data
Source:     http://www.cpan.org/modules/by-module/Lexical/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Devel::LexAlias)
BuildRequires: perl(PadWalker)

BuildArch: noarch

%description
Lexical::Persistence does a few things, all related. Note that all the
behaviors listed here are the defaults. Subclasses can override nearly
every aspect of Lexical::Persistence's behavior.

Lexical::Persistence lets your code access persistent data through lexical
variables. This example prints "some value" because the value of $x perists
in the $lp object between setter() and getter().

	use Lexical::Persistence;

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*


