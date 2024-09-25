# TODO: system djinterop >= 0.20.2, shoutidjc >= 2.4.6?
#
# Conditional build:
%bcond_without	faad		# FAAD AAC audio decoder
%bcond_without	ffmpeg		# FFmpeg support
%bcond_without	hidapi		# HID controller support
%bcond_without	lv2		# LV2 support
%bcond_without	qtkeychain	# secure credentials storage for Live Broadcasting profiles (qt5 only, see below)
%bcond_with	taglib2		# allow Taglib 2 (not fully supported)
%bcond_without	upower		# UPower battery state support
%bcond_without	wavpack		# WavPack audio decoder

%define		qt5_ver		5.12

Summary:	Mixxx - DJ tool
Summary(hu.UTF-8):	Mixxx - DJ program
Summary(pl.UTF-8):	Mixxx - narzędzie dla DJ-ów
Name:		mixxx
Version:	2.4.1
Release:	1
License:	GPL v2+ (code), Apache v2.0 (OpenSans font), Ubuntu Font License v1.0 (Ubuntu fonts)
Group:		X11/Applications/Multimedia
Source0:	https://github.com/mixxxdj/mixxx/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	95d2cc0cb35b88164615a75d9466bc0f
Patch0:		%{name}-build-type.patch
Patch1:		%{name}-taglib2.patch
Patch2:		%{name}-msgsl.patch
URL:		https://mixxx.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Concurrent-devel >= %{qt5_ver}
BuildRequires:	Qt5Core-devel >= %{qt5_ver}
BuildRequires:	Qt5DBus-devel >= %{qt5_ver}
BuildRequires:	Qt5Gui-devel >= %{qt5_ver}
%{?with_qtkeychain:BuildRequires:	Qt5Keychain-devel}
BuildRequires:	Qt5Network-devel >= %{qt5_ver}
BuildRequires:	Qt5OpenGL-devel >= %{qt5_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt5_ver}
BuildRequires:	Qt5Qml-devel >= %{qt5_ver}
BuildRequires:	Qt5Script-devel >= %{qt5_ver}
BuildRequires:	Qt5ScriptTools-devel >= %{qt5_ver}
BuildRequires:	Qt5Sql-devel >= %{qt5_ver}
BuildRequires:	Qt5Svg-devel >= %{qt5_ver}
BuildRequires:	Qt5Test-devel >= %{qt5_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt5_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt5_ver}
BuildRequires:	Qt5Xml-devel >= %{qt5_ver}
BuildRequires:	cmake >= 3.16
# libavcodec >= 58.35.100 libavformat >= 58.20.100 libavutil >= 56.22.100 libswresample >= 3.3.100
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel >= 4.1.9}
BuildRequires:	flac-devel
%{?with_upower:BuildRequires:	glib2-devel >= 2.0}
BuildRequires:	gtest-devel
%{?with_hidapi:BuildRequires:	hidapi-devel >= 0.11.2}
BuildRequires:	lame-libs-devel
BuildRequires:	libchromaprint-devel
BuildRequires:	libebur128-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libogg-devel
BuildRequires:	libkeyfinder-devel >= 2.2.8
# TODO: use system package when appropriate version gets released
#BuildRequires:	libshout-idjc-devel >= 2.4.6
BuildRequires:	libsndfile-devel
# -std=c++20
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	libvorbis-devel
%{?with_lv2:BuildRequires:	lilv-devel >= 0.5}
BuildRequires:	microsoft-gsl-devel
# or mpeg4ip (libmp4), but mp4v2 is preferred
%{?with_faad:BuildRequires:	mp4v2-devel}
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	opus-devel >= 1.0
BuildRequires:	opusfile-devel >= 0.2
BuildRequires:	portaudio-devel >= 19
BuildRequires:	portmidi-devel >= 217
BuildRequires:	protobuf-devel
BuildRequires:	python3 >= 1:3
BuildRequires:	rubberband-devel
BuildRequires:	qt5-build >= %{qt5_ver}
BuildRequires:	qt5-linguist >= %{qt5_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRequires:	soundtouch-devel >= 2.1.2
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	taglib-devel >= 1.11
%{!?with_taglib2:BuildRequires:	taglib-devel < 2}
BuildRequires:	udev-devel
%{?with_upower:BuildRequires:	upower-devel}
%{?with_wavpack:BuildRequires:	wavpack-devel}
BuildRequires:	xorg-lib-libX11-devel
# for local djinterop
BuildRequires:	zlib-devel >= 1.2.8
Requires:	Qt5Sql-sqldriver-sqlite3 >= %{qt5_ver}
%{?with_ffmpeg:Requires:	ffmpeg-libs >= 4.1.9}
%{?with_hidapi:Requires:	hidapi >= 0.11.2}
Requires:	libkeyfinder >= 2.2.8
Requires:	soundtouch >= 2.1.2
Requires:	taglib >= 1.11
Requires:	zlib >= 1.2.8
Obsoletes:	mixxx-translations < 1.11.0-5
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
%{?with_taglib2:%patch1 -p1}
%patch2 -p1

%build
%cmake -B build \
	-DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON \
	%{!?with_upower:-DBATTERY=OFF} \
	%{!?with_faad:-DFAAD=OFF} \
	%{!?with_ffmpeg:-DFFMPEG=OFF} \
	%{!?with_hidapi:-DHID=OFF} \
	%{!?with_lv2:-DLILV=OFF} \
	-DOPTIMIZE=off \
	%{!?with_qtkeychain:-DQTKEYCHAIN=OFF} \
	%{!?with_wavpack:-DWAVPACK=OFF}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/{COPYING,LICENSE,Mixxx-Keyboard-Shortcuts.pdf,README.md}
# not used on Linux
%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/mixxx_macos.svg

# both es and es_ES exist, the first is more outdated
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{es_ES,es}.qm
# both pt and pt_PT exist, the first is more outdated
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{pt_PT,pt}.qm
# unify using short code
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{hi_IN,hi}.qm
%{__mv} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_{sq_AL,sq}.qm
# stick to per-country files
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_es_419.qm
# which variant? zh_CN,zh_HK,zh_TW are also present
%{__rm} $RPM_BUILD_ROOT%{_datadir}/mixxx/translations/mixxx_zh.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md COPYING README.md res/Mixxx-Keyboard-Shortcuts.pdf res/fonts/Ubuntu.LICENCE.txt
%attr(755,root,root) %{_bindir}/mixxx
/lib/udev/rules.d/69-mixxx-usb-uaccess.rules
%{_datadir}/metainfo/org.mixxx.Mixxx.metainfo.xml
%dir %{_datadir}/mixxx
%{_datadir}/mixxx/controllers
%{_datadir}/mixxx/effects
%{_datadir}/mixxx/keyboard
%dir %{_datadir}/mixxx/skins
%{_datadir}/mixxx/skins/*.qss
# This is the default skin
%{_datadir}/mixxx/skins/Deere
%dir %{_datadir}/mixxx/translations
%lang(ar) %{_datadir}/mixxx/translations/mixxx_ar.qm
%lang(ast) %{_datadir}/mixxx/translations/mixxx_ast.qm
%lang(bg) %{_datadir}/mixxx/translations/mixxx_bg.qm
%lang(br) %{_datadir}/mixxx/translations/mixxx_br.qm
%lang(bs) %{_datadir}/mixxx/translations/mixxx_bs.qm
%lang(ca) %{_datadir}/mixxx/translations/mixxx_ca.qm
%lang(cs) %{_datadir}/mixxx/translations/mixxx_cs.qm
%lang(da) %{_datadir}/mixxx/translations/mixxx_da.qm
%lang(de) %{_datadir}/mixxx/translations/mixxx_de.qm
%lang(el) %{_datadir}/mixxx/translations/mixxx_el.qm
%lang(en_CA) %{_datadir}/mixxx/translations/mixxx_en_CA.qm
%lang(en_GB) %{_datadir}/mixxx/translations/mixxx_en_GB.qm
%lang(eo) %{_datadir}/mixxx/translations/mixxx_eo.qm
%lang(es) %{_datadir}/mixxx/translations/mixxx_es.qm
%lang(es_AR) %{_datadir}/mixxx/translations/mixxx_es_AR.qm
%lang(es_CO) %{_datadir}/mixxx/translations/mixxx_es_CO.qm
%lang(es_CR) %{_datadir}/mixxx/translations/mixxx_es_CR.qm
%lang(es_EC) %{_datadir}/mixxx/translations/mixxx_es_EC.qm
%lang(es_MX) %{_datadir}/mixxx/translations/mixxx_es_MX.qm
%lang(es_PA) %{_datadir}/mixxx/translations/mixxx_es_PA.qm
%lang(es_UY) %{_datadir}/mixxx/translations/mixxx_es_UY.qm
%lang(et) %{_datadir}/mixxx/translations/mixxx_et.qm
%lang(eu) %{_datadir}/mixxx/translations/mixxx_eu.qm
%lang(fa) %{_datadir}/mixxx/translations/mixxx_fa.qm
%lang(fi) %{_datadir}/mixxx/translations/mixxx_fi.qm
%lang(fr) %{_datadir}/mixxx/translations/mixxx_fr.qm
%lang(ga) %{_datadir}/mixxx/translations/mixxx_ga.qm
%lang(gl) %{_datadir}/mixxx/translations/mixxx_gl.qm
%lang(he) %{_datadir}/mixxx/translations/mixxx_he.qm
%lang(hi) %{_datadir}/mixxx/translations/mixxx_hi.qm
%lang(hr) %{_datadir}/mixxx/translations/mixxx_hr.qm
%lang(hu) %{_datadir}/mixxx/translations/mixxx_hu.qm
%lang(hy) %{_datadir}/mixxx/translations/mixxx_hy.qm
%lang(id) %{_datadir}/mixxx/translations/mixxx_id.qm
%lang(is) %{_datadir}/mixxx/translations/mixxx_is.qm
%lang(it) %{_datadir}/mixxx/translations/mixxx_it.qm
%lang(ja) %{_datadir}/mixxx/translations/mixxx_ja.qm
%lang(ko) %{_datadir}/mixxx/translations/mixxx_ko.qm
%lang(lb) %{_datadir}/mixxx/translations/mixxx_lb.qm
%lang(lt) %{_datadir}/mixxx/translations/mixxx_lt.qm
%lang(lv) %{_datadir}/mixxx/translations/mixxx_lv.qm
%lang(mi) %{_datadir}/mixxx/translations/mixxx_mi.qm
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
%lang(te) %{_datadir}/mixxx/translations/mixxx_te.qm
%lang(tr) %{_datadir}/mixxx/translations/mixxx_tr.qm
%lang(uk) %{_datadir}/mixxx/translations/mixxx_uk.qm
%lang(uz) %{_datadir}/mixxx/translations/mixxx_uz.qm
%lang(vi) %{_datadir}/mixxx/translations/mixxx_vi.qm
%lang(zh_CN) %{_datadir}/mixxx/translations/mixxx_zh_CN.qm
%lang(zh_HK) %{_datadir}/mixxx/translations/mixxx_zh_HK.qm
%lang(zh_TW) %{_datadir}/mixxx/translations/mixxx_zh_TW.qm
%{_desktopdir}/org.mixxx.Mixxx.desktop
%{_iconsdir}/hicolor/*x*/apps/mixxx.png
%{_iconsdir}/hicolor/scalable/apps/mixxx.svg

%files skins-core
%defattr(644,root,root,755)
# note: "?" is used to catch spaces (I can't see any way to match space explicitly in rpm)
%{_datadir}/mixxx/skins/Deere?(64?Samplers)
%{_datadir}/mixxx/skins/LateNight
%{_datadir}/mixxx/skins/LateNight?(64?Samplers)
%{_datadir}/mixxx/skins/Shade
%{_datadir}/mixxx/skins/Tango
%{_datadir}/mixxx/skins/Tango?(64?Samplers)
