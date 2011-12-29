# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/epsincl
# catalog-date 2008-08-19 20:15:24 +0200
# catalog-license pd
# catalog-version 0.2
Name:		texlive-epsincl
Version:	0.2
Release:	1
Summary:	Include EPS in MetaPost figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/epsincl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsincl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsincl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package facilitates including EPS files in MetaPost
figures; it makes use of (G)AWK.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/epsincl/epsincl.mp
%doc %{_texmfdistdir}/doc/metapost/epsincl/0info.txt
%doc %{_texmfdistdir}/doc/metapost/epsincl/README
%doc %{_texmfdistdir}/doc/metapost/epsincl/epsincl.awk
%doc %{_texmfdistdir}/doc/metapost/epsincl/epsincl.bat
%doc %{_texmfdistdir}/doc/metapost/epsincl/testinc0.eps
%doc %{_texmfdistdir}/doc/metapost/epsincl/testincl.bat
%doc %{_texmfdistdir}/doc/metapost/epsincl/testincl.mp
%doc %{_texmfdistdir}/doc/metapost/epsincl/testincl.sh

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
