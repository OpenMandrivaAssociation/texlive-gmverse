# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gmverse
# catalog-date 2008-09-06 11:23:59 +0200
# catalog-license lppl
# catalog-version v0.73
Name:		texlive-gmverse
Version:	v0.73
Release:	1
Summary:	a package for typesetting (short) poems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmverse
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverse.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverse.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A redefinition of the verse environment to make the \\ command
optional for line ends and to give it a possibility of optical
centering and `right-hanging' alignment of lines broken because
of length.

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
%{_texmfdistdir}/tex/latex/gmverse/gmverse.sty
%doc %{_texmfdistdir}/doc/latex/gmverse/README
%doc %{_texmfdistdir}/doc/latex/gmverse/gmverse.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
