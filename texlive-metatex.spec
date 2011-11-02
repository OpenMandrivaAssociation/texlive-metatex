Name:		texlive-metatex
Version:	1.1
Release:	1
Summary:	Incorporate MetaFont pictures in TeX source
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/metatex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metatex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
METATeX is a set of plain TeX and MetaFont macros that you can
use to define both the text and the figures in a single source
file. Because METATeX sets up two way communication, from TeX
to MetaFont and back from MetaFont to TeX, drawing dimensions
can be controlled by TeX and labels can be located by MetaFont.
Only standard features of TeX and MetaFont are used, but two
runs of TeX and one of MetaFont are needed.

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
%{_texmfdistdir}/tex/plain/metatex/metatex.tex
%doc %{_texmfdistdir}/doc/plain/metatex/README
%doc %{_texmfdistdir}/doc/plain/metatex/gpl.txt
%doc %{_texmfdistdir}/doc/plain/metatex/mtmp2pdf.tex
%doc %{_texmfdistdir}/doc/plain/metatex/mtpaper.pdf
%doc %{_texmfdistdir}/doc/plain/metatex/mtpaper/delay.mf
%doc %{_texmfdistdir}/doc/plain/metatex/mtpaper/diagram.tex
%doc %{_texmfdistdir}/doc/plain/metatex/mtpaper/frame.tex
%doc %{_texmfdistdir}/doc/plain/metatex/mtpaper/mtpaper.tex
%doc %{_texmfdistdir}/doc/plain/metatex/mtpaper/shadow.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
