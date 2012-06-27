%define	_name	rosa

Summary:	ROSA icons theme
Name:		%{_name}-icons
Version:	1.0.27
Release:	1
Source0:	%{_name}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/Other
BuildArch:	noarch

%description
ROSA icon theme is high quality icon theme for KDE, GNOME and Xfce.
It is part of ROSA Theme pack - theme for ROSA Desktop distro. 
Initially based on the original icon theme Elementary by Daniel Fore
(Dan Rabbit).

%prep
%setup -q -n %{_name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/%{_name}
cp -rf ./* %{buildroot}%{_datadir}/icons/%{_name}

%files
%{_datadir}/icons/%{_name}/*
