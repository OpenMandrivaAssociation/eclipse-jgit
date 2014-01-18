%{?_javapackages_macros:%_javapackages_macros}
%global install_loc    %{_datadir}/eclipse/dropins/jgit
%global version_suffix 201310021548-r

%{?scl:%scl_package eclipse-jgit}
%{!?scl:%global pkg_name %{name}}


Name:           %{?scl_prefix}eclipse-jgit
Version:        3.1.0
Release:        1.0%{?dist}
Summary:        Eclipse JGit


License:        BSD
URL:            http://www.eclipse.org/egit/
Source0:        http://git.eclipse.org/c/jgit/jgit.git/snapshot/jgit-%{version}.%{version_suffix}.tar.bz2
Patch0:         fix_jgit_sh.patch
Patch1:			eclipse-jgit-413163.patch

BuildArch: noarch

BuildRequires: java-devel
BuildRequires: %{?scl_prefix}eclipse-pde >= 1:3.5.0
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shade-plugin
BuildRequires:  tycho
BuildRequires:  eclipse-equinox-osgi
BuildRequires:  eclipse-platform
BuildRequires:  args4j >= 2.0.12
BuildRequires:  apache-commons-compress
BuildRequires:  xz-java >= 1.1-2
BuildRequires:  javaewah
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  feclipse-maven-plugin >= 0.0.3
%{?scl:Requires: %scl_runtime}
Requires: %{?scl_prefix}eclipse-platform >= 3.5.0
Requires:  javaewah

%description
A pure Java implementation of the Git version control system.

%package -n     %{?scl_prefix}jgit-javadoc
Summary:        API documentation for %{pkg_name}

Requires:       jpackage-utils

%description -n %{?scl_prefix}jgit-javadoc
%{summary}.

%package -n     %{?scl_prefix}jgit
Summary:        Java-based command line Git interface

Requires:       args4j >= 2.0.12
Requires:       java >= 1.6.0
Requires:       apache-commons-compress
Requires:       xz-java >= 1.1-2
Requires:       jpackage-utils
Requires:       javaewah

%description -n %{?scl_prefix}jgit
Command line Git tool built entirely in Java.

%prep
%setup -n jgit-%{version}.%{version_suffix} -q

%patch0
%patch1 -p1

#javaevah change
sed -i -e 's/javaewah/com.googlecode.javaewah/g' org.eclipse.jgit/META-INF/MANIFEST.MF
find -name *.java -exec sed -i -e "s/javaewah/com.googlecode.javaewah/g" {} \;
sed -i -e "s/javaewah/com.googlecode.javaewah.JavaEWAH/g" org.eclipse.jgit.packaging/org.eclipse.jgit.feature/feature.xml

#don't try to get it from local *maven* repo, use tycho resolved one
%pom_remove_dep com.googlecode.javaewah:JavaEWAH

#those bundles don't compile with latest jetty
%pom_disable_module org.eclipse.jgit.http.test
%pom_disable_module org.eclipse.jgit.pgm.test
%pom_disable_module org.eclipse.jgit.junit.http
%pom_remove_dep : org.eclipse.jgit.packaging/org.eclipse.jgit.repository

%pom_disable_module org.eclipse.jgit.target org.eclipse.jgit.packaging
%pom_xpath_remove "pom:build/pom:pluginManagement/pom:plugins/pom:plugin/pom:configuration/pom:target" org.eclipse.jgit.packaging/pom.xml

%pom_disable_module org.eclipse.jgit.java7.feature org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.source.feature org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.junit.feature org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.pgm.feature org.eclipse.jgit.packaging
%pom_disable_module org.eclipse.jgit.pgm.source.feature org.eclipse.jgit.packaging

# remove all features except for jgit
sed -i -e '9,23d' org.eclipse.jgit.packaging/org.eclipse.jgit.repository/category.xml

sed -i -e 's/\, multiValued = true//' org.eclipse.jgit.pgm/src/org/eclipse/jgit/pgm/Status.java

%build
%{?scl:%scl_maven_opts}
mvn-rpmbuild -Dmaven.test.skip=true install
mvn-rpmbuild -Dmaven.test.skip=true -f org.eclipse.jgit.packaging/pom.xml verify

