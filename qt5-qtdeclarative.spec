# TODO: QtQml / QtQuick split?

# Conditional build:
%bcond_without	qch	# documentation in QCH format

%define		orgname		qtdeclarative
%define		qtbase_ver	%{version}
%define		qttools_ver	%{version}
Summary:	The Qt5 Declarative libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Declarative
Name:		qt5-%{orgname}
Version:	5.2.1
Release:	0.1
License:	LGPL v2.1 or GPL v3.0
Group:		X11/Libraries
Source0:	http://download.qt-project.org/official_releases/qt/5.2/%{version}/submodules/%{orgname}-opensource-src-%{version}.tar.xz
# Source0-md5:	a23fba03a4b48f36fe8b51d326d08acc
URL:		http://qt-project.org/
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Sql-devel >= %{qtbase_ver}
BuildRequires:	Qt5Test-devel >= %{qtbase_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
%if %{with qch}
BuildRequires:	qt5-assistant >= %{qttools_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing
%define		qt5dir		%{_libdir}/qt5

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains Qt5 Declarative libraries.

%description -l pl.UTF-8
Qt to wieloplatformowy szkielet aplikacji i interfejsów użytkownika.
Przy użyciu Qt można pisać aplikacje powiązane z WWW i wdrażać je w
systemach biurkowych, przenośnych i wbudowanych bez przepisywania kodu
źródłowego.

Ten pakiet zawiera biblioteki Qt5 Declarative.

%package devel
Summary:	The Qt5 Declarative application framework - development files
Summary(pl.UTF-8):	Szkielet aplikacji Qt5 Declarative - pliki programistyczne
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The Qt5 Declarative application framework - development files.

%description devel -l pl.UTF-8
Szkielet aplikacji Qt5 Declarative - pliki programistyczne.

%package doc
Summary:	Qt5 Declarative documentation
Summary(pl.UTF-8):	Dokumentacja do biblioteki Qt5 Declarative
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
Qt5 Declarative documentation.

%description doc -l pl.UTF-8
Dokumentacja do biblioteki Qt5 Declarative

%package examples
Summary:	Qt5 Declarative examples
Summary(pl.UTF-8):	Przykłady do biblioteki Qt5 Declarative
Group:		X11/Development/Libraries
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description examples
Qt5 Declarative examples.

%description examples -l pl.UTF-8
Przykłady do biblioteki Qt5 Declarative.

%prep
%setup -q -n %{orgname}-opensource-src-%{version}

%build
qmake-qt5
%{__make}
%{__make} %{!?with_qch:html_}docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__make} install_%{!?with_qch:html_}docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.?
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# symlinks in system bin dir
for f in qml qmlbundle qmlimportscanner qmlmin qmlplugindump qmlprofiler qmlscene qmltestrunner ; do
	ln -sf ../%{_lib}/qt5/bin/$f $RPM_BUILD_ROOT%{_bindir}/${f}-qt5
done

# Prepare some files list
ifecho() {
	r="$RPM_BUILD_ROOT$2"
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
ifecho_tree() {
	ifecho $1 $2
	for f in `find $RPM_BUILD_ROOT$2 -printf "%%P "`; do
		ifecho $1 $2/$f
	done
}

echo "%defattr(644,root,root,755)" > examples.files
ifecho_tree examples %{_examplesdir}/qt5/qml
ifecho_tree examples %{_examplesdir}/qt5/qmltest
ifecho_tree examples %{_examplesdir}/qt5/quick

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_bindir}/qml-qt5
%attr(755,root,root) %{_bindir}/qmlbundle-qt5
%attr(755,root,root) %{_bindir}/qmlimportscanner-qt5
%attr(755,root,root) %{_bindir}/qmlmin-qt5
%attr(755,root,root) %{_bindir}/qmlplugindump-qt5
%attr(755,root,root) %{_bindir}/qmlprofiler-qt5
%attr(755,root,root) %{_bindir}/qmlscene-qt5
%attr(755,root,root) %{_bindir}/qmltestrunner-qt5
%attr(755,root,root) %{_libdir}/libQt5Qml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Qml.so.5
%attr(755,root,root) %{_libdir}/libQt5Quick.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Quick.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickParticles.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickTest.so.5
%attr(755,root,root) %{qt5dir}/bin/qml
%attr(755,root,root) %{qt5dir}/bin/qmlbundle
%attr(755,root,root) %{qt5dir}/bin/qmlimportscanner
%attr(755,root,root) %{qt5dir}/bin/qmlmin
%attr(755,root,root) %{qt5dir}/bin/qmlplugindump
%attr(755,root,root) %{qt5dir}/bin/qmlprofiler
%attr(755,root,root) %{qt5dir}/bin/qmlscene
%attr(755,root,root) %{qt5dir}/bin/qmltestrunner
%dir %{qt5dir}/plugins/accessible
%attr(755,root,root) %{qt5dir}/plugins/accessible/libqtaccessiblequick.so
%dir %{qt5dir}/plugins/qmltooling
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_qtquick2.so
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_tcp.so
%dir %{qt5dir}/qml
%dir %{qt5dir}/qml/Qt
%dir %{qt5dir}/qml/Qt/labs
%dir %{qt5dir}/qml/Qt/labs/folderlistmodel
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.so
%{qt5dir}/qml/Qt/labs/folderlistmodel/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/folderlistmodel/qmldir
%dir %{qt5dir}/qml/Qt/labs/settings
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/settings/libqmlsettingsplugin.so
%{qt5dir}/qml/Qt/labs/settings/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/settings/qmldir
%dir %{qt5dir}/qml/QtQml
%dir %{qt5dir}/qml/QtQml/Models.2
%attr(755,root,root) %{qt5dir}/qml/QtQml/Models.2/libmodelsplugin.so
%{qt5dir}/qml/QtQml/Models.2/qmldir
%dir %{qt5dir}/qml/QtQuick
%dir %{qt5dir}/qml/QtQuick/Dialogs
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Dialogs/libdialogplugin.so
%{qt5dir}/qml/QtQuick/Dialogs/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Dialogs/qmldir
%dir %{qt5dir}/qml/QtQuick/Dialogs/Private
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Dialogs/Private/libdialogsprivateplugin.so
%{qt5dir}/qml/QtQuick/Dialogs/Private/qmldir
%dir %{qt5dir}/qml/QtQuick/LocalStorage
%attr(755,root,root) %{qt5dir}/qml/QtQuick/LocalStorage/libqmllocalstorageplugin.so
%{qt5dir}/qml/QtQuick/LocalStorage/plugins.qmltypes
%{qt5dir}/qml/QtQuick/LocalStorage/qmldir
%dir %{qt5dir}/qml/QtQuick/Particles.2
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Particles.2/libparticlesplugin.so
%{qt5dir}/qml/QtQuick/Particles.2/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Particles.2/qmldir
%dir %{qt5dir}/qml/QtQuick/PrivateWidgets
%attr(755,root,root) %{qt5dir}/qml/QtQuick/PrivateWidgets/libwidgetsplugin.so
%{qt5dir}/qml/QtQuick/PrivateWidgets/plugins.qmltypes
%{qt5dir}/qml/QtQuick/PrivateWidgets/qmldir
%dir %{qt5dir}/qml/QtQuick/Window.2
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Window.2/libwindowplugin.so
%{qt5dir}/qml/QtQuick/Window.2/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Window.2/qmldir
%dir %{qt5dir}/qml/QtQuick.2
%attr(755,root,root) %{qt5dir}/qml/QtQuick.2/libqtquick2plugin.so
%{qt5dir}/qml/QtQuick.2/plugins.qmltypes
%{qt5dir}/qml/QtQuick.2/qmldir
%dir %{qt5dir}/qml/QtTest
%attr(755,root,root) %{qt5dir}/qml/QtTest/libqmltestplugin.so
%{qt5dir}/qml/QtTest/plugins.qmltypes
%{qt5dir}/qml/QtTest/qmldir
%{qt5dir}/qml/QtTest/testlogger.js
%{qt5dir}/qml/QtTest/*.qml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Qml.so
%attr(755,root,root) %{_libdir}/libQt5Quick.so
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so
%{_libdir}/libQt5QmlDevTools.a

%{_libdir}/libQt5Qml.prl
%{_libdir}/libQt5Quick.prl
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/libQt5QmlDevTools.prl

%{_libdir}/cmake/Qt5Qml
%{_libdir}/cmake/Qt5Quick
%{_libdir}/cmake/Qt5QuickTest
%{_libdir}/cmake/Qt5Widgets/Qt5Widgets_AccessibleQuickFactory.cmake

%{_includedir}/qt5/QtQml
%{_includedir}/qt5/QtQuick
%{_includedir}/qt5/QtQuickParticles
%{_includedir}/qt5/QtQuickTest

%{_pkgconfigdir}/Qt5Qml.pc
%{_pkgconfigdir}/Qt5QmlDevTools.pc
%{_pkgconfigdir}/Qt5Quick.pc
%{_pkgconfigdir}/Qt5QuickParticles.pc
%{_pkgconfigdir}/Qt5QuickTest.pc

%{qt5dir}/mkspecs/modules/qt_lib_qml.pri
%{qt5dir}/mkspecs/modules/qt_lib_qml_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmldevtools_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmltest.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmltest_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_quick.pri
%{qt5dir}/mkspecs/modules/qt_lib_quick_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_quickparticles_private.pri

%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtqml
%{_docdir}/qt5-doc/qtquick
%{_docdir}/qt5-doc/qtquickdialogs

%if %{with qch}
#%files doc-qch
%{_docdir}/qt5-doc/qtqml.qch
%{_docdir}/qt5-doc/qtquick.qch
%{_docdir}/qt5-doc/qtquickdialogs.qch
%endif

%files examples -f examples.files
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
