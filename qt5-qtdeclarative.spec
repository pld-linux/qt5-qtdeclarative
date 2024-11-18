#
# Conditional build:
%bcond_with	bootstrap	# disable features to able to build without installed qt5
# -- build targets
%bcond_without	doc		# Documentation
%bcond_with	jit		# QML just-in-time compiler
%bcond_with	openvg		# OpenVG scenegraph plugin
%bcond_without	qm		# QM translations

%if %{with bootstrap}
%undefine	with_doc
%undefine	with_qm
%endif

# requires sse2 on x86
%ifarch pentium4 %{x8664} aarch64
%define		with_jit	1
%endif

%define		orgname		qtdeclarative
%define		qtbase_ver		%{version}
%define		qttools_linguist_ver	5.5
%define		qttools_assistant_ver	5.9
Summary:	The Qt5 Declarative libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Declarative
Name:		qt5-%{orgname}
Version:	5.15.16
Release:	2
License:	LGPL v2.1 or LGPL v3 with Qt Company LGPL Exception v1.1
Group:		X11/Libraries
Source0:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/%{orgname}-everywhere-opensource-src-%{version}.tar.xz
# Source0-md5:	5fbc16b594913626aa1da2b0ecc46714
Source1:	https://download.qt.io/official_releases/qt/5.15/%{version}/submodules/qttranslations-everywhere-opensource-src-%{version}.tar.xz
# Source1-md5:	2f9320ff53b3cb51482cd45eec25a470
URL:		https://www.qt.io/
%{?with_openvg:BuildRequires:	EGL-devel}
BuildRequires:	OpenGL-devel
%{?with_openvg:BuildRequires:	OpenVG-devel}
BuildRequires:	Qt5Core-devel >= %{qtbase_ver}
BuildRequires:	Qt5Gui-devel >= %{qtbase_ver}
BuildRequires:	Qt5Network-devel >= %{qtbase_ver}
BuildRequires:	Qt5Sql-devel >= %{qtbase_ver}
BuildRequires:	Qt5Test-devel >= %{qtbase_ver}
BuildRequires:	Qt5Widgets-devel >= %{qtbase_ver}
%if %{with doc}
BuildRequires:	qt5-assistant >= %{qttools_assistant_ver}
%endif
BuildRequires:	qt5-build >= %{qtbase_ver}
%{?with_qm:BuildRequires:	qt5-linguist >= %{qttools_linguist_ver}}
BuildRequires:	qt5-qmake >= %{qtbase_ver}
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# qml: Core Gui Qml Widgets
# qmlcachegen: Core
# qmleasing: Core Gui Qml Quick Widgets
# qmlformat: Core
# qmlimportscanner: Core
# qmllint: Core
# qmlmin: Core
# qmlplugindump: Core Gui Qml Widgets
# qmlpreview: Core Network
# qmlprofiler: Core Network
# qmlscene: Core Gui Qml Quick Widgets
# qmltestrunner: Core QuickTest
# qmltyperegistrar: Core
Requires:	Qt5Core >= %{qtbase_ver}
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml = %{version}-%{release}
Requires:	Qt5Quick = %{version}-%{release}
Requires:	Qt5Widgets >= %{qtbase_ver}
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

%package -n Qt5Qml
Summary:	Qt5 Qml libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Qml
Group:		Libraries
# Qt5Qml: Core Network
# Qt5QmlModels: Core Qml
# Qt5QmlWorkerScript: Core Network Qml
%requires_eq_to	Qt5Core Qt5Core-devel
Requires:	Qt5Network >= %{qtbase_ver}

%description -n Qt5Qml
The Qt5 QML module provides a framework for developing applications
and libraries with the QML language. It defines and implements the
language and engine infrastructure, and provides an API to enable
application developers to extend the QML language with custom types
and integrate QML code with JavaScript and C++. The Qt5 QML module
provides both a QML API and a C++ API.

%description -n Qt5Qml -l pl.UTF-8
Moduł Qt5 Qml dostarcza szkielet do tworzenia aplikacji i bibliotek
przy użyciu języka QML. Moduł definiuje i implementuje język oraz
silnik, a także udostąpnia API pozwalające programistom rozszerzać
język QML o własne typy oraz integrować kod w języku QML z
JavaScriptem i C++. Moduł Qt5 QML udostępnia API zarówno dla języka
QML, jak i C++.

