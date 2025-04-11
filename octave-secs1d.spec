%define octpkg secs1d

Summary:	A Drift-Diffusion simulator for 1d semiconductor devices with Octave
Name:		octave-%{octpkg}
Version:	0.0.9
Release:	2
Url:		https://packages.octave.org/%{octpkg}/
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.0
BuildRequires:	octave-bim

Requires:	octave(api) = %{octave_api}
Requires:	octave-bim

Requires(post): octave
Requires(postun): octave

%description
A Drift-Diffusion simulator for 1d semiconductor devices with Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

