#
# Conditional build:
# _without_ipv6		- don't build with IPv6 support
# _without_fun		- disable fun
#
Summary:	GTK2-based FTP Client
Summary(pl):	Klient FTP (GTK2)
Name:		junkie
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}%{version}.tar.gz
# Source0-md5:	7cc23dbe9135775bde0299c1759aa812
URL:		http://www.sourceforge.net/projects/%{name}/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Junkie is a stable GTK2 FTP client for the X Window System. It has
features such as queueing files, download/uploading of whole
directories, caching of directories, drag and drop, a site manager,
preferences (and a configure library), and an event-based FTP library,
which means that the client should be stable and not slow the user
interface down much

%description -l pl
Junkie jest stabilnym klientem FTP (GTK2) dla systemu X Window.
Cechuje si� mi�dzy innymi kolejkowaniem plik�w, �ciaganiem/wysy�aniem
ca�ych katalog�w, cache'owaniem katalog�w, wykorzystaniem mechanizmu
"Przeci�gnij i upu��" (drag and drop), mened�erem zapami�tanych
adres�w, mo�liwo�ci� konfiguracji. Junkie korzysta z w�asnej
biblioteki, dzi�ki czemu nie powinien zbytnio spowalnia� interfejsu
u�ytkownika.

%prep
%setup -q -n %{name}%{version}

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?_without_ipv6:--enable-ipv6} \
	%{?_without_fun:--disable-fun}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
