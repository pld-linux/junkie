# Bcond:
#  - _without_ipv6 - don't build with IPv6 support
#  - _without_fun  - disable fun
Summary:	GTK2-based FTP Client
Summary(pl):	Klient FTP (GTK2)
Name:		junkie
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/%{name}/
BuildRequires:	pkg-config
BuildRequires:	glib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Junkie is a stable GTK2 FTP client for the X Windows system. It has
features such as queueing files, download/uploading of whole
directories, caching of directories, drag and drop, a site manager,
preferences (and a configure library), and an event-based FTP library,
which means that the client should be stable and not slow the user
interface down much

%description -l pl
Junkie jest stabilnym klientem FTP (GTK2) dla systemu X windows.
Cechuje siê miêdzy innymi kolejkowaniem plików, ¶ciaganiem/wysy³aniem
ca³ych katalogów, cache'owaniem katalogów, "Przeci±gnij i upu¶æ" (drag
and drop), mened¿er zapamiêtanych adresów, mo¿liwo¶æ konfiguracji.
Junkie korzysta z w³asnej biblioteki, dziêki czemu nie powinien
zbytnio spowalniaæ interfejsu u¿ytkownika.

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
