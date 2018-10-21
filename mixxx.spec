Summary:	Mixxx - DJ tool
Summary(hu.UTF-8):	Mixxx - DJ program
Summary(pl.UTF-8):	Mixxx - narzędzie dla DJ-ów
Name:		mixxx
Version:	1.11.0
Release:	6
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://downloads.mixxx.org/mixxx-%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	89ee8ba60824919d8dd1194287bda259
Patch0:		desktop.patch
Patch1:		%{name}-libdir.patch
URL:		http://mixxx.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt3Support-devel >= 4.6
BuildRequires:	QtCore-devel >= 4.6
BuildRequires:	QtGui-devel >= 4.6
BuildRequires:	QtNetwork-devel >= 4.6
BuildRequires:	QtOpenGL-devel >= 4.6
BuildRequires:	QtScript-devel >= 4.6
BuildRequires:	QtSql-devel >= 4.6
BuildRequires:	QtSvg-devel >= 4.6
BuildRequires:	QtXml-devel >= 4.6
BuildRequires:	QtXmlPatterns-devel >= 4.6
BuildRequires:	audiofile-devel
BuildRequires:	faad2-devel >= 2.7
BuildRequires:	fftw3-devel >= 3
BuildRequires:	flac-devel
# for ipod=1
#BuildRequires:	glib2-devel >= 2.0
BuildRequires:	jack-audio-connection-kit-devel
# for ipod=1
#BuildRequires:	libgpod-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libogg-devel
BuildRequires:	libshout-devel >= 2
BuildRequires:	libsndfile-devel
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libvorbis-devel
BuildRequires:	mp4v2-devel
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	portaudio-devel >= 19
BuildRequires:	portmidi-devel >= 217
BuildRequires:	protobuf-devel
BuildRequires:	qt4-build >= 4.6
BuildRequires:	qt4-linguist >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRequires:	taglib-devel
BuildRequires:	vamp-devel >= 2.3
BuildRequires:	wavpack-devel
BuildRequires:	xorg-lib-libX11-devel
Requires:	QtSql-sqlite3 >= 4.6
Obsoletes:	mixxx-translations
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixxx is an open source DJ tool designed for both professional and
amateur DJs alike.

%description -l hu.UTF-8
Mixxx egy nyílt forrású DJ eszköz profi és amatőr DJ-knek egyaránt.

%description -l pl.UTF-8
Mixxx to mające otwarte źródła narzędzie dla DJ-ów zaprojektowane
zarówno dla profesjonalistów jak i amatorów.

%package skins-core
Summary:	The core skins for Mixxx
Summary(hu.UTF-8):	Alap skinek a Mixxx-hez
Summary(pl.UTF-8):	Podstawowe skórki dla programu Mixxx
Group:		X11/Applications/Multimedia

%description skins-core
The core skins for Mixxx.

%description skins-core -l hu.UTF-8
Alap skinek a Mixxx-hez.

%description skins-core -l pl.UTF-8
Podstawowe skórki dla programu Mixxx.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
%scons \
	libdir=%{_libdir} \
	faad=1 \
	wv=1
# ffmpeg=1 is "NOT-WORKING"
# ipod=1: src/wipodtracksmodel.cpp is missing
# ladspa=1 doesn't build

%install
rm -rf $RPM_BUILD_ROOT
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
%scons install \
	install_root=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mixxx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Mixxx-Manual.pdf