%package -n Qt5Qml-devel
Summary:	Qt5 Qml libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 Qml - pliki programistyczne
Group:		Development/Libraries
# Qt5Qml: Core Network
# Qt5QmlModels: Core Network Qml
# Qt5QmlWorkerScript: Core Network Qml
# Qt5PacketProtocol.a: Core
# Qt5QmlDebug.a: Core Network PacketProtocol Qml
# Qt5QmlDevTools.a: Core
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Qml = %{version}-%{release}
Obsoletes:	qt5-qtdeclarative-devel < 5.2.1-1

%description -n Qt5Qml-devel
Qt5 Qml libraries - development files.

%description -n Qt5Qml-devel -l pl.UTF-8
Biblioteki Qt5 Qml - pliki programistyczne.

%package -n Qt5Quick
Summary:	Qt5 Quick libraries
Summary(pl.UTF-8):	Biblioteki Qt5 Quick
Group:		X11/Libraries
# Qt5Quick: Core Gui Network Qml QmlModels
# Qt5QuickParticles: Core Gui Qml Quick GL
# Qt5QuickShapes: Core Gui Qml Quick
# Qt5QuickTest: Core Gui Qml Quick Test Widgets
# Qt5QuickWidgets: Core Gui Qml Quick Widgets
%requires_eq_to	Qt5Core Qt5Core-devel
Requires:	Qt5Gui >= %{qtbase_ver}
Requires:	Qt5Network >= %{qtbase_ver}
Requires:	Qt5Qml = %{version}-%{release}
Requires:	Qt5Test >= %{qtbase_ver}
Requires:	Qt5Widgets >= %{qtbase_ver}

%description -n Qt5Quick
The Qt5 Quick module is the standard library for writing QML
applications. While the Qt5 QML module provides the QML engine and
language infrastructure, the Qt5 Quick module provides all the basic
types necessary for creating user interfaces with QML. It provides a
visual canvas and includes types for creating and animating visual
components, receiving user input, creating data models and views and
delayed object instantiation.

The Qt5 Quick module provides both a QML API which supplies QML types
for creating user interfaces with the QML language, and a C++ API for
extending QML applications with C++ code.

%description -n Qt5Quick -l pl.UTF-8
Moduł Qt5 Quick to biblioteka standardowa do pisania aplikacji QML.
Sam moduł Qt5 QML dostarcza silnik i infrastrukturę języka, natomiast
moduł Qt5 Quick udostępnia wszystkie podstawowe typy niezbędne do
tworzenia interfejsu użytkownika przy użyciu języka QML. Udostępnia
graficzne "płótno", zawiera typy do tworzenia i animowania komponentów
graficznych, odczytu wejścia od użytkownika, tworzenia modeli i
widoków danych oraz opóźnionych instancji obiektów.

Moduł Qt5 Quick dostarcza API zarówno dla języka QML, zapewniające
typy QML do tworzenia interfejsów użytkownika w języku QML, jak i dla
języka C++ do rozszerzania aplikacji QML przy użyciu kodu w C++.

%package -n Qt5Quick-devel
Summary:	Qt5 Qml libraries - development files
Summary(pl.UTF-8):	Biblioteki Qt5 Qml - pliki programistyczne
Group:		X11/Development/Libraries
# Qt5Quick: Core Gui Network Qml QmlModels
# Qt5QuickParticles: Core Gui Network Qml QmlModels Quick
# Qt5QuickShapes: Core Gui Network Qml QmlModels Quick
# Qt5QuickTest: Core Gui Test Widgets
# Qt5QuickWidgets: Core Gui Network Qml QmlModels Quick Test Widgets
Requires:	Qt5Core-devel >= %{qtbase_ver}
Requires:	Qt5Gui-devel >= %{qtbase_ver}
Requires:	Qt5Network-devel >= %{qtbase_ver}
Requires:	Qt5Qml-devel = %{version}-%{release}
Requires:	Qt5Quick = %{version}-%{release}
Requires:	Qt5Widgets-devel >= %{qtbase_ver}
Requires:	qt5-qtdeclarative >= %{qtbase_ver}

%description -n Qt5Quick-devel
Qt5 Qml libraries - development files.

%description -n Qt5Quick-devel -l pl.UTF-8
Biblioteki Qt5 Qml - pliki programistyczne.

%package doc
Summary:	Qt5 Declarative documentation in HTML format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Declarative w formacie HTML
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc
Qt5 Declarative documentation in HTML format.

%description doc -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Declarative w formacie HTML.

