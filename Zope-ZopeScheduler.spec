%define		zope_subname	ZopeScheduler
Summary:	Cron like service for Zope
Summary(pl):	Produkt dla Zope pomocny przy wywo³ywaniu okresowych zadañ
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://dev.legco.biz/downloads/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	0dfcd5fa753a499b7e9f294971971f40
URL:		http://dev.legco.biz/products/ZopeScheduler/
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-TimerService
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZopeScheduler - Cron like service for Zope.

%description -l pl
ZopeScheduler jest produktem dla Zope pomocnym przy wywo³ywaniu
okresowych zadañ.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af %{zope_subname}/{Extensions,skins,zpt,*.py,refresh.txt,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
for p in ZopeScheduler ; do
        /usr/sbin/installzopeproduct %{_datadir}/%{name}/$p
done
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
        for p in ZopeScheduler ; do
                /usr/sbin/installzopeproduct -d $p
        done
	if [ -f /var/lock/subsys/zope ]; then
            /etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/{README.txt,CREDITS.txt}
%{_datadir}/%{name}
