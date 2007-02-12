%define		zope_subname	ZopeScheduler
Summary:	Cron like service for Zope
Summary(pl.UTF-8):   Produkt dla Zope pomocny przy wywoływaniu okresowych zadań
Name:		Zope-%{zope_subname}
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dev.legco.biz/downloads/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	0dfcd5fa753a499b7e9f294971971f40
URL:		http://dev.legco.biz/products/ZopeScheduler/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope
Requires:	Zope-TimerService
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZopeScheduler - Cron like service for Zope.

%description -l pl.UTF-8
ZopeScheduler jest produktem dla Zope pomocnym przy wywoływaniu
okresowych zadań.

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
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/{README.txt,CREDITS.txt}
%{_datadir}/%{name}