%package doc-qch
Summary:	Qt5 Declarative documentation in QCH format
Summary(pl.UTF-8):	Dokumentacja do bibliotek Qt5 Declarative w formacie QCH
Group:		Documentation
Requires:	qt5-doc-common >= %{qtbase_ver}
BuildArch:	noarch

%description doc-qch
Qt5 Declarative documentation in QCH format.

%description doc-qch -l pl.UTF-8
Dokumentacja do bibliotek Qt5 Declarative w formacie QCH.

%package examples
Summary:	Qt5 Declarative examples
Summary(pl.UTF-8):	Przykłady do bibliotek Qt5 Declarative
Group:		X11/Development/Libraries
BuildArch:	noarch

%description examples
Qt5 Declarative examples.

%description examples -l pl.UTF-8
Przykłady do bibliotek Qt5 Declarative.

%prep
%setup -q -n %{orgname}-everywhere-src-%{version} %{?with_qm:-a1}

%if %{without openvg}
%{__sed} -i '/openvg/d' src/plugins/scenegraph/scenegraph.pro
%endif

%build
%{qmake_qt5} -- \
	%{!?with_jit:-no}-feature-qml-jit

%{__make}

%{?with_doc:%{__make} docs}

%if %{with qm}
cd qttranslations-everywhere-src-%{version}
%{qmake_qt5}
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%if %{with doc}
%{__make} install_docs \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

%if %{with qm}
%{__make} -C qttranslations-everywhere-src-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
# keep only qtdeclarative
%{__rm} $RPM_BUILD_ROOT%{_datadir}/qt5/translations/{assistant,designer,linguist,qt,qtbase,qtconnectivity,qtlocation,qtmultimedia,qtquickcontrols,qtquickcontrols2,qtserialport,qtscript,qtwebengine,qtwebsockets,qtxmlpatterns}_*.qm
%endif

# kill unnecessary -L%{_libdir} from *.la, *.prl, *.pc
%{__sed} -i -e "s,-L%{_libdir} \?,,g" \
	$RPM_BUILD_ROOT%{_libdir}/*.{la,prl} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# useless symlinks
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.so.5.??
# actually drop *.la, follow policy of not packaging them when *.pc exist
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libQt5*.la

# symlinks in system bin dir
for f in qml qmlcachegen qmlimportscanner qmlmin qmlplugindump qmlpreview qmlprofiler qmlscene qmltestrunner qmltime qmleasing qmllint qmlformat qmltyperegistrar; do
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

# find_lang --with-qm supports only PLD qt3/qt4 specific %{_localedir}/*/LC_MESSAGES layout
find_qt5_qm()
{
	name="$1"
	find $RPM_BUILD_ROOT%{_datadir}/qt5/translations -name "${name}_*.qm" | \
		sed -e "s:^$RPM_BUILD_ROOT::" \
		    -e 's:\(.*/'$name'_\)\([a-z][a-z][a-z]\?\)\(_[A-Z][A-Z]\)\?\(\.qm\)$:%lang(\2\3) \1\2\3\4:'
}

echo '%defattr(644,root,root,755)' > qtdeclarative.lang
%if %{with qm}
find_qt5_qm qtdeclarative >> qtdeclarative.lang
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n Qt5Qml -p /sbin/ldconfig
%postun	-n Qt5Qml -p /sbin/ldconfig

%post	-n Qt5Quick -p /sbin/ldconfig
%postun	-n Qt5Quick -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qmlcachegen-qt5
%attr(755,root,root) %{_bindir}/qmleasing-qt5
%attr(755,root,root) %{_bindir}/qmlformat-qt5
%attr(755,root,root) %{_bindir}/qmlimportscanner-qt5
%attr(755,root,root) %{_bindir}/qmllint-qt5
%attr(755,root,root) %{_bindir}/qmlmin-qt5
%attr(755,root,root) %{_bindir}/qmlplugindump-qt5
%attr(755,root,root) %{_bindir}/qmlpreview-qt5
%attr(755,root,root) %{_bindir}/qmlprofiler-qt5
%attr(755,root,root) %{_bindir}/qml-qt5
%attr(755,root,root) %{_bindir}/qmlscene-qt5
%attr(755,root,root) %{_bindir}/qmltestrunner-qt5
%attr(755,root,root) %{_bindir}/qmltime-qt5
%attr(755,root,root) %{_bindir}/qmltyperegistrar-qt5
%attr(755,root,root) %{qt5dir}/bin/qml
%attr(755,root,root) %{qt5dir}/bin/qmlcachegen
%attr(755,root,root) %{qt5dir}/bin/qmleasing
%attr(755,root,root) %{qt5dir}/bin/qmlformat
%attr(755,root,root) %{qt5dir}/bin/qmlimportscanner
%attr(755,root,root) %{qt5dir}/bin/qmllint
%attr(755,root,root) %{qt5dir}/bin/qmlmin
%attr(755,root,root) %{qt5dir}/bin/qmlplugindump
%attr(755,root,root) %{qt5dir}/bin/qmlpreview
%attr(755,root,root) %{qt5dir}/bin/qmlprofiler
%attr(755,root,root) %{qt5dir}/bin/qmlscene
%attr(755,root,root) %{qt5dir}/bin/qmltestrunner
%attr(755,root,root) %{qt5dir}/bin/qmltime
%attr(755,root,root) %{qt5dir}/bin/qmltyperegistrar

