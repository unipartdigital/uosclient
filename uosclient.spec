%global srcname uosclient

Name:		python-%{srcname}
Version:	0.0.7
Release:	1%{?dist}
Summary:	Unipart OpenStack client tools
License:	GPLv2+
URL:		https://github.com/unipartdigital/uosclient
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm

%description
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.

%package -n	python3-%{srcname}
Summary:	%{summary}
Provides:	%{srcname} = %{version}-%{release}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.

%prep
%autosetup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/

%changelog
* Thu Feb 20 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.7-1
- network: Set default DNS TTL to 60 seconds

* Wed Feb 05 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.6-1
- network: Add tools for creating and deleting per-project networks
- port: Use project_id in place of tenant_id

* Tue Feb 04 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.5-1
- build: Fix building of RPM from a tarball

* Tue Feb 04 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.4-1
- First package built with tito
