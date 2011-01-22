Summary:	Mixxx - DJ tool
Summary(hu.UTF-8):	Mixxx - DJ program
Summary(pl.UTF-8):	Mixxx - narzędzie dla DJ-ów
Name:		mixxx
Version:	1.8.2
Release:	3
License:	GPL/GPL v2+
Group:		X11/Applications
Source0:	http://downloads.mixxx.org/mixxx-%{version}/%{name}-%{version}-src.tar.gz
# Source0-md5:	f0297f4493d4d8e6ad59f72970bad7bc
URL:		http://mixxx.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	Qt3Support-devel
BuildRequires:	audiofile-devel
BuildRequires:	fftw-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	portaudio-devel
BuildRequires:	scons
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

%prep
%setup -q

%build
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
scons \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
export CXXFLAGS="%{rpmcxxflags}"
export CCFLAGS="%{rpmcflags}"
export CXX="%{__cxx}"
export QMAKE_CXX="%{__cxx}"
scons prefix=%{_prefix} install_root=$RPM_BUILD_ROOT install

# I don't know why doesn't use 'prefix' option...
install -d $RPM_BUILD_ROOT%{_prefix}
mv $RPM_BUILD_ROOT/{bin,share} $RPM_BUILD_ROOT%{_prefix}

rm -rf $RPM_BUILD_ROOT%{_docdir}/mixxx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Mixxx-Manual.pdf
%attr(755,root,root) %{_bindir}/mixxx
%dir %{_datadir}/mixxx
%{_datadir}/mixxx/schema.xml
%{_datadir}/mixxx/skins
%{_datadir}/mixxx/keyboard
%{_datadir}/mixxx/midi
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}-icon.png
