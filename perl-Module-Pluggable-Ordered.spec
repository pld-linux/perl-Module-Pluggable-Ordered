#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Pluggable-Ordered
Summary:	Module::Pluggable::Ordered - call module plugins in a specified order
Summary(pl):	Module::Pluggable::Ordered - wywo�ywanie modu��w-wtyczek w zadanej kolejno�ci
Name:		perl-Module-Pluggable-Ordered
Version:	1.4
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a63e0c325b9690680d7ee6ac34e178d0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Module-Pluggable >= 1.9
BuildRequires:	perl-UNIVERSAL-require
%endif
Requires:	perl-dirs >= 1.0-5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module behaves exactly the same as Module::Pluggable, supporting
all of its options, but also mixes in the call_plugins method to your
class. call_plugins acts a little like Class::Trigger; it takes the
name of a method, and some parameters. Let's say we call it like so:

__PACKAGE__->call_plugins("my_method", @something);

call_plugins looks at the plugin modules found using Module::Pluggable
for ones which provide my_method_order. It sorts the modules
numerically based on the result of this method, and then calls
$my_method(@something) on them in order. This produces an effect a
little like the System V init process, where files can specify where
in the init sequence they want to be called.

%description -l pl
Ten modu� zachowuje si� dok�adnie tak samo jak Module::Pluggable,
obs�uguj�c wszystkie jego opcje, ale dodatkowo w��cza do klasy metod�
call_plugins. call_plugins zachowuje si� jak Class::Trigger; przyjmuje
nazw� metody i parametry. W przypadku wywo�ania powiedzmy:

__PACKAGE__->call_plugins("my_method", @something);

call_plugins przeszukuje modu�y wtyczek znalezione przy u�yciu
Module::Pluggable pod k�tem tych, kt�re dostarczaj� my_method_order.
Sortuje modu�y liczbowo w oparciu o wynik tej metody i wywo�uje po
kolei na nich $my_method(@something). Daje to efekt podobny troch� do
procesu inicjalizacji Systemu V, gdzie pliki mog� okre�li� sekwencj�
startow�, w jakiej maj� by� wywo�ywane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Module/Pluggable/*.pm
%{_mandir}/man3/*