%install
install -d -m 755 %{buildroot}%{install_loc}


mvn-rpmbuild org.fedoraproject:feclipse-maven-plugin:install  \
               -DskipTychoVersionCheck \
               -DsourceRepo=`pwd`/org.eclipse.jgit.packaging/org.eclipse.jgit.repository/target/repository \
               -DtargetLocation=%{buildroot}%{install_loc}/eclipse

pushd %{buildroot}%{install_loc}/eclipse/plugins
    rm com.jcraft.jsch_*.jar
    rm com.googlecode.javaewah.JavaEWAH_*.jar
#to the future maintainers - dont forget to add those jars to the fix_jgit_sh.patch
    ln -s %{_javadir}/args4j.jar
    ln -s %{_javadir}/commons-compress.jar
    ln -s %{_javadir}/xz-java.jar
    ln -s %{_javadir}/javaewah/JavaEWAH.jar
popd

#giant hack - for some reason source bundle is in the repo, install the proper one
cp org.eclipse.jgit/target/org.eclipse.jgit-*-r.jar %{buildroot}%{install_loc}/eclipse/plugins 

# JARs
install -d -m 0755 %{buildroot}%{_javadir}/jgit
install -m 644 org.eclipse.jgit/target/org.eclipse.jgit-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/jgit.jar
install -m 644 org.eclipse.jgit.ui/target/org.eclipse.jgit.ui-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/ui.jar
install -m 644 org.eclipse.jgit.java7/target/org.eclipse.jgit.java7-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/java7.jar
install -m 644 org.eclipse.jgit.console/target/org.eclipse.jgit.console-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/console.jar
install -m 644 org.eclipse.jgit.pgm/target/org.eclipse.jgit.pgm-%{version}.%{version_suffix}.jar   %{buildroot}%{_javadir}/jgit/pgm.jar
# Javadocs
install -d -m 755 %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit/target/apidocs %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit.ui/target/apidocs %{buildroot}%{_javadocdir}/jgit
cp -rp org.eclipse.jgit.console/target/apidocs %{buildroot}%{_javadocdir}/jgit
# POM Files
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-jgit-parent.pom
install -pm 644 org.eclipse.jgit/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-jgit.pom
install -pm 644 org.eclipse.jgit.ui/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-ui.pom
install -pm 644 org.eclipse.jgit.java7/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-java7.pom
install -pm 644 org.eclipse.jgit.console/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-console.pom
install -pm 644 org.eclipse.jgit.pgm/pom.xml %{buildroot}%{_mavenpomdir}/JPP.jgit-pgm.pom

%add_maven_depmap JPP.jgit-jgit.pom jgit/jgit.jar
%add_maven_depmap JPP.jgit-ui.pom jgit/ui.jar
%add_maven_depmap JPP.jgit-java7.pom jgit/java7.jar
%add_maven_depmap JPP.jgit-console.pom jgit/console.jar
%add_maven_depmap JPP.jgit-pgm.pom jgit/pgm.jar
%add_maven_depmap JPP-jgit-parent.pom
# Binary
install -dm 755 %{buildroot}%{_bindir}
install -m 755 org.eclipse.jgit.pgm/jgit.sh %{buildroot}%{_bindir}/jgit

%files
%doc LICENSE 
%doc README.md
%{install_loc}

%files -n %{?scl_prefix}jgit
%{_bindir}/jgit
%{_javadir}/jgit
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-jgit-parent.pom
%{_mavenpomdir}/JPP.jgit*.pom
%doc LICENSE 
%doc README.md

%files -n %{?scl_prefix}jgit-javadoc
%{_javadocdir}/jgit
%doc LICENSE 
%doc README.md

%changelog
* Thu Oct 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.1.0-1
- Update to Kepler SR1.

* Mon Aug 5 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-7
- Add missing jgit plugin back.

* Tue Jul 16 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-6
- Change the build system to mvn-rpmbuild.
- Use feclipse-maven-plugin to install things.
- Bug 413163 - Incompatible change in latest args4j: multiValued removed from @Option

