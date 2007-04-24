#
# TODO:
# - desktop file as Source1
#
Summary:	Mixxx - DJ tool
Summary(pl.UTF-8):	Mixxx - narzędzie dla DJ-ów
Name:		mixxx
Version:	1.5.0
Release:	0.1
License:	GPL/GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/mixxx/%{name}-%{version}-src.tar.bz2
# Source0-md5:	64aed846d3973dfb00a3d918ec7be769
URL:		http://mixxx.sourceforge.net/
BuildRequires:	audiofile-devel
BuildRequires:	fftw-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	portaudio-devel
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixxx is an open source DJ tool designed for both professional and
amateur DJs alike.

%description -l pl.UTF-8
Mixxx to mające otwarte źródła narzędzie dla DJ-ów zaprojektowane
zarówno dla profesjonalistów jak i amatorów.

%prep
%setup -q
%{__sed} -i -e s#lib/libqt-mt#/usr/%{_lib}/libqt-mt#g src/build.definition

%build
export QTDIR=%{_prefix}
cd src/
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/skins/{outline,traditional,outlineClose,outlineSmall}}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{midi,keyboard}
# Copy skins
install src/skins/outline/* $RPM_BUILD_ROOT%{_datadir}/mixxx/skins/outline
install src/skins/outlineClose/* $RPM_BUILD_ROOT%{_datadir}/mixxx/skins/outlineClose
install src/skins/outlineSmall/* $RPM_BUILD_ROOT%{_datadir}/mixxx/skins/outlineSmall
install src/skins/traditional/* $RPM_BUILD_ROOT%{_datadir}/mixxx/skins/traditional

# Copy midi config files
install src/midi/* $RPM_BUILD_ROOT%{_datadir}/mixxx/midi

# Copy keyboard config files
install src/keyboard/* $RPM_BUILD_ROOT%{_datadir}/mixxx/keyboard

# Copy mixxx binary
install src/mixxx $RPM_BUILD_ROOT%{_bindir}
#install src/mixxx-with-jack $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Mixxx-Manual.pdf
%attr(755,root,root) %{_bindir}/mixxx
%dir %{_datadir}/mixxx
%{_datadir}/mixxx/skins
%{_datadir}/mixxx/keyboard
%{_datadir}/mixxx/midi
