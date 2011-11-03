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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package facilitates including EPS files in MetaPost
figures; it makes use of (G)AWK.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
