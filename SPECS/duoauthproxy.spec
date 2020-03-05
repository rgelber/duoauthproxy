Name: duoauthproxy	
Version: 3.2.2
Release: 1%{?dist}
Summary: Duo authentication for Palo Alto GlobalProtect supports push, phone call, or passcode authentication for GlobalProtect desktop and mobile client connections using RADIUS.	

Group: Application/VPN
License: GPL

BuildRequires: gcc make python2-devel libffi-devel perl zlib-devel
Requires: gcc make python2-devel libffi-devel perl zlib-devel


%description
Duo authentication for Palo Alto GlobalProtect supports push, phone call, or passcode authentication for GlobalProtect desktop and mobile client connections using RADIUS. This configuration does not feature the interactive Duo Prompt for web-based logins. After submitting primary username and password, users automatically receive a login request via Duo Push notification to a mobile device or as a phone call.

%files
%pre -p /bin/sh
cd /tmp/
wget https://dl.duosecurity.com/%{name}-%{version}-src.tgz
tar -xvf %{name}-%{version}-src.tgz
rm -fv %{name}-%{version}-src.tgz 
cd %{name}-%{version}--src
make 
cd duoauthproxy-build
python2 install \
       --install-dir=/opt/duoauthproxy \
       --service-user=duo_authproxy_svc \
       --log-group=duo_authproxy_grp  \
       --create-init-script=yes
cd /tmp
rm -rf duoauthproxy-3.2.2--src

%postun -p /bin/sh
python2 /opt/duoauthproxy/uninstall --no-prompt
%clean 
echo "NOOP"
%changelog

