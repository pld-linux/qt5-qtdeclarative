# TODO:
# - cleanup

%define		orgname		qtdeclarative
Summary:	The Qt5 Declarative
Name:		qt5-%{orgname}
Version:	5.2.0
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	0f7714c5c91b8eb7cdc1071f0a51c202
URL:		http://qt-project.org/
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	qt5-qttools-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_noautostrip	'.*_debug\\.so*'

%define		specflags	-fno-strict-aliasing
%define		_qtdir		%{_libdir}/qt5

%description
Qt5 declarative libraries.

%package devel
Summary:	The Qt5 Declarative application framework - development files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Qt5 Declarative - development files.

%package doc
Summary:	The Qt5 Declarative - docs
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Declarative - documentation.

%package examples
Summary:	Qt5 Declarative examples
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Declarative - examples.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# Prepare some files list
ifecho() {
	RESULT=`echo $RPM_BUILD_ROOT$2 2>/dev/null`
	[ "$RESULT" == "" ] && return # XXX this is never true due $RPM_BUILD_ROOT being set
	r=`echo $RESULT | awk '{ print $1 }'`

	if [ -d "$r" ]; then
		echo "%%dir $2" >> $1.files
	elif [ -x "$r" ] ; then
		echo "%%attr(755,root,root) $2" >> $1.files
	elif [ -f "$r" ]; then
		echo "$2" >> $1.files
	else
		echo "Error generation $1 files list!"
		echo "$r: no such file or directory!"
		return 1
	fi
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho examples %{_examplesdir}/qt5
for f in `find $RPM_BUILD_ROOT%{_examplesdir}/qt5 -printf "%%P "`; do
	ifecho examples %{_examplesdir}/qt5/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%post		-p /sbin/ldconfig
%postun		-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/libQt5Qml.so.?
%attr(755,root,root) %{_libdir}/libQt5Qml.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Quick.so.?
%attr(755,root,root) %{_libdir}/libQt5Quick.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickParticles.so.?
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickTest.so.?
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so.*.*
%{_libdir}/libQt5QmlDevTools.a
%attr(755,root,root) %{_qtdir}/bin/qml*
%attr(755,root,root) %{_qtdir}/plugins
%attr(755,root,root) %{_qtdir}/qml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Qml.so
%attr(755,root,root) %{_libdir}/libQt5Quick.so
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so
%{_libdir}/libQt5Qml.la
%{_libdir}/libQt5Quick.la
%{_libdir}/libQt5QuickParticles.la
%{_libdir}/libQt5QuickTest.la
%{_libdir}/libQt5QmlDevTools.la

%{_libdir}/libQt5Qml.prl
%{_libdir}/libQt5Quick.prl
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/libQt5QmlDevTools.prl

%{_libdir}/cmake/Qt5Qml
%{_libdir}/cmake/Qt5Quick
%{_libdir}/cmake/Qt5QuickTest

%{_includedir}/qt5/QtQml
%{_includedir}/qt5/QtQuick
%{_includedir}/qt5/QtQuickParticles
%{_includedir}/qt5/QtQuickTest

%{_pkgconfigdir}/*.pc

%{_qtdir}/mkspecs

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc

%files examples -f examples.files