%attr(755,root,root) %{_bindir}/mixxx
%dir %{_libdir}/mixxx
%dir %{_libdir}/mixxx/plugins
%dir %{_libdir}/mixxx/plugins/soundsource
%attr(755,root,root) %{_libdir}/mixxx/plugins/soundsource/libsoundsourcem4a.so
%attr(755,root,root) %{_libdir}/mixxx/plugins/soundsource/libsoundsourcewv.so
%dir %{_libdir}/mixxx/plugins/vamp
%attr(755,root,root) %{_libdir}/mixxx/plugins/vamp/libmixxxminimal.so
%dir %{_datadir}/mixxx
%dir %{_datadir}/mixxx/skins
%dir %{_datadir}/mixxx/translations
%lang(ar) %{_datadir}/mixxx/translations/mixxx_ar.qm
%lang(ast) %{_datadir}/mixxx/translations/mixxx_ast.qm
%lang(bg) %{_datadir}/mixxx/translations/mixxx_bg.qm
%lang(br) %{_datadir}/mixxx/translations/mixxx_br.qm
%lang(bs) %{_datadir}/mixxx/translations/mixxx_bs.qm
%lang(ca) %{_datadir}/mixxx/translations/mixxx_ca.qm
%lang(ceb) %{_datadir}/mixxx/translations/mixxx_ceb.qm
%lang(cs) %{_datadir}/mixxx/translations/mixxx_cs.qm
%lang(da) %{_datadir}/mixxx/translations/mixxx_da.qm
%lang(de) %{_datadir}/mixxx/translations/mixxx_de.qm
%lang(el) %{_datadir}/mixxx/translations/mixxx_el.qm
%lang(en) %{_datadir}/mixxx/translations/mixxx_en_GB.qm
%lang(eo) %{_datadir}/mixxx/translations/mixxx_eo.qm
%lang(es) %{_datadir}/mixxx/translations/mixxx_es.qm
%lang(et) %{_datadir}/mixxx/translations/mixxx_et.qm
%lang(eu) %{_datadir}/mixxx/translations/mixxx_eu.qm
%lang(fi) %{_datadir}/mixxx/translations/mixxx_fi.qm
%lang(fr) %{_datadir}/mixxx/translations/mixxx_fr.qm
%lang(ga) %{_datadir}/mixxx/translations/mixxx_ga.qm
%lang(gl) %{_datadir}/mixxx/translations/mixxx_gl.qm
%lang(he) %{_datadir}/mixxx/translations/mixxx_he.qm
%lang(hr) %{_datadir}/mixxx/translations/mixxx_hr.qm
%lang(hu) %{_datadir}/mixxx/translations/mixxx_hu.qm
%lang(hy) %{_datadir}/mixxx/translations/mixxx_hy.qm
%lang(ia) %{_datadir}/mixxx/translations/mixxx_ia.qm
%lang(id) %{_datadir}/mixxx/translations/mixxx_id.qm
%lang(is) %{_datadir}/mixxx/translations/mixxx_is.qm
%lang(it) %{_datadir}/mixxx/translations/mixxx_it.qm
%lang(ja) %{_datadir}/mixxx/translations/mixxx_ja.qm
%lang(ky) %{_datadir}/mixxx/translations/mixxx_ky.qm
%lang(lb) %{_datadir}/mixxx/translations/mixxx_lb.qm
%lang(lt) %{_datadir}/mixxx/translations/mixxx_lt.qm
%lang(lv) %{_datadir}/mixxx/translations/mixxx_lv.qm
%lang(mk) %{_datadir}/mixxx/translations/mixxx_mk.qm
%lang(ml) %{_datadir}/mixxx/translations/mixxx_ml.qm
%lang(mn) %{_datadir}/mixxx/translations/mixxx_mn.qm
%lang(mr) %{_datadir}/mixxx/translations/mixxx_mr.qm
%lang(ms) %{_datadir}/mixxx/translations/mixxx_ms.qm
%lang(my) %{_datadir}/mixxx/translations/mixxx_my.qm
%lang(nb) %{_datadir}/mixxx/translations/mixxx_nb.qm
%lang(nl) %{_datadir}/mixxx/translations/mixxx_nl.qm
%lang(nn) %{_datadir}/mixxx/translations/mixxx_nn.qm
%lang(oc) %{_datadir}/mixxx/translations/mixxx_oc.qm
%lang(pl) %{_datadir}/mixxx/translations/mixxx_pl.qm
%lang(pt) %{_datadir}/mixxx/translations/mixxx_pt.qm
%lang(pt_BR) %{_datadir}/mixxx/translations/mixxx_pt_BR.qm
%lang(ro) %{_datadir}/mixxx/translations/mixxx_ro.qm
%lang(ru) %{_datadir}/mixxx/translations/mixxx_ru.qm
%lang(sl) %{_datadir}/mixxx/translations/mixxx_sl.qm
%lang(sr) %{_datadir}/mixxx/translations/mixxx_sr.qm
%lang(sv) %{_datadir}/mixxx/translations/mixxx_sv.qm
%lang(te) %{_datadir}/mixxx/translations/mixxx_te.qm
%lang(tr) %{_datadir}/mixxx/translations/mixxx_tr.qm
%lang(uk) %{_datadir}/mixxx/translations/mixxx_uk.qm
%lang(uz) %{_datadir}/mixxx/translations/mixxx_uz.qm
%lang(zh_CN) %{_datadir}/mixxx/translations/mixxx_zh_CN.qm
%lang(zh_TW) %{_datadir}/mixxx/translations/mixxx_zh_TW.qm
%{_datadir}/mixxx/skins/cross.png
# This is the default skin
%{_datadir}/mixxx/skins/Outline1024x600-Netbook
%{_datadir}/mixxx/schema.xml
%{_datadir}/mixxx/controllers
%{_datadir}/mixxx/keyboard
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}-icon.png

%files skins-core
%defattr(644,root,root,755)
%{_datadir}/mixxx/skins/Deere*x*-*
%{_datadir}/mixxx/skins/LateNight*x*-*
%{_datadir}/mixxx/skins/Outline1024x768-XGA
%{_datadir}/mixxx/skins/Outline800x480-WVGA
%{_datadir}/mixxx/skins/Phoney*x*-*
%{_datadir}/mixxx/skins/Shade*x*-*
