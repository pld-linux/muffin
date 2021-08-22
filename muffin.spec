Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		muffin
Version:	4.8.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/muffin/releases
Source0:	https://github.com/linuxmint/muffin/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fe0ca2d74999f78b4abc2a6a98a058c2
Patch0:		%{name}-gir.patch
URL:		https://github.com/linuxmint/muffin
BuildRequires:	EGL-devel
BuildRequires:	Mesa-libGL-devel
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	autoconf-archive
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	cinnamon-desktop-devel >= 2.4.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.3
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk+3-devel >= 3.9.12
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	intltool >= 0.35.0
BuildRequires:	json-glib-devel
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libtool >= 2:2.2.6
# xcb-randr xcb-res
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel >= 1:1.14.0
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.3
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.6.0
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.3
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cinnamon-desktop >= 2.4.0
#Requires:	control-center-filesystem
Requires:	dbus-x11
Requires:	libcanberra-gtk3 >= 0.26
Requires:	startup-notification >= 0.7
Requires:	zenity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Muffin is a window and compositing manager that displays and manages
your desktop via OpenGL. Muffin combines a sophisticated display
engine using the Clutter toolkit with solid window-management logic
inherited from the Metacity window manager.

While Muffin can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as Cinnamon. For this
reason, Muffin is very extensible via plugins, which are used both to
add fancy visual effects and to rework the window management behaviors
to meet the needs of the environment.

%description -l pl.UTF-8
Muffin to zarządca okien i składania, wyświetlający i zarządzający
pulpitem poprzez OpenGL. Muffin łączy przemyślany silnik wyświetlania
wykorzystujący toolkit Clutter z solidną logiką zarządcy okien
odziedziczoną z zarządcy okien Metacity.

Mimo że Muffin może być używany samodzielnie, jest pomyślany głównie
jako główny element większego systemu, takiego jak Cinnamon. Z tego
powodu Muffin może być znacząco rozszerzany poprzez wtyczki, które
mogą zarówno dodawać ładne efekty wizualne, jak i zmieniać zachowanie
zarządzania oknami, aby pasowały do potrzeb środowiska.

%package libs
Summary:	Muffin shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Muffina
Group:		X11/Libraries
Requires:	atk >= 1:2.5.3
Requires:	cairo >= 1.10
Requires:	cairo-gobject >= 1.14.0
Requires:	cinnamon-desktop-libs >= 2.4.0
Requires:	glib2 >= 1:2.50.3
Requires:	gtk+3 >= 3.9.12
Requires:	json-glib >= 0.12.0
Requires:	pango >= 1:1.30
Requires:	xorg-lib-libXcomposite >= 0.4
Requires:	xorg-lib-libXfixes >= 3
Requires:	xorg-lib-libXi >= 1.6.0
Requires:	xorg-lib-libXrandr >= 1.2

%description libs
Muffin shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone Muffina.

%package devel
Summary:	Development package for Muffin
Summary(pl.UTF-8):	Pakiet programistyczny dla Muffina
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	EGL-devel
Requires:	atk-devel >= 1:2.5.3
Requires:	cairo-devel >= 1.10
Requires:	cairo-gobject-devel >= 1.14.0
Requires:	cinnamon-desktop-devel >= 2.4.0
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.50.3
Requires:	gtk+3-devel >= 3.9.12
Requires:	json-glib-devel >= 0.12.0
Requires:	pango-devel >= 1:1.30
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 3
Requires:	xorg-lib-libXi-devel >= 1.6.0
Requires:	xorg-lib-libXrandr-devel >= 1.2
Requires:	xorg-lib-libXtst-devel

%description devel
Header files for developing Muffin plugins. Also includes utilities
for testing Metacity/Muffin themes.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek Muffina. Pakiet zawiera
dodatkowo narzędzia do testowania motywów Metacity/Muffina.

%package apidocs
Summary:	API documentation for Muffin libraries
Summary(pl.UTF-8):	Dokumentacja API bibliotek Muffina
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Muffin libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Muffina.

%prep
%setup -q
%patch0 -p1

%build
install -d m4
%{__glib_gettextize}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd cogl
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../clutter
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%configure \
	ZENITY=%{_bindir}/zenity \
	--disable-silent-rules \
	--disable-static \
	--enable-compile-warnings=minimum \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la \
	$RPM_BUILD_ROOT%{_libdir}/muffin/*.la

# Muffin contains a .desktop file so we just need to validate it
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%{__mv} $RPM_BUILD_ROOT%{_gtkdocdir}/{clutter,muffin-clutter}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/muffin
%attr(755,root,root) %{_bindir}/muffin-message
%attr(755,root,root) %{_bindir}/muffin-theme-viewer
%attr(755,root,root) %{_bindir}/muffin-window-demo
%attr(755,root,root) %{_libexecdir}/muffin-restart-helper
%dir %{_libdir}/muffin/plugins
%attr(755,root,root) %{_libdir}/muffin/plugins/default.so
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%dir %{_datadir}/muffin
%dir %{_datadir}/muffin/icons
%{_datadir}/muffin/icons/muffin-window-demo.png
%dir %{_datadir}/muffin/theme
%{_datadir}/muffin/theme/metacity-theme-3.xml
%{_desktopdir}/muffin.desktop
%{_mandir}/man1/muffin.1*
%{_mandir}/man1/muffin-message.1*
%{_mandir}/man1/muffin-theme-viewer.1*
%{_mandir}/man1/muffin-window-demo.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmuffin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmuffin.so.0
%attr(755,root,root) %{_libdir}/libmuffin-clutter-0.so
%attr(755,root,root) %{_libdir}/libmuffin-cogl-0.so
%attr(755,root,root) %{_libdir}/libmuffin-cogl-pango-0.so
%attr(755,root,root) %{_libdir}/libmuffin-cogl-path-0.so
%dir %{_libdir}/muffin
%{_libdir}/muffin/Cally-0.typelib
%{_libdir}/muffin/Clutter-0.typelib
%{_libdir}/muffin/ClutterX11-0.typelib
%{_libdir}/muffin/Cogl-0.typelib
%{_libdir}/muffin/CoglPango-0.typelib
%{_libdir}/muffin/Meta-Muffin.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmuffin.so
%attr(755,root,root) %{_libdir}/muffin/libmuffin-clutter-0.so
%attr(755,root,root) %{_libdir}/muffin/libmuffin-cogl-0.so
%attr(755,root,root) %{_libdir}/muffin/libmuffin-cogl-pango-0.so
%attr(755,root,root) %{_libdir}/muffin/libmuffin-cogl-path-0.so
%{_libdir}/muffin/Cally-0.gir
%{_libdir}/muffin/Clutter-0.gir
%{_libdir}/muffin/ClutterX11-0.gir
%{_libdir}/muffin/Cogl-0.gir
%{_libdir}/muffin/CoglPango-0.gir
%{_libdir}/muffin/Meta-Muffin.0.gir
%{_includedir}/muffin
%{_pkgconfigdir}/libmuffin.pc
%{_pkgconfigdir}/muffin-clutter-0.pc
%{_pkgconfigdir}/muffin-clutter-x11-0.pc
%{_pkgconfigdir}/muffin-cogl-0.pc
%{_pkgconfigdir}/muffin-cogl-pango-0.pc
%{_pkgconfigdir}/muffin-cogl-path-0.pc
%{_pkgconfigdir}/muffin-plugins.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/muffin
%{_gtkdocdir}/muffin-clutter