%files -n Qt5Qml -f qtdeclarative.lang
%defattr(644,root,root,755)
%doc LICENSE.GPL3-EXCEPT
%attr(755,root,root) %{_libdir}/libQt5Qml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Qml.so.5
%attr(755,root,root) %{_libdir}/libQt5QmlModels.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QmlModels.so.5
%attr(755,root,root) %{_libdir}/libQt5QmlWorkerScript.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QmlWorkerScript.so.5

# loaded from src/qml/debugger/{qqmldebugserver,qqmlinspectorservice}.cpp
%dir %{qt5dir}/plugins/qmltooling
# R: Core Network Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_debugger.so
# R: Core Network Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_local.so
# R: Core Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_messages.so
# R: Core Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_native.so
# R: Core Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_nativedebugger.so
# R: Core Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_profiler.so
# R: Core Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_server.so
# R: Core Network Qml
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_tcp.so

%dir %{qt5dir}/qml
%dir %{qt5dir}/qml/Qt
%dir %{qt5dir}/qml/Qt/labs
%dir %{qt5dir}/qml/Qt/labs/animation
# R: Core Qml
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/animation/liblabsanimationplugin.so
%{qt5dir}/qml/Qt/labs/animation/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/animation/qmldir

%dir %{qt5dir}/qml/Qt/labs/folderlistmodel
# R: Core Qml
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/folderlistmodel/libqmlfolderlistmodelplugin.so
%{qt5dir}/qml/Qt/labs/folderlistmodel/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/folderlistmodel/qmldir

%dir %{qt5dir}/qml/Qt/labs/qmlmodels
%{qt5dir}/qml/Qt/labs/qmlmodels/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/qmlmodels/qmldir
# R: Core Qml QmlModels
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/qmlmodels/liblabsmodelsplugin.so

%dir %{qt5dir}/qml/Qt/labs/settings
# R: Core Qml
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/settings/libqmlsettingsplugin.so
%{qt5dir}/qml/Qt/labs/settings/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/settings/qmldir

%dir %{qt5dir}/qml/QtQml
# R: Core Qml QmlModels
%attr(755,root,root) %{qt5dir}/qml/QtQml/libqmlplugin.so
%dir %{qt5dir}/qml/QtQml/Models.2
# R: Core Qml QmlModels
%attr(755,root,root) %{qt5dir}/qml/QtQml/Models.2/libmodelsplugin.so
%{qt5dir}/qml/QtQml/Models.2/plugins.qmltypes
%{qt5dir}/qml/QtQml/Models.2/qmldir

%dir %{qt5dir}/qml/QtQml/StateMachine
# R: Core Qml
%attr(755,root,root) %{qt5dir}/qml/QtQml/StateMachine/libqtqmlstatemachine.so
%{qt5dir}/qml/QtQml/StateMachine/plugins.qmltypes
%{qt5dir}/qml/QtQml/StateMachine/qmldir

%dir %{qt5dir}/qml/QtQml/WorkerScript.2
# R: Core Qml QmlWorkerScript
%attr(755,root,root) %{qt5dir}/qml/QtQml/WorkerScript.2/libworkerscriptplugin.so
%{qt5dir}/qml/QtQml/WorkerScript.2/plugins.qmltypes
%{qt5dir}/qml/QtQml/WorkerScript.2/qmldir

%{qt5dir}/qml/QtQml/plugins.qmltypes
%{qt5dir}/qml/QtQml/qmldir
%{qt5dir}/qml/builtins.qmltypes

