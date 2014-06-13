%define tarname	rosa
%define _name	rosa
%define version	1.0.33
%define release	8

Summary:	ROSA icons theme
Name:		%{_name}-icons
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.xz
Source1:	mdvbutton.svg
Source2:	drakconf32.svg
Source3:	drakconf48.svg
Source4:	drakconf64.svg
URL:		www.rosalinux.com
License:	GPLv2
Group:		Graphical desktop/Other
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
%setup -q -n %{_name}-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/icons/%{_name}
cp -rf ./* %{buildroot}%{_datadir}/icons/%{_name}

# An ugly hack to work with Ikscape.
# TODO: Neccessary find a real problem!
cd %{buildroot}%{_datadir}/icons/%{_name}/places/16

for i in `ls`
do
    echo "Converting $i to plain SVG."
    inkscape -l $i $i
done
# devices icons should be converted too
cd %{buildroot}%{_datadir}/icons/%{_name}/devices/16
for i in `ls`
do
    echo "Converting $i to plain SVG."
    inkscape -l $i $i
done

# replace the rosa icon with open mandriva
for i in 22 24 32 48 64 128; do
        cp %{SOURCE1} %{buildroot}%{_iconsdir}/%{_name}/places/${i}/start-here.svg ;
done

cp -f %{SOURCE2} %{buildroot}%{_iconsdir}/rosa/categories/32/drakconf.svg
cp -f %{SOURCE3} %{buildroot}%{_iconsdir}/rosa/categories/48/drakconf.svg
cp -f %{SOURCE4} %{buildroot}%{_iconsdir}/rosa/categories/64/drakconf.svg

%fdupes -s %{buildroot}%{_datadir}/icons/%{_name}

%files
%{_datadir}/icons/%{_name}/*
