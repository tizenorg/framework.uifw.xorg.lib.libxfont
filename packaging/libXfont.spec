
Name:       libXfont
Summary:    X.Org X11 libXfont runtime library
Version:    1.4.3
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontcacheproto)


%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font file
formats, and rasterizing them



%package devel
Summary:    X.Org X11 libXfont development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
the legacy X11 font system development files


%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-static \
    --enable-fc --enable-builtins --enable-pcfformat --enable-bdfformat --without-bzip2

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# FIXME:  Missing README/INSTALL - should file bug upstream.
#%doc AUTHORS COPYING README INSTALL ChangeLog NEWS
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXfont.so.1
%{_libdir}/libXfont.so.1.4.1


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/bdfint.h
%{_includedir}/X11/fonts/bitmap.h
%{_includedir}/X11/fonts/bufio.h
%{_includedir}/X11/fonts/fntfil.h
%{_includedir}/X11/fonts/fntfilio.h
%{_includedir}/X11/fonts/fntfilst.h
%{_includedir}/X11/fonts/fontconf.h
%{_includedir}/X11/fonts/fontencc.h
%{_includedir}/X11/fonts/fontmisc.h
%{_includedir}/X11/fonts/fontshow.h
%{_includedir}/X11/fonts/fontutil.h
%{_includedir}/X11/fonts/fontxlfd.h
%{_includedir}/X11/fonts/pcf.h
%{_includedir}/X11/fonts/ft.h
%{_includedir}/X11/fonts/ftfuncs.h
%{_libdir}/libXfont.so
%{_libdir}/pkgconfig/xfont.pc