%files -n Qt5Qml-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Qml.so
%attr(755,root,root) %{_libdir}/libQt5QmlModels.so
%attr(755,root,root) %{_libdir}/libQt5QmlWorkerScript.so
# static-only
%{_libdir}/libQt5PacketProtocol.a
%{_libdir}/libQt5QmlDebug.a
%{_libdir}/libQt5QmlDevTools.a
%{_libdir}/libQt5PacketProtocol.prl
%{_libdir}/libQt5Qml.prl
%{_libdir}/libQt5QmlDebug.prl
%{_libdir}/libQt5QmlDevTools.prl
%{_libdir}/libQt5QmlModels.prl
%{_libdir}/libQt5QmlWorkerScript.prl
%{_libdir}/metatypes/qt5qml_metatypes.json
%{_libdir}/metatypes/qt5qmlmodels_metatypes.json
%{_libdir}/metatypes/qt5qmlworkerscript_metatypes.json
%{_includedir}/qt5/QtQml
%{_includedir}/qt5/QtQmlDebug
%{_includedir}/qt5/QtQmlModels
%{_includedir}/qt5/QtQmlWorkerScript
%{_includedir}/qt5/QtPacketProtocol
%{_pkgconfigdir}/Qt5Qml.pc
%{_pkgconfigdir}/Qt5QmlModels.pc
%{_pkgconfigdir}/Qt5QmlWorkerScript.pc
%{_libdir}/cmake/Qt5PacketProtocol
%{_libdir}/cmake/Qt5Qml
%{_libdir}/cmake/Qt5QmlDebug
%{_libdir}/cmake/Qt5QmlDevTools
%{_libdir}/cmake/Qt5QmlImportScanner
%{_libdir}/cmake/Qt5QmlModels
%{_libdir}/cmake/Qt5QmlWorkerScript
%{_libdir}/cmake/Qt5QuickParticles
%{_libdir}/cmake/Qt5QuickShapes
%{qt5dir}/mkspecs/features/qmlcache.prf
%{qt5dir}/mkspecs/features/qmltypes.prf
%{qt5dir}/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qml.pri
%{qt5dir}/mkspecs/modules/qt_lib_qml_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmldebug_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmldevtools_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmlmodels.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmltest.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmltest_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{qt5dir}/mkspecs/modules/qt_lib_qmlworkerscript_private.pri

%files -n Qt5Quick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Quick.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5Quick.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickParticles.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickShapes.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickShapes.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickTest.so.5
%attr(755,root,root) %{_libdir}/libQt5QuickWidgets.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQt5QuickWidgets.so.5

# R: Core Gui Qml Quick
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_inspector.so
# R: Core Gui Qml Quick
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_preview.so
# R: Core Qml Quick
%attr(755,root,root) %{qt5dir}/plugins/qmltooling/libqmldbg_quickprofiler.so

%if %{with openvg}
%dir %{qt5dir}/plugins/scenegraph
# R: Core Gui Quick EGL OpenVG
%attr(755,root,root) %{qt5dir}/plugins/scenegraph/libqsgopenvgbackend.so
%endif

%dir %{qt5dir}/qml/Qt/labs/sharedimage
# R: Core Gui Qml Quick
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/sharedimage/libsharedimageplugin.so
%{qt5dir}/qml/Qt/labs/sharedimage/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/sharedimage/qmldir

%dir %{qt5dir}/qml/Qt/labs/wavefrontmesh
# R: Core Gui Qml Quick
%attr(755,root,root) %{qt5dir}/qml/Qt/labs/wavefrontmesh/libqmlwavefrontmeshplugin.so
%{qt5dir}/qml/Qt/labs/wavefrontmesh/plugins.qmltypes
%{qt5dir}/qml/Qt/labs/wavefrontmesh/qmldir

%dir %{qt5dir}/qml/Qt/test
%dir %{qt5dir}/qml/Qt/test/qtestroot
%{qt5dir}/qml/Qt/test/qtestroot/plugins.qmltypes
%{qt5dir}/qml/Qt/test/qtestroot/qmldir

%dir %{qt5dir}/qml/QtQuick

%dir %{qt5dir}/qml/QtQuick/Layouts
# R: Core Gui Qml Quick
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Layouts/libqquicklayoutsplugin.so
%{qt5dir}/qml/QtQuick/Layouts/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Layouts/qmldir

%dir %{qt5dir}/qml/QtQuick/LocalStorage
# R: Core Qml Sql
%attr(755,root,root) %{qt5dir}/qml/QtQuick/LocalStorage/libqmllocalstorageplugin.so
%{qt5dir}/qml/QtQuick/LocalStorage/plugins.qmltypes
%{qt5dir}/qml/QtQuick/LocalStorage/qmldir

