#
# Conditional build
%bcond_without	pipewire	# remote desktop via pipewire
%bcond_with	sysprof		# sysprof tracing support

Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		muffin
Version:	6.4.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/muffin/tags
Source0:	https://github.com/linuxmint/muffin/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f21cbdfc8efde459e0cfe6fd06ef65ed
URL:		https://github.com/linuxmint/muffin
BuildRequires:	EGL-devel
# <EGL/eglmesaext.h>
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libgbm-devel >= 10.3
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	atk-devel >= 1:2.5.3
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	cinnamon-desktop-devel >= 5.3
BuildRequires:	dbus-devel
BuildRequires:	fribidi-devel >= 1.0.0
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.67.3
BuildRequires:	gobject-introspection-devel >= 1.40
BuildRequires:	graphene-devel >= 1.9.3
BuildRequires:	gtk+3-devel >= 3.19.8
BuildRequires:	json-glib-devel >= 0.12.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libdrm-devel
BuildRequires:	libgudev-devel >= 232
BuildRequires:	libinput-devel >= 1.7
BuildRequires:	libwacom-devel >= 0.13
# xcb-randr xcb-res
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.30
%{?with_pipewire:BuildRequires:	pipewire-devel >= 0.3.0}
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	startup-notification-devel >= 0.7
%{?with_sysprof:BuildRequires:	sysprof-devel >= 3.35.2}
# or elogind-devel
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	udev-devel >= 1:228
# wayland-client wayland-server
BuildRequires:	wayland-devel >= 1.13.0
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.19
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.4
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 3
BuildRequires:	xorg-lib-libXi-devel >= 1.7.4
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.3
BuildRequires:	xorg-lib-libxkbcommon-x11-devel >= 0.4.3
BuildRequires:	xorg-lib-libxkbfile-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cinnamon-desktop >= 5.3
#Requires:	control-center-filesystem
Requires:	dbus-x11
Requires:	libcanberra-gtk3 >= 0.26
Requires:	startup-notification >= 0.7
Requires:	wayland >= 1.13.0
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
Requires:	cinnamon-desktop-libs >= 5.3
Requires:	glib2 >= 1:2.67.3
Requires:	graphene >= 1.9.3
Requires:	gtk+3 >= 3.19.8
Requires:	json-glib >= 0.12.0
Requires:	libgudev >= 232
Requires:	libwacom >= 0.13
Requires:	pango >= 1:1.30
Requires:	xorg-lib-libXcomposite >= 0.4
Requires:	xorg-lib-libXfixes >= 3
Requires:	xorg-lib-libXi >= 1.7.4
Requires:	xorg-lib-libXrandr >= 1.5.0

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
Requires:	OpenGL-devel
Requires:	OpenGLESv2-devel >= 2.0
Requires:	atk-devel >= 1:2.5.3
Requires:	cairo-devel >= 1.10
Requires:	cairo-gobject-devel >= 1.14.0
Requires:	cinnamon-desktop-devel >= 5.3
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.67.3
Requires:	graphene-devel >= 1.9.3
Requires:	gtk+3-devel >= 3.19.8
Requires:	json-glib-devel >= 0.12.0
Requires:	pango-devel >= 1:1.30
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 3
Requires:	xorg-lib-libXi-devel >= 1.7.4
Requires:	xorg-lib-libXrandr-devel >= 1.5.0
Requires:	xorg-lib-libXtst-devel
Obsoletes:	muffin-apidocs < 5.8

%description devel
Header files for developing Muffin plugins. Also includes utilities
for testing Metacity/Muffin themes.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek Muffina. Pakiet zawiera
dodatkowo narzędzia do testowania motywów Metacity/Muffina.

%prep
%setup -q

%build
%meson build \
	%{?with_sysprof:-Dprofiler=true} \
	%{!?with_pipewire:-Dremote_desktop=false} \
	-Dxwayland_initfd=enabled \
	-Dxwayland_path=/usr/bin/Xwayland

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/muffin
%attr(755,root,root) %{_libexecdir}/muffin-restart-helper
%dir %{_libdir}/muffin/plugins
%attr(755,root,root) %{_libdir}/muffin/plugins/libdefault.so
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.wayland.gschema.xml
%{_datadir}/glib-2.0/schemas/org.cinnamon.muffin.x11.gschema.xml
%{_desktopdir}/muffin.desktop
%{_mandir}/man1/muffin.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmuffin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmuffin.so.0
%attr(755,root,root) %{_libdir}/muffin/libmuffin-clutter-0.so.*
%attr(755,root,root) %{_libdir}/muffin/libmuffin-cogl-0.so.*
%attr(755,root,root) %{_libdir}/muffin/libmuffin-cogl-pango-0.so.*
%attr(755,root,root) %{_libdir}/muffin/libmuffin-cogl-path-0.so.*
%dir %{_libdir}/muffin
%{_libdir}/muffin/Cally-0.typelib
%{_libdir}/muffin/Clutter-0.typelib
%{_libdir}/muffin/ClutterX11-0.typelib
%{_libdir}/muffin/Cogl-0.typelib
%{_libdir}/muffin/CoglPango-0.typelib
%{_libdir}/muffin/Meta-0.typelib

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
%{_libdir}/muffin/Meta-0.gir
%{_includedir}/muffin
%{_pkgconfigdir}/libmuffin-0.pc
%{_pkgconfigdir}/muffin-clutter-0.pc
%{_pkgconfigdir}/muffin-clutter-x11-0.pc
%{_pkgconfigdir}/muffin-cogl-0.pc
%{_pkgconfigdir}/muffin-cogl-pango-0.pc
%{_pkgconfigdir}/muffin-cogl-path-0.pc
