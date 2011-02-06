# TODO:
# - initscript
# - read config
# - pldize
Summary:	A Snare Log Forwarder for arbitrary text-based logs
Summary(pl.UTF-8):	Demon Snare przekazujący logi dla dowolnych tekstowych logów
Name:		snaresquid
Version:	1.2
Release:	0.1
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/snare/%{name}-%{version}.tar.gz
# Source0-md5:	d757c89e24ed354d7633893b8d607f93
URL:		http://www.intersectalliance.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Snare Log Forwarder for arbitrary text-based logs, that works with
the System iNtrusion Analysis and Reporting Environment (SNARE).

%description -l pl.UTF-8
Demon Snare przekazujący logi dla dowolnych tekstowych logów,
działający ze środowiskiem SNARE (System iNtrusion Analysis and
Reporting Environment).

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

%{__make} install \
	prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

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
# %attr(754,root,root) /etc/rc.d/init.d/snaresquid