%dir %{qt5dir}/qml/QtQuick/Particles.2
# R: Core Qml QuickParticles
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Particles.2/libparticlesplugin.so
%{qt5dir}/qml/QtQuick/Particles.2/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Particles.2/qmldir

%dir %{qt5dir}/qml/QtQuick/Shapes
# R: Core Qml QuickShapes
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Shapes/libqmlshapesplugin.so
%{qt5dir}/qml/QtQuick/Shapes/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Shapes/qmldir

%dir %{qt5dir}/qml/QtQuick/Window.2
# R: Core Gui Qml Quick
%attr(755,root,root) %{qt5dir}/qml/QtQuick/Window.2/libwindowplugin.so
%{qt5dir}/qml/QtQuick/Window.2/plugins.qmltypes
%{qt5dir}/qml/QtQuick/Window.2/qmldir

%dir %{qt5dir}/qml/QtQuick.2
# R: Core Qml QmlModels QmlWorkerScript Quick
%attr(755,root,root) %{qt5dir}/qml/QtQuick.2/libqtquick2plugin.so
%{qt5dir}/qml/QtQuick.2/plugins.qmltypes
%{qt5dir}/qml/QtQuick.2/qmldir

%dir %{qt5dir}/qml/QtTest
# R: Core Gui Qml Quick QuickTest Widgets Test
%attr(755,root,root) %{qt5dir}/qml/QtTest/libqmltestplugin.so
%{qt5dir}/qml/QtTest/plugins.qmltypes
%{qt5dir}/qml/QtTest/qmldir
%{qt5dir}/qml/QtTest/testlogger.js
%{qt5dir}/qml/QtTest/*.qml

%files -n Qt5Quick-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libQt5Quick.so
%attr(755,root,root) %{_libdir}/libQt5QuickParticles.so
%attr(755,root,root) %{_libdir}/libQt5QuickShapes.so
%attr(755,root,root) %{_libdir}/libQt5QuickTest.so
%attr(755,root,root) %{_libdir}/libQt5QuickWidgets.so
%{_libdir}/libQt5Quick.prl
%{_libdir}/libQt5QuickParticles.prl
%{_libdir}/libQt5QuickShapes.prl
%{_libdir}/libQt5QuickTest.prl
%{_libdir}/libQt5QuickWidgets.prl
%{_libdir}/metatypes/qt5quick_metatypes.json
%{_libdir}/metatypes/qt5quickparticles_metatypes.json
%{_libdir}/metatypes/qt5quickshapes_metatypes.json
%{_libdir}/metatypes/qt5quicktest_metatypes.json
%{_includedir}/qt5/QtQuick
%{_includedir}/qt5/QtQuickParticles
%{_includedir}/qt5/QtQuickShapes
%{_includedir}/qt5/QtQuickTest
%{_includedir}/qt5/QtQuickWidgets
%{_pkgconfigdir}/Qt5Quick.pc
%{_pkgconfigdir}/Qt5QuickTest.pc
%{_pkgconfigdir}/Qt5QuickWidgets.pc
%{_libdir}/cmake/Qt5Quick
%{_libdir}/cmake/Qt5QuickCompiler
%{_libdir}/cmake/Qt5QuickTest
%{_libdir}/cmake/Qt5QuickWidgets
%{qt5dir}/mkspecs/features/qtquickcompiler.prf
%{qt5dir}/mkspecs/modules/qt_lib_quick.pri
%{qt5dir}/mkspecs/modules/qt_lib_quick_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_quickparticles_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_quickshapes_private.pri
%{qt5dir}/mkspecs/modules/qt_lib_quickwidgets.pri
%{qt5dir}/mkspecs/modules/qt_lib_quickwidgets_private.pri

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtqml
%{_docdir}/qt5-doc/qtqmlmodels
%{_docdir}/qt5-doc/qtqmltest
%{_docdir}/qt5-doc/qtqmlworkerscript
%{_docdir}/qt5-doc/qtquick

%files doc-qch
%defattr(644,root,root,755)
%{_docdir}/qt5-doc/qtqml.qch
%{_docdir}/qt5-doc/qtqmlmodels.qch
%{_docdir}/qt5-doc/qtqmltest.qch
%{_docdir}/qt5-doc/qtqmlworkerscript.qch
%{_docdir}/qt5-doc/qtquick.qch
%endif

%files examples -f examples.files
%defattr(644,root,root,755)
# XXX: dir shared with qt5-qtbase-examples
%dir %{_examplesdir}/qt5
