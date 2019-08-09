#
# Conditional build:
%bcond_without	faad		# FAAD AAC audio decoder
%bcond_without	ffmpeg		# FFmpeg support
%bcond_without	hidapi		# HID controller support
%bcond_with	ipod		# iPod support via libgpod [NOT-WORKING, src/wipodtracksmodel.cpp is missing]
%bcond_without	lv2		# LV2 support
%bcond_with	qt4		# Qt 4 instead of Qt 5
%bcond_without	qtkeychain	# secure credentials storage for Live Broadcasting profiles (qt5 only, see below)
%bcond_without	upower		# UPower battery state support
%bcond_without	wavpack		# WavPack audio decoder

%define		qt4_ver		4.6
%define		qt5_ver		5.0

%if %{with qt4}
# as of 2.2.1, qt5keychain is always checked, see build/depends.py
%undefine	with_qtkeychain
%endif
Summary:	Mixxx - DJ tool
Summary(hu.UTF-8):	Mixxx - DJ program
Summary(pl.UTF-8):	Mixxx - narzędzie dla DJ-ów
Name:		mixxx
Version:	2.2.1
Release:	2
License:	GPL v2+ (code), Apache v2.0 (OpenSans font), Ubuntu Font License v1.0 (Ubuntu fonts)
Group:		X11/Applications/Multimedia
Source0:	https://github.com/mixxxdj/mixxx/archive/release-%{version}/%{name}-release-%{version}.tar.gz
# Source0-md5:	ef72d4b594f9f3dbafd1e264be89fbdc
Patch0:		%{name}-vamp.patch
URL:		https://mixxx.org/
BuildRequires:	OpenGL-GLU-devel
%if %{with qt4}
BuildRequires:	QtCore-devel >= %{qt4_ver}
BuildRequires:	QtDBus-devel >= %{qt4_ver}
BuildRequires:	QtGui-devel >= %{qt4_ver}
BuildRequires:	QtNetwork-devel >= %{qt4_ver}
BuildRequires:	QtOpenGL-devel >= %{qt4_ver}
BuildRequires:	QtScript-devel >= %{qt4_ver}
BuildRequires:	QtScriptTools-devel >= %{qt4_ver}
BuildRequires:	QtSql-devel >= %{qt4_ver}
BuildRequires:	QtSvg-devel >= %{qt4_ver}
BuildRequires:	QtTest-devel >= %{qt4_ver}
BuildRequires:	QtXml-devel >= %{qt4_ver}
%else
BuildRequires:	Qt5Concurrent-devel >= %{qt5_ver}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5DBus-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
%{?with_qtkeychain:BuildRequires:	Qt5Keychain-devel}
BuildRequires:	Qt5Network-devel >= %{qt5_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt5_ver}
BuildRequires:	Qt5Script-devel >= %{qt5_ver}
BuildRequires:	Qt5ScriptTools-devel >= %{qt5_ver}
BuildRequires:	Qt5Sql-devel >= %{qt5_ver}
BuildRequires:	Qt5Svg-devel >= %{qt5_ver}
BuildRequires:	Qt5Test-devel >= %{qt5_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt5_ver}
BuildRequires:	Qt5Xml-devel >= %{qt5_ver}
%endif
BuildRequires:	audiofile-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.7}
# libavcodec >= 53.35.0 libavformat >= 53.21.0 libavutil
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel >= 0.11}
BuildRequires:	fftw3-devel >= 3
BuildRequires:	flac-devel
%{?with_ipod:BuildRequires:	glib2-devel >= 2.0}
%{?with_hidapi:BuildRequires:	hidapi-devel >= 0.8.0}
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libchromaprint-devel
BuildRequires:	libebur128-devel
%{?with_ipod:BuildRequires:	libgpod-devel}
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libogg-devel
BuildRequires:	libshout-devel >= 2
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libvorbis-devel
%{?with_lv2:BuildRequires:	lilv-devel >= 0.5}
%{?with_faad:BuildRequires:	mp4v2-devel}
BuildRequires:	opus-devel >= 1.0
BuildRequires:	opusfile-devel >= 0.2
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	portaudio-devel >= 19
BuildRequires:	portmidi-devel >= 217
BuildRequires:	protobuf-devel
%if %{with qt4}
BuildRequires:	qt4-build >= %{qt4_ver}
BuildRequires:	qt4-linguist >= %{qt4_ver}
%else
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-linguist >= %{qt5_ver}
%endif
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	rubberband-devel
BuildRequires:	scons
BuildRequires:	sed >= 4.0
BuildRequires:	soundtouch-devel >= 2.0.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	taglib-devel
%{?with_upower:BuildRequires:	upower-devel}
BuildRequires:	vamp-devel >= 2.7.1
%{?with_wavpack:BuildRequires:	wavpack-devel}
BuildRequires:	xorg-lib-libX11-devel
%if %{with qt4}
Requires:	QtSql-sqlite3 >= %{qt4_ver}
%else
Requires:	Qt5Sql-sqldriver-sqlite3 >= %{qt5_ver}
%endif
%{?with_faad:Requires:	faad2 >= 2.7}
%{?with_hidapi:Requires:	hidapi >= 0.8.0}
Obsoletes:	mixxx-translations
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with qt4}
%define		qtsuf	%{nil}
%else
%define		qtsuf	qt5
%endif

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
%setup -q -n %{name}-release-%{version}
%patch0 -p1

