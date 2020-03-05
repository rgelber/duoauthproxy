Name: duoauthproxy	
Version: 3.2.2
Release: 1%{?dist}
Summary: Duo authentication for Palo Alto GlobalProtect supports push, phone call, or passcode authentication for GlobalProtect desktop and mobile client connections using RADIUS.	

Group: Application/VPN
License: GPL
URL: https://www.duo.com	
Source0: https://dl.duosecurity.com/duoauthproxy-latest-src.tgz

BuildRequires: gcc make python2-devel libffi-devel perl zlib-devel
Requires: gcc make python2-devel libffi-devel perl zlib-devel


%description
Duo authentication for Palo Alto GlobalProtect supports push, phone call, or passcode authentication for GlobalProtect desktop and mobile client connections using RADIUS. This configuration does not feature the interactive Duo Prompt for web-based logins. After submitting primary username and password, users automatically receive a login request via Duo Push notification to a mobile device or as a phone call.

%prep
%setup -q -n %{name}-%{version}--src


%build
make 

%install
python2 duoauthproxy-build/install \
       --install-dir=%{buildroot}/opt/duoauthproxy \
       --service-user=duo_authproxy_svc \
       --log-group=duo_authproxy_grp  \
       --create-init-script=yes

# Specify Python Version and Fix Installation Paths from Installer
LIST=$(grep -RI '%{buildroot}' %{buildroot} | awk -F':' '{print $1}')
for i in $LIST; do 
    sed "s|%{buildroot}||g" -i "${i}"
done

LIST=$(grep -RI '#!/usr/bin/env python' %{buildroot} | awk -F':' '{print $1}')
for i in $LIST; do 
    sed 's|#!/usr/bin/env python|#!/usr/bin/env python2|g' -i "${i}"
done

LIST=$(grep -RI '#!/usr/bin/python' %{buildroot} | awk -F':' '{print $1}')
for i in $LIST; do 
    sed 's|#!/usr/bin/python|#!/usr/bin/python2|g' -i "${i}"
done


%clean
echo "NOOP"

%files
/opt/duoauthproxy
/opt/duoauthproxy*

%changelog

