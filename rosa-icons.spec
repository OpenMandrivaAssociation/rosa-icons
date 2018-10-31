%define oname rosa

Summary:	ROSA icons theme
Name:		%{oname}-icons
Version:	1.1.3
Release:	6
# https://abf.rosalinux.ru/uxteam/rosa-icons-devel
Source0:	%{name}-%{version}.tar.xz
Source1:	kdenlive-actions.tar.xz
Source2:	gnome3-devices.tar.xz
URL:		www.rosalinux.com
License:	GPLv2
Group:		Graphical desktop/Other
Patch0:		rosa-icons-1.1.3-inherits.patch
BuildArch:	noarch
BuildRequires:	fdupes
BuildRequires:	inkscape
Requires:	gnome-icon-theme

%description
ROSA icon theme is high quality icon theme for KDE, GNOME and Xfce.
It is part of ROSA theme pack - theme for ROSA Desktop distribution.
Initially based on the original icon theme Elementary by Daniel Fore
(Dan Rabbit).

%prep
%setup -q
%patch0 -p1
tar xJf %{SOURCE1}
tar xJf %{SOURCE2}

%install
mkdir -p %{buildroot}%{_datadir}/icons/%{oname}
cp -rf ./* %{buildroot}%{_datadir}/icons/%{oname}

# An ugly hack to work with Ikscape.
# TODO: Neccessary find a real problem!
cd %{buildroot}%{_datadir}/icons/%{oname}/16x16/places

for i in `ls`
do
    echo "Converting $i to plain SVG."
    inkscape -l $i $i
done
# devices icons should be converted too
cd %{buildroot}%{_datadir}/icons/%{oname}/16x16/devices
for i in `ls`
do
    echo "Converting $i to plain SVG."
    inkscape -l $i $i
done

%fdupes -s %{buildroot}%{_datadir}/icons/%{oname}

%files
%{_datadir}/icons/%{oname}/*