%build
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
export LIBDIR=%{_libdir}
%scons \
	prefix=%{_prefix} \
	%{!?with_upower:battery=0} \
	%{?with_faad:faad=1} \
	%{?with_ffmpeg:ffmpeg=1} \
	%{!?with_hidapi:hid=0} \
	%{?with_ipod:ipod=1} \
	%{?with_lv2:lilv=1} \
	modplug=1 \
	%{?with_qt4:qt5=0} \
	%{?with_qtkeychain:qtkeychain=1} \
	vinylcontrol=1 \
	%{?with_wavpack:wv=1}

%install
rm -rf $RPM_BUILD_ROOT

export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
export LIBDIR=%{_libdir}
%scons install \
	install_root=$RPM_BUILD_ROOT%{_prefix}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mixxx
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/fonts/Ubuntu.LICENCE.txt
# generic Apache v2.0 license
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/fonts/OpenSans.LICENSE.txt

# what a mess...
# both ca and ca-ES exist, both up to date, with few differences... keep ca
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_ca-ES.qm
# en is en_US in fact
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{en,en_US}.qm
# both es and es-ES exist, the first is outdated
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{es-ES,es}.qm
# both fr and fr-FR exist, the latter is outdated
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_fr-FR.qm
# both pt and pt-PT exist, the first is outdated
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{pt-PT,pt}.qm
# both zh_TW and zh_TW.Big5 exist, thr latter is outdated
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_zh_TW.Big5.qm
# unify using short code
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{sq-AL,sq}.qm
# underscore (not dash) should be used as delimiter
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{es-MX,es_MX}.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Mixxx-Manual.pdf res/fonts/Ubuntu.LICENCE.txt
%attr(755,root,root) %{_bindir}/mixxx
%dir %{_libdir}/mixxx
%dir %{_libdir}/mixxx/plugins
%dir %{_libdir}/mixxx/plugins/soundsource%{qtsuf}
%attr(755,root,root) %{_libdir}/mixxx/plugins/soundsource%{qtsuf}/libsoundsourcem4a.so
%attr(755,root,root) %{_libdir}/mixxx/plugins/soundsource%{qtsuf}/libsoundsourcewv.so
%dir %{_libdir}/mixxx/plugins/vamp%{qtsuf}
%attr(755,root,root) %{_libdir}/mixxx/plugins/vamp%{qtsuf}/libmixxxminimal.so
%{_datadir}/appdata/mixxx.appdata.xml
%dir %{_datadir}/mixxx
%{_datadir}/mixxx/controllers
%{_datadir}/mixxx/fonts
%{_datadir}/mixxx/keyboard
%dir %{_datadir}/mixxx/skins
# This is the default skin
%{_datadir}/mixxx/skins/Deere
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
%lang(en) %{_datadir}/mixxx/translations/mixxx_en_US.qm
%lang(eo) %{_datadir}/mixxx/translations/mixxx_eo.qm
%lang(es) %{_datadir}/mixxx/translations/mixxx_es.qm
%lang(es_MX) %{_datadir}/mixxx/translations/mixxx_es_MX.qm
%lang(et) %{_datadir}/mixxx/translations/mixxx_et.qm
%lang(eu) %{_datadir}/mixxx/translations/mixxx_eu.qm
%lang(fa) %{_datadir}/mixxx/translations/mixxx_fa.qm
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
%lang(ko) %{_datadir}/mixxx/translations/mixxx_ko.qm
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
%lang(si) %{_datadir}/mixxx/translations/mixxx_si.qm
%lang(sk) %{_datadir}/mixxx/translations/mixxx_sk.qm
%lang(sl) %{_datadir}/mixxx/translations/mixxx_sl.qm
%lang(sn) %{_datadir}/mixxx/translations/mixxx_sn.qm
%lang(sq) %{_datadir}/mixxx/translations/mixxx_sq.qm
%lang(sr) %{_datadir}/mixxx/translations/mixxx_sr.qm
%lang(sv) %{_datadir}/mixxx/translations/mixxx_sv.qm
%lang(ta) %{_datadir}/mixxx/translations/mixxx_ta.qm
%lang(te) %{_datadir}/mixxx/translations/mixxx_te.qm
%lang(tr) %{_datadir}/mixxx/translations/mixxx_tr.qm
%lang(uk) %{_datadir}/mixxx/translations/mixxx_uk.qm
%lang(uz) %{_datadir}/mixxx/translations/mixxx_uz.qm
%lang(vi) %{_datadir}/mixxx/translations/mixxx_vi.qm
%lang(zh_CN) %{_datadir}/mixxx/translations/mixxx_zh_CN.qm
%lang(zh_TW) %{_datadir}/mixxx/translations/mixxx_zh_TW.qm
%{_desktopdir}/mixxx.desktop
%{_pixmapsdir}/mixxx_icon.svg

%files skins-core
%defattr(644,root,root,755)
# note: "?" is used to catch spaces (I can't see any way to match space explicitly in rpm)
%{_datadir}/mixxx/skins/Deere?(64?Samplers)
%{_datadir}/mixxx/skins/LateNight
%{_datadir}/mixxx/skins/Shade
%{_datadir}/mixxx/skins/Tango
%{_datadir}/mixxx/skins/Tango?(64?Samplers)
