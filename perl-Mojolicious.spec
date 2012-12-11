%define upstream_name    Mojolicious
%define upstream_version 1.43

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	A next generation web framework for Perl
License:	Artistic 2.0
Group:		Development/Perl
URL:		http://mojolicious.org/
Source0:	http://www.cpan.org/authors/id/K/KR/KRAIH/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)
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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE examples
%{_bindir}/mojo
%{_bindir}/hypnotoad
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Wed Jun 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.430.0-1mdv2011.0
+ Revision: 685331
- update to new version 1.43

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.420.0-1
+ Revision: 684775
- update to new version 1.42

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.340.0-1
+ Revision: 682136
- update to new version 1.34

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1
+ Revision: 677373
- update to new version 1.33

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.320.0-1
+ Revision: 673814
- update to new version 1.32

* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.310.0-1
+ Revision: 672855
- update to new version 1.31

* Fri May 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.300.0-1
+ Revision: 669865
- fix check section
- new version 1.3

* Wed May 04 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.220.0-1
+ Revision: 665986
- new version 1.22

* Wed Apr 20 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.210.0-1
+ Revision: 656280
- import perl-Mojolicious

