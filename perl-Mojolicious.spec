%define oname    Mojolicious

Name:		perl-%{oname}
Version:	9.39
Release:	2
Summary:	A next generation web framework for Perl
License:	Artistic 2.0
Group:		Development/Perl
URL:		https://mojolicious.org/
Source0:	https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(Sub::Util)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(EV) >= 4.340.0
BuildArch:	noarch
Requires:	perl(IO::Socket::SSL)
Requires:	perl(Sub::Util)
Requires:	perl(EV) >= 4.340.0

%files
%doc Changes LICENSE examples
%{_bindir}/mojo
%{_bindir}/morbo
%{_bindir}/hypnotoad
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

#----------------------------------------------------------------------------

%description
Back in the early day of the web there was this wonderful Perl library
called CGI, many people only learned Perl because of it. It was simple
enough to get started without knowing much about the language and powerful
enough to keep you going, learning by doing was much fun. While most of the
techniques used are outdated now, the idea behind it is not. Mojolicious is
a new attempt at implementing this idea using state of the art technology.

%prep
%autosetup -n %{oname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build CFLAGS="%{optflags}"

%install
%make_install
