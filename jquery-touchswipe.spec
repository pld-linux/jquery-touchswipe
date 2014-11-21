%define		plugin	touchSwipe
Summary:	A jQuery plugin for touch devices
Name:		jquery-touchswipe
Version:	1.6.6
Release:	1
License:	MIT/GPL
Group:		Applications/WWW
Source0:	https://github.com/mattbryson/TouchSwipe-Jquery-Plugin/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	98115bae96b53f2f8294fcfed87b7e54
URL:		http://labs.rampinteractive.co.uk/touchSwipe/demos/
BuildRequires:	unzip
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A jQuery plugin to be used on touch devices such as iPad, iPhone,
Android, etc.

Detects single and multiple finger swipes, pinches and falls back to
mouse 'drags' on the desktop.

Time and distance thresholds can be set to destinguish between swipe
gesture and slow drag.

Allows exclusion of child elements (interactive elements) as well
allowing page scrolling or page zooming depending on configuration.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -qc
mv TouchSwipe-Jquery-Plugin-%{version}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
