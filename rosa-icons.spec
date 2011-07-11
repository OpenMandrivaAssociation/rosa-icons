%define tarname	 rosa
%define _name    rosa
%define version	 1.0.2
%define release  %mkrel 0

Summary:	ROSA icons theme
Name:		%{_name}-icons
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.bz2
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ROSA icons theme. Designed for Mandriva. Based on the original icon theme Elementary by Daniel Fore (Dan Rabbit).

%prep
%setup -q -n %{_name}-%{version}

%install
%__rm -rf %{buildroot}
%__mkdir -p %{buildroot}%{_datadir}/icons
%__mkdir -p %{buildroot}%{_datadir}/icons/%{_name}
cp -rf ./* %{buildroot}%{_datadir}/icons/%{_name}


%files
%defattr(-,root,root)
%{_datadir}/icons/%{_name}/*

