%define beta b2

Name:		python-sphinx_theme_builder
Version:	0.2.0
Release:	%{?beta:0.%{beta}.}1
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_theme_builder/sphinx-theme-builder-%{version}%{?beta:%{beta}}.tar.gz
Summary:	A tool for authoring Sphinx themes with a simple (opinionated) workflow.
URL:		https://pypi.org/project/sphinx_theme_builder/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A tool for authoring Sphinx themes with a simple (opinionated) workflow.

%prep
%autosetup -p1 -n sphinx-theme-builder-%{version}%{?beta:%{beta}}

%build
%py_build

%install
%py_install

%files
%{_bindir}/stb
%{py_sitedir}/sphinx_theme_builder
%{py_sitedir}/sphinx_theme_builder-*.*-info
