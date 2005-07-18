# TODO:
# - initscript
# - read config
# - pldize
Summary:	A Snare Log Forwarder for arbitrary text-based logs
Name:		snaresquid
Version:	1.2
Release:	0.1
License:	GPL
Group:		System Environment/Daemons
######		Unknown group!
URL:		http://www.intersectalliance.com/
Source0:	http://www.intersectalliance.com/SnareText/snaresquid-%{version}.tar.gz
# Source0-md5:	8123f76405657e4595c250a3f09b15ee
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Snare Log Forwarder for arbitrary text-based logs, that works with
the System iNtrusion Analysis and Reporting Environment (SNARE).

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/init.d

%{__make} install \
	prefix=$RPM_BUILD_ROOT

%clean
rm -r $RPM_BUILD_ROOT

# %post
# chkconfig --add snaresquid
# chkconfig snaresquid on
# cat <<EOF

# Installation of SnareSquid complete.
# Please change the DESTSERVER option in /etc/init.d/snaresquid
# EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/snaresquid
# %attr(754,root,root) %{_sysconfdir}/rc.d/init.d/snaresquid
