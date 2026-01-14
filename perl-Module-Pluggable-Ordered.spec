#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Module
%define	pnam	Pluggable-Ordered
Summary:	Module::Pluggable::Ordered - call module plugins in a specified order
Summary(pl.UTF-8):	Module::Pluggable::Ordered - wywoływanie modułów-wtyczek w zadanej kolejności
Name:		perl-Module-Pluggable-Ordered
Version:	1.5
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9a33859fa3ff61a845035d44a2f73e8
URL:		http://search.cpan.org/dist/Module-Pluggable-Ordered/
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

%description -l pl.UTF-8
Ten moduł zachowuje się dokładnie tak samo jak Module::Pluggable,
obsługując wszystkie jego opcje, ale dodatkowo włącza do klasy metodę
call_plugins. call_plugins zachowuje się jak Class::Trigger; przyjmuje
nazwę metody i parametry. W przypadku wywołania powiedzmy:

__PACKAGE__->call_plugins("my_method", @something);

call_plugins przeszukuje moduły wtyczek znalezione przy użyciu
Module::Pluggable pod kątem tych, które dostarczają my_method_order.
Sortuje moduły liczbowo w oparciu o wynik tej metody i wywołuje po
kolei na nich $my_method(@something). Daje to efekt podobny trochę do
procesu inicjalizacji Systemu V, gdzie pliki mogą określić sekwencję
startową, w jakiej mają być wywoływane.

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
