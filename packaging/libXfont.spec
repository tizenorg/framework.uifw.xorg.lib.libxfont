Summary: X.Org X11 libXfont runtime library
Name: libXfont
Version: 1.4.5
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(fontsproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires: xorg-x11-xutils-dev
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-3
BuildRequires: libfontenc-devel
BuildRequires: freetype-devel

%description
X.Org X11 libXfont runtime library

%package devel
Summary: X.Org X11 libXfont development package
Group: Development/Libraries
Provides: libxfont-devel 
Requires: %{name} = %{version}-%{release}
Requires: libfontenc-devel

%description devel
X.Org X11 libXfont development package

%prep
%setup -q

%build
export CFLAGS="${CFLAGS} $RPM_OPT_FLAGS -Os"
%reconfigure --disable-static \
           --enable-fc --enable-builtins --enable-pcfformat --enable-bdfformat --without-bzip2 \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

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