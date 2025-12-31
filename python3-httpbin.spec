#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	HTTP Request and Response Service
Summary(pl.UTF-8):	Usługa żądań i odpowiedzi HTTP
Name:		python3-httpbin
Version:	0.10.2
Release:	1
License:	ISC or MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/httpbin
Source0:	https://files.pythonhosted.org/packages/source/h/httpbin/httpbin-%{version}.tar.gz
# Source0-md5:	f7eefe44907a031db3322832945c4349
URL:		https://github.com/Runscope/httpbin
%if %(locale -a | grep -q '^C\.UTF-8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-brotlicffi
BuildRequires:	python3-decorator
BuildRequires:	python3-flasgger
BuildRequires:	python3-flask >= 2.2.4
BuildRequires:	python3-greenlet
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-importlib_metadata
%endif
BuildRequires:	python3-six
BuildRequires:	python3-werkzeug >= 2.2.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP Request and Response Service.

%description -l pl.UTF-8
Usługa żądań i odpowiedzi HTTP.

%prep
%setup -q -n httpbin-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE LICENSE.ISC LICENSE.MIT README.md
%{py3_sitescriptdir}/httpbin
%{py3_sitescriptdir}/httpbin-%{version}.dist-info
