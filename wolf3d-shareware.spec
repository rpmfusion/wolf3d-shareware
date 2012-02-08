Name:           wolf3d-shareware
Version:        1.4
Release:        2%{?dist}
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
* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 27 2010 Hans de Goede <hdegoede@redhat.com> 1.4-1
- Initial rpmfusion package