* Fri Jul 5 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-5
- Bump release

* Tue Jun 25 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jun 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-3
- Add missing R: javaewah to eclipse-jgit.

* Tue Jun 25 2013 Krzysztof Daniel <kdaniel@redhat.com> 3.0.0-2
- Move symlinks to eclipse-jgit.
- Fix jgit classpath.

* Thu Jun 20 2013 Neil Brian Guzman <nguzman@redhat.com> 3.0.0-1
- Update to 3.0.0 release

* Tue May 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.3.1-2
- Rebuild with latest icu4j.

* Thu Feb 21 2013 Roland Grunberg <rgrunber@redhat.com> - 2.3.1-1
- SCL-ize package.

* Thu Feb 21 2013 Roland Grunberg <rgrunber@redhat.com> - 2.3.1-1
- Update to 2.3.1 release.

* Thu Feb 14 2013 Roland Grunberg <rgrunber@redhat.com> - 2.2.0-3
- jgit subpackage should own its symlinked dependencies.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.2.0-1
- Update to 2.2.0 release.

* Mon Oct 1 2012 Alexander Kurtakov <akurtako@redhat.com> 2.1.0-1
- Update to 2.1.0 release.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Update to 2.0.0 upstream release.

* Fri Apr 27 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-3
- Use eclipse-pdebuild over old pdebuild script.

* Thu Apr 26 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.3.0-2
- Tweak .spec so as to avoid modifying to much of the .spec file
- Fix upstream 1.3 release sources.

* Fri Feb 17 2012 Andrew Robinson <arobinso@redhat.com> 1.3.0-1
- Update to 1.3.0 upstream release.

* Thu Jan 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-2
- Build eclipse plugin first to not interfere with maven artifacts.

* Thu Jan 5 2012 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-1
- Update to 1.2.0 release.

* Fri Oct 28 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-4
- Add jsch jar to the classpath.

* Fri Oct 28 2011 Alexander Kurtakov <akurtako@redhat.com> 1.1.0-3
- Drop libs subpackage and use the sh script directly instead of the shaded executable.
- Install jars in _javadir subdir as per guidelines.

* Thu Oct 27 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-2
- Added Java libraries, javadocs and console binary subpackages.

* Fri Sep 23 2011 Andrew Robinson <arobinso@redhat.com> 1.1.0-1
- Update to upstream release 1.1.0.

* Tue Jun 14 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-2
- Update to upstream release 1.0.0.201106090707-r.

* Tue Jun 07 2011 Chris Aniszczyk <zx@redhat.com> 1.0.0-1
- Update to upstream release 1.0.0.

* Tue May 03 2011 Chris Aniszczyk <zx@redhat.com> 0.12.1-1
- Update to upstream release 0.12.1.

* Tue Feb 22 2011 Chris Aniszczyk <zx@redhat.com> 0.11.3-1
- Update to upstream release 0.11.3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Chris Aniszczyk <zx@redhat.com> 0.10.1-1
- Update to upstream release 0.10.1.

* Thu Oct 7 2010 Chris Aniszczyk <zx@redhat.com> 0.9.3-1
- Update to upstream release 0.9.3.

* Wed Sep 15 2010 Severin Gehwolf <sgehwolf@redhat.com> 0.9.1-1
- Update to upstream release 0.9.1.

* Thu Aug 26 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.1.20100825git
- Make release tag more readable (separate "0.1" and pre-release tag by ".").

* Wed Aug 25 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.9.0-0.120100825git
- Pre-release version of JGit 0.9.0

* Fri Jun 25 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.8.4-2
- Increase release number to make tagging work.

* Wed Jun 23 2010 Severin Gehwolf <sgehwolf at, redhat.com> 0.8.4-1
- Rebase to 0.8.4 release.

* Mon Apr 12 2010 Jeff Johnston <jjohnstn@redhat.com> 0.7.1-1
- Rebase to 0.7.1 release.

* Tue Feb 9 2010 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20100208
- New git snapshot.

* Thu Nov 5 2009 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.1.git20091029
- Correct release.

* Thu Oct 29 2009 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-0.git20091029.1
- Initial package
