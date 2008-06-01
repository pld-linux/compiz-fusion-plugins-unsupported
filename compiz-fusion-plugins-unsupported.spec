Summary:	Unsupported Compiz Fusion plugins
Summary(pl.UTF-8):	Niewspierane wtyczki Compiz Fusion
Name:		compiz-fusion-plugins-unsupported
Version:	0.7.6
Release:	1
License:	GPL v2+
Group:		X11
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	de511745f755166326d9d361e9a3dba3
URL:		http://forum.compiz-fusion.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	compiz-bcop >= %{version}
BuildRequires:	compiz-devel >= %{version}
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	compiz >= %{version}
Obsoletes:	beryl-plugins
Obsoletes:	beryl-plugins-unsupported
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fakeargb: Makes a special color of a window transparent.
Mswitch: Enables the switching of viewports with mouse gestures.
Snow: Displays falling snow over the desktop and windows.
Tile: Enables the tiling of windows on the desktop in a manner similar
    to ion3.

%description -l pl.UTF-8
Fakeargb: Sprawia, że wybrany kolor staje się przezroczystym.
Mswitch: Umożliwia przełączanie viewportów za pomocą gestów myszy.
Snow: Wyświetla spadający śnieg nad pulpitem i oknami.
Tile: Umożliwia kafelkowanie okien na pulpicie w podobny sposób jak
    ion3.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize} --automake
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/compiz/*.so
%{_datadir}/compiz/*.xml
%{_datadir}/compiz/*.png
