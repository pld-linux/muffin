%define		_internal_version  392f000
Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		muffin
Version:	1.1.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://github.com/linuxmint/muffin/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e8b44ea43f041af680f94822d4a35032
URL:		https://github.com/linuxmint/muffin
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	clutter-devel >= 1.9.10
BuildRequires:	cogl-devel >= 1.9.6
BuildRequires:	desktop-file-utils
BuildRequires:	glib2-devel >= 1:2.25.10
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gsettings-desktop-schemas-devel >= 3.3.0
BuildRequires:	gtk-doc
BuildRequires:	gtk+3-devel >= 3.3.7
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.2
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	GConf2
Requires:	cairo >= 1.10.0
Requires:	clutter >= 1.9.10
Requires:	cogl >= 1.9.6
#Requires:	control-center-filesystem
Requires:	dbus-x11
Requires:	glib2 >= 1:2.25.10
Requires:	gtk+3 >= 3.3.7
Requires:	libcanberra-gtk3 >= 0.26
Requires:	pango >= 1.2.0
Requires:	startup-notification >= 0.7
Requires:	xorg-lib-libXcomposite >= 0.2
Requires:	zenity
Requires(post):	/sbin/ldconfig
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

%package devel
Summary:	Development package for Muffin
Summary(pl.UTF-8):	Pakiet programistyczny dla Muffina
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.9.10
Requires:	gsettings-desktop-schemas-devel >= 3.3.0
Requires:	gtk+3-devel >= 3.3.7
Requires:	xorg-lib-libX11-devel

%description devel
Header files for developing Muffin plugins. Also includes utilities
for testing Metacity/Muffin themes.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek Muffina. Pakiet zawiera
dodatkowo narzędzia do testowania motywów Metacity/Muffina.

%prep
%setup -q -n linuxmint-%{name}-%{_internal_version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ZENITY=/usr/bin/zenity \
	--disable-silent-rules \
	--disable-static \
	--enable-compile-warnings=minimum

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_XINERAMA HAVE_XFREE_XINERAMA HAVE_SHAPE HAVE_RANDR HAVE_STARTUP_NOTIFICATION"

for I in $SHOULD_HAVE_DEFINED; do
	if ! grep -q "define $I" config.h; then
		echo "$I was not defined in config.h"
		grep "$I" config.h
		exit 1
	else
		echo "$I was defined as it should have been"
		grep "$I" config.h
	fi
done

%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	DESTDIR=$RPM_BUILD_ROOT

# Remove libtool archives.
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

# Muffin contains a .desktop file so we just need to validate it
desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS HACKING doc/theme-format.txt
%attr(755,root,root) %{_bindir}/muffin
%attr(755,root,root) %{_bindir}/muffin-message
%{_mandir}/man1/muffin.1*
%{_mandir}/man1/muffin-message.1*
%{_desktopdir}/muffin.desktop
%dir %{_datadir}/muffin
%dir %{_datadir}/muffin/icons
%attr(755,root,root) %{_libdir}/libmuffin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmuffin.so.0
%{_libdir}/muffin/Meta-3.0.gir
%{_libdir}/muffin/Meta-3.0.typelib
%dir %{_libdir}/muffin
%dir %{_libdir}/muffin/plugins
%attr(755,root,root) %{_libdir}/muffin/plugins/default.so
%{_datadir}/GConf/gsettings/muffin-schemas.convert
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-muffin-windows.xml

# XXX: nothing uses this?
%dir %{_datadir}/gnome/wm-properties
%{_datadir}/gnome/wm-properties/muffin-wm.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/muffin-theme-viewer
%attr(755,root,root) %{_bindir}/muffin-window-demo
%attr(755,root,root) %{_libdir}/libmuffin.so
%{_includedir}/muffin
%{_datadir}/muffin/icons/muffin-window-demo.png
%{_pkgconfigdir}/libmuffin.pc
%{_pkgconfigdir}/muffin-plugins.pc
%{_mandir}/man1/muffin-theme-viewer.1*
%{_mandir}/man1/muffin-window-demo.1*
