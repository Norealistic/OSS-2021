Name:       c-b19-515-4
Version:    1.0
Release:    1%{?dist}
Summary:    simple program
Group:      Testing
License:    GPL
URL:        labs by Galatsan Nikita Б19-515
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b19-515-4 c-b19-515-4.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b19-515-4 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b19-515-4-1.0-1.el8.noarch.rpm --force
%files
%{_bindir}/c-b19-515-4

%changelog
* Mon May 23 2022 Galatsan 
- Added %{_bindir}/c-b19-515-4
