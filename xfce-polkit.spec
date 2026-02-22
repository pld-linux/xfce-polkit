%define		git_ref		820497b731f95b420b4b1ced1f70e551ef5fd611
%define		ref_date	20220621
Summary:	A simple PolicyKit authentication agent for XFCE
Name:		xfce-polkit
Version:	0.3.%{ref_date}
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://github.com/ncopa/xfce-polkit/archive/%{git_ref}/%{name}-%{version}.tar.gz
# Source0-md5:	0bc28378844675aa64c5696e2db21d98
#Source0:	https://github.com/ncopa/xfce-polkit/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/ncopa/xfce-polkit
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	libxfce4ui-devel
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
Requires:	polkit-libs >= 0.97
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple PolicyKit authentication agent for XFCE.

%prep
%setup -q -n %{name}-%{git_ref}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
/etc/xdg/autostart/xfce-polkit.desktop
%attr(755,root,root) %{_prefix}/libexec/xfce-polkit
