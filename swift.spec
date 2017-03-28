Name:	swift
Version:	3.1
Release:	1%{?dist}
Summary:	The Swift Programming Language
URL:	https://swift.org/

License:	Apache License 2.0
Source0:	https://github.com/apple/%{name}/archive/%{name}-%{version}-RELEASE.tar.gz

BuildRequires:	git
BuildRequires:	cmake
BuildRequires:	ninja-build
BuildRequires:	clang
BuildRequires:	python
BuildRequires:	uuid-devel
BuildRequires:	libicu-devel
BuildRequires:	libbsd-devel
BuildRequires:	libedit-devel
BuildRequires:	libxml2-devel
BuildRequires:	libsqlite3x-devel
BuildRequires:	swig
#BuildRequires:	python-libs
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-compat-libs
BuildRequires:	pkgconfig
BuildRequires:	libcurl-devel
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	systemtap-sdt-devel

# uuid-dev libicu-dev icu-devtools libbsd-dev libedit-dev libxml2-dev libsqlite3-dev swig libpython-dev libncurses5-dev pkg-config libblocksruntime-dev libcurl4-openssl-dev autoconf libtool systemtap-sdt-dev

%description
The Swift Programming Language

%prep
%setup -q -n swift-swift-3.1-RELEASE
./utils/update-checkout --clone 

%build
./utils/build-script -r -t

%install

%files

%changelog

