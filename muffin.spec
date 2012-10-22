%define		_internal_version  392f000
Summary:	Window and compositing manager based on Clutter
Name:		muffin
Version:	1.1.1
Release:	1.1
License:	GPL v2+
Group:		X11/Applications
URL:		https://github.com/linuxmint/muffin
Source0:	https://github.com/linuxmint/muffin/tarball/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e8b44ea43f041af680f94822d4a35032
BuildRequires:	GConf2-devel
BuildRequires:	clutter-devel >= 1.5.8
BuildRequires:	desktop-file-utils
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 2.99.0
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	zenity
# Bootstrap requirements
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libcanberra-devel
Requires:	GConf2
#Requires:	control-center-filesystem
Requires:	dbus-x11
Requires:	startup-notification
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

%package devel
Summary:	Development package for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and libraries for developing Muffin plugins. Also
includes utilities for testing Metacity/Muffin themes.

%prep
%setup -q -n linuxmint-%{name}-%{_internal_version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-compile-warnings=minimum \

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
%ghost %{_libdir}/libmuffin.so.0
%{_libdir}/muffin/Meta-3.0.gir
%{_libdir}/muffin/Meta-3.0.typelib
%dir %{_libdir}/muffin
%dir %{_libdir}/muffin/plugins
%{_libdir}/muffin/plugins/default.so
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
%{_includedir}/muffin
%{_libdir}/libmuffin.so
%{_datadir}/muffin/icons/muffin-window-demo.png
%{_pkgconfigdir}/libmuffin.pc
%{_pkgconfigdir}/muffin-plugins.pc
%{_mandir}/man1/muffin-theme-viewer.1*
%{_mandir}/man1/muffin-window-demo.1*
