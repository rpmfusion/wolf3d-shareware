Name:           wolf3d-shareware
Version:        1.4
Release:        4%{?dist}
Summary:        Wolfenstein 3D shareware Episode
Group:          Amusements/Games
License:        Shareware
URL:            http://www.3drealms.com/wolf3d/index.html
Source0:        ftp://ftp.3drealms.com/share/1wolf14.zip
Source1:        extract.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  dynamite-devel
Requires:       wolf4sdl-shareware

%description
This package contains the shareware Episode of id Software's classic
first-person shooter Wolfenstein 3D.

%prep
%setup -q -c


%build
gcc -o extract %{SOURCE1} -ldynamite
./extract W3DSW14.SHR
iconv -f CP850 -t UTF-8 vendor.doc > tmp
cat tmp | sed 's|\r||g' > vendor.doc
touch -r W3DSW14.SHR vendor.doc *.wl1


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/wolf3d/shareware
install -p -m 644 *.wl1 $RPM_BUILD_ROOT%{_datadir}/wolf3d/shareware


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc vendor.doc
%{_datadir}/wolf3d


%changelog
* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1.4-1
- Initial rpmfusion package
