# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/gmverse
# catalog-date 2012-05-17 22:49:03 +0200
# catalog-license lppl
# catalog-version v0.73
Name:		texlive-gmverse
Version:	v0.73
Release:	9
Summary:	A package for typesetting (short) poems
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmverse
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverse.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverse.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A redefinition of the verse environment to make the \\ command
optional for line ends and to give it a possibility of optical
centering and `right-hanging' alignment of lines broken because
of length.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmverse/gmverse.sty
%doc %{_texmfdistdir}/doc/latex/gmverse/README
%doc %{_texmfdistdir}/doc/latex/gmverse/gmverse.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
