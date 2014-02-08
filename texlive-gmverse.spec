# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gmverse
# catalog-date 2008-09-06 11:23:59 +0200
# catalog-license lppl
# catalog-version v0.73
Name:		texlive-gmverse
Version:	v0.73
Release:	3
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.73-2
+ Revision: 752365
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.73-1
+ Revision: 718569
- texlive-gmverse
- texlive-gmverse
- texlive-gmverse
- texlive-gmverse

