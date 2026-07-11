%global tl_name gmverse
%global tl_revision 29803

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.73
Release:	%{tl_revision}.1
Summary:	A package for typesetting (short) poems
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmverse
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverse.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmverse.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A redefinition of the verse environment to make the \\ command optional
for line ends and to give it a possibility of optical centering and
`right-hanging' alignment of lines broken because of length.

