Name:           wolf3d-shareware
Version:        1.4
Release:        10%{?dist}
Summary:        Wolfenstein 3D shareware Episode
Group:          Amusements/Games
License:        Shareware
URL:            http://www.3drealms.com/wolf3d/index.html
Source0:        ftp://ftp.3drealms.com/share/1wolf14.zip
Source1:        extract.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  dynamite-devel
BuildRequires:  gcc
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
* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.4-8
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.4-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1.4-1
- Initial rpmfusion package
