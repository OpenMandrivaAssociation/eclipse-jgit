%global eclipse_base   %{_libdir}/eclipse
%global install_loc    %{_datadir}/eclipse/dropins/jgit

Name:           eclipse-jgit
Version:        0.11.3
Release:        1
Summary:        Eclipse JGit

Group:          Development/Java
License:        BSD
URL:            http://www.eclipse.org/egit/
#Fetched from http://egit.eclipse.org/w/?p=jgit.git;a=snapshot;h=v0.11.3;sf=tbz2
Source0:        jgit-v0.11.3.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: java-devel
BuildRequires: eclipse-pde >= 0:3.4.0
Requires: eclipse-platform >= 3.5.0

%description
A pure Java implementation of the Git version control system.

%prep
%setup -n eclipse-jgit -q -c

%build
%{eclipse_base}/buildscripts/pdebuild -f org.eclipse.jgit

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.jgit.zip 

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc jgit/LICENSE 
%doc jgit/README
%{install_loc}

