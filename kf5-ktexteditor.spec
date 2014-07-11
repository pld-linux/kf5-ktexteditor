# TODO:
# Not packaged:
# /usr/include/KF5
# /usr/lib/qt5/plugins/kf5/parts
# /usr/share/katepart
# /usr/share/katepart5/script/commands
# /usr/share/katepart5/script/files/quickcoding/cpp
# /usr/share/katepart5/script/indentation
# /usr/share/katepart5/script/libraries
# /usr/share/katepart5/script/libraries/emmet
# /usr/share/katepart5/syntax
# /usr/share/kservices5
# /usr/share/kservicetypes5
%define         _state          stable
%define		orgname		ktexteditor

Summary:	Full text editor component
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	fb438acf5b10c0e9a620916c2bfe5797
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel >= 5.2.0
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 0.0.15
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
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	-D_IMPORT_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{orgname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}5.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/katemoderc
/etc/xdg/kateschemarc
/etc/xdg/katesyntaxhighlightingrc
%attr(755,root,root) %ghost %{_libdir}/libKF5TextEditor.so.5
%attr(755,root,root) %{_libdir}/libKF5TextEditor.so.5.0.0
%attr(755,root,root) %ghost %{qt5dir}/plugins/kf5/parts/katepart.so
%{_datadir}/katepart/katepart5ui.rc
%{_datadir}/katepart5/script/commands/emmet.js
%{_datadir}/katepart5/script/commands/jumpMatchingIndent.js
%{_datadir}/katepart5/script/commands/quickcoding.js
%{_datadir}/katepart5/script/commands/utils.js
%{_datadir}/katepart5/script/files/quickcoding/cpp/a.template
%{_datadir}/katepart5/script/files/quickcoding/cpp/c.template
%{_datadir}/katepart5/script/indentation/ada.js
%{_datadir}/katepart5/script/indentation/cppstyle.js
%{_datadir}/katepart5/script/indentation/cstyle.js
%{_datadir}/katepart5/script/indentation/haskell.js
%{_datadir}/katepart5/script/indentation/latex.js
%{_datadir}/katepart5/script/indentation/lilypond.js
%{_datadir}/katepart5/script/indentation/lisp.js
%{_datadir}/katepart5/script/indentation/lua.js
%{_datadir}/katepart5/script/indentation/pascal.js
%{_datadir}/katepart5/script/indentation/python.js
%{_datadir}/katepart5/script/indentation/ruby.js
%{_datadir}/katepart5/script/indentation/xml.js
%{_datadir}/katepart5/script/libraries/cursor.js
%{_datadir}/katepart5/script/libraries/documentcursor.js
%{_datadir}/katepart5/script/libraries/emmet/editor_interface.js
%{_datadir}/katepart5/script/libraries/emmet/lib.js
%{_datadir}/katepart5/script/libraries/range.js
%{_datadir}/katepart5/script/libraries/string.js
%{_datadir}/katepart5/script/libraries/underscore.js
%{_datadir}/katepart5/script/libraries/utils.js
%{_datadir}/katepart5/syntax/abap.xml
%{_datadir}/katepart5/syntax/abc.xml
%{_datadir}/katepart5/syntax/actionscript.xml
%{_datadir}/katepart5/syntax/ada.xml
%{_datadir}/katepart5/syntax/ahdl.xml
%{_datadir}/katepart5/syntax/ahk.xml
%{_datadir}/katepart5/syntax/alert.xml
%{_datadir}/katepart5/syntax/alert_indent.xml
%{_datadir}/katepart5/syntax/ample.xml
%{_datadir}/katepart5/syntax/ansforth94.xml
%{_datadir}/katepart5/syntax/ansic89.xml
%{_datadir}/katepart5/syntax/ansys.xml
%{_datadir}/katepart5/syntax/apache.xml
%{_datadir}/katepart5/syntax/asm-avr.xml
%{_datadir}/katepart5/syntax/asm-dsp56k.xml
%{_datadir}/katepart5/syntax/asm-m68k.xml
%{_datadir}/katepart5/syntax/asm6502.xml
%{_datadir}/katepart5/syntax/asn1.xml
%{_datadir}/katepart5/syntax/asp.xml
%{_datadir}/katepart5/syntax/asterisk.xml
%{_datadir}/katepart5/syntax/awk.xml
%{_datadir}/katepart5/syntax/bash.xml
%{_datadir}/katepart5/syntax/bibtex.xml
%{_datadir}/katepart5/syntax/bmethod.xml
%{_datadir}/katepart5/syntax/boo.xml
%{_datadir}/katepart5/syntax/c.xml
%{_datadir}/katepart5/syntax/ccss.xml
%{_datadir}/katepart5/syntax/cg.xml
%{_datadir}/katepart5/syntax/cgis.xml
%{_datadir}/katepart5/syntax/changelog.xml
%{_datadir}/katepart5/syntax/chicken.xml
%{_datadir}/katepart5/syntax/cisco.xml
%{_datadir}/katepart5/syntax/clipper.xml
%{_datadir}/katepart5/syntax/clojure.xml
%{_datadir}/katepart5/syntax/cmake.xml
%{_datadir}/katepart5/syntax/coffee.xml
%{_datadir}/katepart5/syntax/coldfusion.xml
%{_datadir}/katepart5/syntax/commonlisp.xml
%{_datadir}/katepart5/syntax/component-pascal.xml
%{_datadir}/katepart5/syntax/context.xml
%{_datadir}/katepart5/syntax/cpp.xml
%{_datadir}/katepart5/syntax/crk.xml
%{_datadir}/katepart5/syntax/cs.xml
%{_datadir}/katepart5/syntax/css-php.xml
%{_datadir}/katepart5/syntax/css.xml
%{_datadir}/katepart5/syntax/cubescript.xml
%{_datadir}/katepart5/syntax/cue.xml
%{_datadir}/katepart5/syntax/curry.xml
%{_datadir}/katepart5/syntax/d.xml
%{_datadir}/katepart5/syntax/debianchangelog.xml
%{_datadir}/katepart5/syntax/debiancontrol.xml
%{_datadir}/katepart5/syntax/desktop.xml
%{_datadir}/katepart5/syntax/diff.xml
%{_datadir}/katepart5/syntax/djangotemplate.xml
%{_datadir}/katepart5/syntax/dosbat.xml
%{_datadir}/katepart5/syntax/dot.xml
%{_datadir}/katepart5/syntax/doxygen.xml
%{_datadir}/katepart5/syntax/doxygenlua.xml
%{_datadir}/katepart5/syntax/dtd.xml
%{_datadir}/katepart5/syntax/e.xml
%{_datadir}/katepart5/syntax/eiffel.xml
%{_datadir}/katepart5/syntax/email.xml
%{_datadir}/katepart5/syntax/erlang.xml
%{_datadir}/katepart5/syntax/euphoria.xml
%{_datadir}/katepart5/syntax/fasm.xml
%{_datadir}/katepart5/syntax/ferite.xml
%{_datadir}/katepart5/syntax/fgl-4gl.xml
%{_datadir}/katepart5/syntax/fgl-per.xml
%{_datadir}/katepart5/syntax/fortran.xml
%{_datadir}/katepart5/syntax/freebasic.xml
%{_datadir}/katepart5/syntax/fsharp.xml
%{_datadir}/katepart5/syntax/fstab.xml
%{_datadir}/katepart5/syntax/gap.xml
%{_datadir}/katepart5/syntax/gcc.xml
%{_datadir}/katepart5/syntax/gdb.xml
%{_datadir}/katepart5/syntax/gdl.xml
%{_datadir}/katepart5/syntax/gettext.xml
%{_datadir}/katepart5/syntax/git-rebase.xml
%{_datadir}/katepart5/syntax/glosstex.xml
%{_datadir}/katepart5/syntax/glsl.xml
%{_datadir}/katepart5/syntax/gnuassembler.xml
%{_datadir}/katepart5/syntax/gnuplot.xml
%{_datadir}/katepart5/syntax/go.xml
%{_datadir}/katepart5/syntax/grammar.xml
%{_datadir}/katepart5/syntax/haml.xml
%{_datadir}/katepart5/syntax/haskell.xml
%{_datadir}/katepart5/syntax/haxe.xml
%{_datadir}/katepart5/syntax/html-php.xml
%{_datadir}/katepart5/syntax/html.xml
%{_datadir}/katepart5/syntax/idconsole.xml
%{_datadir}/katepart5/syntax/idl.xml
%{_datadir}/katepart5/syntax/ilerpg.xml
%{_datadir}/katepart5/syntax/inform.xml
%{_datadir}/katepart5/syntax/ini.xml
%{_datadir}/katepart5/syntax/isocpp.xml
%{_datadir}/katepart5/syntax/jam.xml
%{_datadir}/katepart5/syntax/java.xml
%{_datadir}/katepart5/syntax/javadoc.xml
%{_datadir}/katepart5/syntax/javascript-php.xml
%{_datadir}/katepart5/syntax/javascript.xml
%{_datadir}/katepart5/syntax/jira.xml
%{_datadir}/katepart5/syntax/json.xml
%{_datadir}/katepart5/syntax/jsp.xml
%{_datadir}/katepart5/syntax/julia.xml
%{_datadir}/katepart5/syntax/k.xml
%{_datadir}/katepart5/syntax/kbasic.xml
%{_datadir}/katepart5/syntax/language.dtd
%{_datadir}/katepart5/syntax/latex.xml
%{_datadir}/katepart5/syntax/ld.xml
%{_datadir}/katepart5/syntax/ldif.xml
%{_datadir}/katepart5/syntax/less.xml
%{_datadir}/katepart5/syntax/lex.xml
%{_datadir}/katepart5/syntax/lilypond.xml
%{_datadir}/katepart5/syntax/literate-curry.xml
%{_datadir}/katepart5/syntax/literate-haskell.xml
%{_datadir}/katepart5/syntax/logtalk.xml
%{_datadir}/katepart5/syntax/lpc.xml
%{_datadir}/katepart5/syntax/lsl.xml
%{_datadir}/katepart5/syntax/lua.xml
%{_datadir}/katepart5/syntax/m3u.xml
%{_datadir}/katepart5/syntax/m4.xml
%{_datadir}/katepart5/syntax/mab.xml
%{_datadir}/katepart5/syntax/makefile.xml
%{_datadir}/katepart5/syntax/mako.xml
%{_datadir}/katepart5/syntax/mandoc.xml
%{_datadir}/katepart5/syntax/markdown.xml
%{_datadir}/katepart5/syntax/mason.xml
%{_datadir}/katepart5/syntax/mathematica.xml
%{_datadir}/katepart5/syntax/matlab.xml
%{_datadir}/katepart5/syntax/maxima.xml
%{_datadir}/katepart5/syntax/mediawiki.xml
%{_datadir}/katepart5/syntax/mel.xml
%{_datadir}/katepart5/syntax/mergetagtext.xml
%{_datadir}/katepart5/syntax/metafont.xml
%{_datadir}/katepart5/syntax/mips.xml
%{_datadir}/katepart5/syntax/modelica.xml
%{_datadir}/katepart5/syntax/modelines.xml
%{_datadir}/katepart5/syntax/modula-2.xml
%{_datadir}/katepart5/syntax/monobasic.xml
%{_datadir}/katepart5/syntax/mup.xml
%{_datadir}/katepart5/syntax/nagios.xml
%{_datadir}/katepart5/syntax/nasm.xml
%{_datadir}/katepart5/syntax/nemerle.xml
%{_datadir}/katepart5/syntax/nesc.xml
%{_datadir}/katepart5/syntax/noweb.xml
%{_datadir}/katepart5/syntax/objectivec.xml
%{_datadir}/katepart5/syntax/objectivecpp.xml
%{_datadir}/katepart5/syntax/ocaml.xml
%{_datadir}/katepart5/syntax/octave.xml
%{_datadir}/katepart5/syntax/oors.xml
%{_datadir}/katepart5/syntax/opal.xml
%{_datadir}/katepart5/syntax/opencl.xml
%{_datadir}/katepart5/syntax/pango.xml
%{_datadir}/katepart5/syntax/pascal.xml
%{_datadir}/katepart5/syntax/perl.xml
%{_datadir}/katepart5/syntax/pgn.xml
%{_datadir}/katepart5/syntax/php.xml
%{_datadir}/katepart5/syntax/picsrc.xml
%{_datadir}/katepart5/syntax/pig.xml
%{_datadir}/katepart5/syntax/pike.xml
%{_datadir}/katepart5/syntax/postscript.xml
%{_datadir}/katepart5/syntax/povray.xml
%{_datadir}/katepart5/syntax/ppd.xml
%{_datadir}/katepart5/syntax/progress.xml
%{_datadir}/katepart5/syntax/prolog.xml
%{_datadir}/katepart5/syntax/protobuf.xml
%{_datadir}/katepart5/syntax/puppet.xml
%{_datadir}/katepart5/syntax/purebasic.xml
%{_datadir}/katepart5/syntax/python.xml
%{_datadir}/katepart5/syntax/q.xml
%{_datadir}/katepart5/syntax/qmake.xml
%{_datadir}/katepart5/syntax/qml.xml
%{_datadir}/katepart5/syntax/r.xml
%{_datadir}/katepart5/syntax/rapidq.xml
%{_datadir}/katepart5/syntax/relaxng.xml
%{_datadir}/katepart5/syntax/relaxngcompact.xml
%{_datadir}/katepart5/syntax/replicode.xml
%{_datadir}/katepart5/syntax/rest.xml
%{_datadir}/katepart5/syntax/restructuredtext.xml
%{_datadir}/katepart5/syntax/rexx.xml
%{_datadir}/katepart5/syntax/rhtml.xml
%{_datadir}/katepart5/syntax/rib.xml
%{_datadir}/katepart5/syntax/roff.xml
%{_datadir}/katepart5/syntax/rpmspec.xml
%{_datadir}/katepart5/syntax/rsiidl.xml
%{_datadir}/katepart5/syntax/ruby.xml
%{_datadir}/katepart5/syntax/sather.xml
%{_datadir}/katepart5/syntax/scala.xml
%{_datadir}/katepart5/syntax/scheme.xml
%{_datadir}/katepart5/syntax/sci.xml
%{_datadir}/katepart5/syntax/scss.xml
%{_datadir}/katepart5/syntax/sed.xml
%{_datadir}/katepart5/syntax/sgml.xml
%{_datadir}/katepart5/syntax/sieve.xml
%{_datadir}/katepart5/syntax/sisu.xml
%{_datadir}/katepart5/syntax/sml.xml
%{_datadir}/katepart5/syntax/spice.xml
%{_datadir}/katepart5/syntax/sql-mysql.xml
%{_datadir}/katepart5/syntax/sql-postgresql.xml
%{_datadir}/katepart5/syntax/sql.xml
%{_datadir}/katepart5/syntax/stata.xml
%{_datadir}/katepart5/syntax/syntax.template
%{_datadir}/katepart5/syntax/systemc.xml
%{_datadir}/katepart5/syntax/systemverilog.xml
%{_datadir}/katepart5/syntax/tads3.xml
%{_datadir}/katepart5/syntax/tcl.xml
%{_datadir}/katepart5/syntax/tcsh.xml
%{_datadir}/katepart5/syntax/template-toolkit.xml
%{_datadir}/katepart5/syntax/texinfo.xml
%{_datadir}/katepart5/syntax/textile.xml
%{_datadir}/katepart5/syntax/tibasic.xml
%{_datadir}/katepart5/syntax/txt2tags.xml
%{_datadir}/katepart5/syntax/uscript.xml
%{_datadir}/katepart5/syntax/vala.xml
%{_datadir}/katepart5/syntax/valgrind-suppression.xml
%{_datadir}/katepart5/syntax/varnish.xml
%{_datadir}/katepart5/syntax/varnishtest.xml
%{_datadir}/katepart5/syntax/vcard.xml
%{_datadir}/katepart5/syntax/velocity.xml
%{_datadir}/katepart5/syntax/vera.xml
%{_datadir}/katepart5/syntax/verilog.xml
%{_datadir}/katepart5/syntax/vhdl.xml
%{_datadir}/katepart5/syntax/vrml.xml
%{_datadir}/katepart5/syntax/winehq.xml
%{_datadir}/katepart5/syntax/wml.xml
%{_datadir}/katepart5/syntax/xharbour.xml
%{_datadir}/katepart5/syntax/xml.xml
%{_datadir}/katepart5/syntax/xmldebug.xml
%{_datadir}/katepart5/syntax/xorg.xml
%{_datadir}/katepart5/syntax/xslt.xml
%{_datadir}/katepart5/syntax/xul.xml
%{_datadir}/katepart5/syntax/yacas.xml
%{_datadir}/katepart5/syntax/yacc.xml
%{_datadir}/katepart5/syntax/yaml.xml
%{_datadir}/katepart5/syntax/zonnon.xml
%{_datadir}/katepart5/syntax/zsh.xml
%{_datadir}/kservices5/katepart.desktop
%{_datadir}/kservicetypes5/ktexteditor.desktop
%{_datadir}/kservicetypes5/ktexteditorplugin.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KTextEditor
%{_includedir}/KF5/ktexteditor_version.h
%{_libdir}/cmake/KF5TextEditor
%attr(755,root,root) %{_libdir}/libKF5TextEditor.so
%{qt5dir}/mkspecs/modules/qt_KTextEditor.pri
