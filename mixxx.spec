Summary:	Mixxx - DJ tool
Summary(hu.UTF-8):	Mixxx - DJ program
Summary(pl.UTF-8):	Mixxx - narzędzie dla DJ-ów
Name:		mixxx
Version:	1.10.0
Release:	1
License:	GPL/GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://downloads.mixxx.org/mixxx-%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	d92bf422491fa92adf7ed6c2998e67fb
Patch0:		desktop.patch
URL:		http://mixxx.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt3Support-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	audiofile-devel
BuildRequires:	fftw-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	portmidi-devel >= 217
BuildRequires:	qt4-build
BuildRequires:	qt4-linguist
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	scons
BuildRequires:	sed >= 4.0
Requires:	QtSql-sqlite3
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
Group:		X11/Applications/Multimedia

%description skins-core
The core skins for Mixxx.

%description skins-core -l hu.UTF-8
Alap skinek a Mixxx-hez.

%package translations
Summary:	Translations for Mixxx
Summary(hu.UTF-8):	Nyelvi fájlok a Mixxx-hez
Group:		X11/Applications/Multimedia

%description translations
Translations for Mixxx.

%description translations -l hu.UTF-8
Nyelvi fájlok a Mixxx-hez.

%prep
%setup -q
%patch0 -p1

%build
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
%scons

%install
rm -rf $RPM_BUILD_ROOT
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
%scons install install_root=$RPM_BUILD_ROOT install

# I don't know why doesn't use 'prefix' option...
install -d $RPM_BUILD_ROOT%{_prefix}
mv $RPM_BUILD_ROOT/{bin,share} $RPM_BUILD_ROOT%{_prefix}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mixxx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Mixxx-Manual.pdf
%attr(755,root,root) %{_bindir}/mixxx
%dir %{_datadir}/mixxx
%dir %{_datadir}/mixxx/skins
%dir %{_datadir}/mixxx/translations
%{_datadir}/mixxx/skins/cross.*
%doc %{_datadir}/mixxx/skins/*.xsl
# This is the default skin
%{_datadir}/mixxx/skins/Outline1024x600-Netbook
# %{_datadir}/mixxx/skins/outlineNetbook
%{_datadir}/mixxx/schema.xml
%{_datadir}/mixxx/keyboard
%{_datadir}/mixxx/midi
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}-icon.png

%files translations
%defattr(644,root,root,755)
%{_datadir}/mixxx/translations/*

%files skins-core
%defattr(644,root,root,755)
%{_datadir}/mixxx/skins/*
