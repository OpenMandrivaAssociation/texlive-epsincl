Name:		texlive-epsincl
Version:	29349
Release:	2
Summary:	Include EPS in MetaPost figures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/epsincl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsincl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epsincl.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
