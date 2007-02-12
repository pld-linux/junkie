#
# Conditional build:
%bcond_without	ipv6		# don't build with IPv6 support
%bcond_without	fun		# disable fun
#
Summary:	GTK2-based FTP Client
Summary(pl.UTF-8):   Klient FTP (GTK2)
Name:		junkie
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/junkie/%{name}%{version}.tar.gz
# Source0-md5:	7cc23dbe9135775bde0299c1759aa812
URL:		http://www.sourceforge.net/projects/junkie/
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

%description -l pl.UTF-8
Junkie jest stabilnym klientem FTP (GTK2) dla systemu X Window.
Cechuje się między innymi kolejkowaniem plików, ściąganiem/wysyłaniem
całych katalogów, cache'owaniem katalogów, wykorzystaniem mechanizmu
"Przeciągnij i upuść" (drag and drop), menedżerem zapamiętanych
adresów, możliwością konfiguracji. Junkie korzysta z własnej
biblioteki, dzięki czemu nie powinien zbytnio spowalniać interfejsu
użytkownika.

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
	%{?with_ipv6:--enable-ipv6} \
	%{!?with_fun:--disable-fun}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
