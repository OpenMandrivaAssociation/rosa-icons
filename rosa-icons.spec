%define tarname	 rosa
%define _name    rosa
%define version	 1.0.27
%define release  %mkrel 1

Summary:	ROSA icons theme
Name:		%{_name}-icons
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
ROSA icon theme is high quality icon theme for KDE, GNOME and Xfce.
It is part of ROSA Theme pack - theme for ROSA Desktop distro. 
Initially based on the original icon theme Elementary by Daniel Fore
(Dan Rabbit).

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


