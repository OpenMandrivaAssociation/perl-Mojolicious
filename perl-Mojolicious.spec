%define upstream_name    Mojolicious
%define upstream_version 1.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
Summary:        A next generation web framework for Perl
License:        Artistic 2.0
Group:          Development/Perl
URL:            http://mojolicious.org/
Source0:        http://www.cpan.org/authors/id/K/KR/KRAIH/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildArch:	noarch

%description
Back in the early day of the web there was this wonderful Perl library
called CGI, many people only learned Perl because of it. It was simple
enough to get started without knowing much about the language and powerful
enough to keep you going, learning by doing was much fun. While most of the
techniques used are outdated now, the idea behind it is not. Mojolicious is
a new attempt at implementing this idea using state of the art technology.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean
rm -rf %buildroot


%files
%defattr(-,root,root,-)
%doc Changes LICENSE examples
%{_bindir}/mojo
%{_bindir}/hypnotoad
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

