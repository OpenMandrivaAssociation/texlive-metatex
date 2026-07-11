%global tl_name metatex
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Incorporate Metafont pictures in TeX source
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/metatex
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metatex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metatex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
METATeX is a set of plain TeX and Metafont macros that you can use to
define both the text and the figures in a single source file. Because
METATeX sets up two way communication, from TeX to Metafont and back
from Metafont to TeX, drawing dimensions can be controlled by TeX and
labels can be located by Metafont. Only standard features of TeX and
Metafont are used, but two runs of TeX and one of Metafont are needed.

