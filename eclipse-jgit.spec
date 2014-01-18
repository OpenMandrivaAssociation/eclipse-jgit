
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		eclipse-jgit
Version:	3.2.0
Release:	1.0
License:	GPLv3+
Source0:	eclipse-jgit-3.2.0-1.0-omv2014.0.noarch.rpm
Source1:	jgit-3.2.0-1.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/eclipse-jgit
BuildArch:	noarch
Summary:	eclipse-jgit bootstrap version
Requires:	javapackages-bootstrap
Requires:	eclipse-platform >= 3.5.0
Requires:	javaewah
Requires:	osgi(com.jcraft.jsch)
Provides:	eclipse-jgit = 3.2.0-1.0:2014.0
Provides:	osgi(org.apache.commons.compress) = 1.6.0
Provides:	osgi(org.eclipse.jgit) = 3.2.0
Provides:	osgi(org.eclipse.jgit.archive) = 3.2.0
Provides:	osgi(org.eclipse.jgit.java7) = 3.2.0
Provides:	osgi(org.eclipse.jgit.java7.source) = 3.2.0
Provides:	osgi(org.eclipse.jgit.source) = 3.2.0

%description
eclipse-jgit bootstrap version.

%files
/usr/share/doc/eclipse-jgit
/usr/share/doc/eclipse-jgit/LICENSE
/usr/share/doc/eclipse-jgit/README.md
/usr/share/eclipse/dropins/jgit
/usr/share/eclipse/dropins/jgit/eclipse
/usr/share/eclipse/dropins/jgit/eclipse/features
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF/maven
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit.java7
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit.java7/pom.properties
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit.java7/pom.xml
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/edl-v10.html
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/feature.properties
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/feature.xml
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.java7_3.2.0.201312181205-r/license.html
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF/maven
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit.source
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit.source/pom.properties
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit.source/pom.xml
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/edl-v10.html
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/feature.properties
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/feature.xml
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit.source_3.2.0.201312181205-r/license.html
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF/MANIFEST.MF
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF/maven
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit/pom.properties
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/META-INF/maven/org.eclipse.jgit.feature/org.eclipse.jgit/pom.xml
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/edl-v10.html
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/feature.properties
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/feature.xml
/usr/share/eclipse/dropins/jgit/eclipse/features/org.eclipse.jgit_3.2.0.201312181205-r/license.html
/usr/share/eclipse/dropins/jgit/eclipse/plugins
/usr/share/eclipse/dropins/jgit/eclipse/plugins/JavaEWAH.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/args4j.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/commons-compress.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.apache.commons.compress_1.6.0.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.eclipse.jgit-3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.eclipse.jgit.archive_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.eclipse.jgit.java7.source_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.eclipse.jgit.java7_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.eclipse.jgit.source_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/org.eclipse.jgit_3.2.0.201312181205-r.jar
/usr/share/eclipse/dropins/jgit/eclipse/plugins/xz-java.jar

#------------------------------------------------------------------------
%package	-n jgit
Version:	3.2.0
Release:	1.0
Summary:	jgit bootstrap version
Requires:	javapackages-bootstrap
Requires:	apache-commons-compress
Requires:	args4j >= 2.0.12
Requires:	java >= 1.6.0
Requires:	javaewah
Requires:	javapackages-tools
Requires:	jpackage-utils
Requires:	osgi(com.jcraft.jsch)
Requires:	xz-java >= 1.1-2
Provides:	jgit = 3.2.0-1.0:2014.0
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit) = 3.2.0.201312181205-r
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit-parent) = 3.2.0.201312181205-r
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit-parent:pom:) = 3.2.0.201312181205-r
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit.console) = 3.2.0.201312181205-r
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit.java7) = 3.2.0.201312181205-r
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit.pgm) = 3.2.0.201312181205-r
Provides:	mvn(org.eclipse.jgit:org.eclipse.jgit.ui) = 3.2.0.201312181205-r
Provides:	osgi(org.eclipse.jgit) = 3.2.0
Provides:	osgi(org.eclipse.jgit.console) = 3.2.0
Provides:	osgi(org.eclipse.jgit.java7) = 3.2.0
Provides:	osgi(org.eclipse.jgit.pgm) = 3.2.0
Provides:	osgi(org.eclipse.jgit.ui) = 3.2.0

%description	-n jgit
jgit bootstrap version.

%files		-n jgit
/usr/bin/jgit
/usr/share/doc/jgit
/usr/share/doc/jgit/LICENSE
/usr/share/doc/jgit/README.md
/usr/share/java/jgit
/usr/share/java/jgit/console.jar
/usr/share/java/jgit/java7.jar
/usr/share/java/jgit/jgit.jar
/usr/share/java/jgit/pgm.jar
/usr/share/java/jgit/ui.jar
/usr/share/maven-fragments/eclipse-jgit
/usr/share/maven-poms/JPP-jgit-parent.pom
/usr/share/maven-poms/JPP.jgit-console.pom
/usr/share/maven-poms/JPP.jgit-java7.pom
/usr/share/maven-poms/JPP.jgit-jgit.pom
/usr/share/maven-poms/JPP.jgit-pgm.pom
/usr/share/maven-poms/JPP.jgit-ui.pom

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
