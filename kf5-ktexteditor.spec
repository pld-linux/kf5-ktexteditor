%define		kdeframever	5.90
%define		qtver		5.9.0
%define		kfname		ktexteditor

Summary:	Full text editor component
Name:		kf5-%{kfname}
Version:	5.90.0
Release:	3
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	46aa278e6d28611efb8fd429cf873565
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5PrintSupport-devel >= %{qtver}
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	Qt5XmlPatterns-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kparts-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	kf5-syntax-highlighting-devel >= %{version}
BuildRequires:	libgit2-devel
BuildRequires:	ninja
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KTextEditor provides a powerful text editor component that you can
embed in your application, either as a KPart or using the
KF5::TextEditor library (if you need more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support,
making it suitable for everything from a simple embedded text-file
editor to an advanced IDE.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

install -d $RPM_BUILD_ROOT%{_datadir}/katepart5/syntax

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKF5TextEditor.so.5
%attr(755,root,root) %{_libdir}/libKF5TextEditor.so.*.*
%ghost %{qt5dir}/plugins/kf5/parts/katepart.so
%dir %{_datadir}/katepart5
%dir %{_datadir}/katepart5/script
%{_datadir}/katepart5/script/README.md
%dir %{_datadir}/katepart5/syntax
%{_datadir}/kservices5/katepart.desktop
%{_datadir}/kservicetypes5/ktexteditor.desktop
%{_datadir}/kservicetypes5/ktexteditorplugin.desktop
%attr(755,root,root) %{_libexecdir}/kauth/kauth_ktexteditor_helper
%{_datadir}/dbus-1/system-services/org.kde.ktexteditor.katetextbuffer.service
%{_datadir}/dbus-1/system.d/org.kde.ktexteditor.katetextbuffer.conf
%{_datadir}/polkit-1/actions/org.kde.ktexteditor.katetextbuffer.policy
%{_datadir}/qlogging-categories5/ktexteditor.categories
%{_datadir}/qlogging-categories5/ktexteditor.renamecategories
%dir %{_datadir}/kdevfiletemplates
%dir %{_datadir}/kdevfiletemplates/templates
%{_datadir}/kdevfiletemplates/templates/ktexteditor-plugin.tar.bz2

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KTextEditor
%{_includedir}/KF5/ktexteditor_version.h
%{_libdir}/cmake/KF5TextEditor
%{_libdir}/libKF5TextEditor.so
%{qt5dir}/mkspecs/modules/qt_KTextEditor.pri
