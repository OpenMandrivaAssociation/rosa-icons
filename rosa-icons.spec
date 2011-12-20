%define tarname	 rosa
%define _name    rosa
%define version	 1.0.11
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



%changelog
* Fri Aug 12 2011 Denis Koryavov <dkoryavov@mandriva.org> 1.0.6-1mdv2011.0
+ Revision: 694145
- Changed icon for Kickoff, Shotwell and folders Music and Images.

* Mon Aug 08 2011 Denis Koryavov <dkoryavov@mandriva.org> 1.0.4-1
+ Revision: 693650
- New version. Fixed some cursors.

* Mon Jul 25 2011 Alex Burmashev <burmashev@mandriva.org> 1.0.3-1
+ Revision: 691577
- New cursor theme

* Tue Jul 12 2011 Denis Koryavov <dkoryavov@mandriva.org> 1.0.3-0
+ Revision: 689684
- Completely fixed problem with GTK+ dialogs. Changed size for Email and instant messenger icons.

* Mon Jul 11 2011 Denis Koryavov <dkoryavov@mandriva.org> 1.0.2-0
+ Revision: 689523
- Added some new icons to the places for solving some problems with GTK-open dialog and Mozilla products

* Mon Jun 27 2011 Alex Burmashev <burmashev@mandriva.org> 1.0.1-0
+ Revision: 687431
- theme update

* Fri Jun 24 2011 Alex Burmashev <burmashev@mandriva.org> 1.0.0-0
+ Revision: 686899
- import rosa-icons

