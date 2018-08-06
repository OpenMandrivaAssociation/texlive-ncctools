# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ncctools
# catalog-date 2008-02-08 09:08:04 +0100
# catalog-license lppl
# catalog-version 3.5
Name:		texlive-ncctools
Version:	3.5.2
Release:	1
Summary:	A collection of general packages for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ncctools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ncctools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ncctools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ncctools.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The NCCtools bundle contains many packages for general use
under LaTeX; many are also used by NCC LaTeX. The bundle
includes tools for: - executing commands after a package is
loaded; - watermarks; - counter manipulation (dynamic counters,
changing counter numbering with another counter); -
improvements to the description environment; - hyphenation of
compound words; - new levels of footnotes; - space-filling
patterns; - "poor man's" Black Board Bold symbols; - alignment
of the content of a box; - use comma as decimal separator; -
boxes with their own crop marks; - page cropmarks; -
improvements to fancy headers; - float "styles", mini floats,
side floats; - manually marked footnotes; - extension of
amsmath; - control of paragraph skip; - an envelope to the
graphicx package; - dashed and multiple rules; - alternative
techniques for declarations of sections, captions, and toc-
entries; - generalised text-stretching; - generation of new
theorem-like environments; - control of the text area; -
centred page layouts; and - an un-numbered top-level section.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ncctools/afterpackage.sty
%{_texmfdistdir}/tex/latex/ncctools/dcounter.sty
%{_texmfdistdir}/tex/latex/ncctools/desclist.sty
%{_texmfdistdir}/tex/latex/ncctools/extdash.sty
%{_texmfdistdir}/tex/latex/ncctools/manyfoot.sty
%{_texmfdistdir}/tex/latex/ncctools/mboxfill.sty
%{_texmfdistdir}/tex/latex/ncctools/nccbbb.sty
%{_texmfdistdir}/tex/latex/ncctools/nccboxes.sty
%{_texmfdistdir}/tex/latex/ncctools/ncccomma.sty
%{_texmfdistdir}/tex/latex/ncctools/ncccropbox.sty
%{_texmfdistdir}/tex/latex/ncctools/ncccropmark.sty
%{_texmfdistdir}/tex/latex/ncctools/nccfancyhdr.sty
%{_texmfdistdir}/tex/latex/ncctools/nccfloats.sty
%{_texmfdistdir}/tex/latex/ncctools/nccfoots.sty
%{_texmfdistdir}/tex/latex/ncctools/nccmath.sty
%{_texmfdistdir}/tex/latex/ncctools/nccparskip.sty
%{_texmfdistdir}/tex/latex/ncctools/nccpic.sty
%{_texmfdistdir}/tex/latex/ncctools/nccrules.sty
%{_texmfdistdir}/tex/latex/ncctools/nccsect.sty
%{_texmfdistdir}/tex/latex/ncctools/nccstretch.sty
%{_texmfdistdir}/tex/latex/ncctools/nccthm.sty
%{_texmfdistdir}/tex/latex/ncctools/textarea.sty
%{_texmfdistdir}/tex/latex/ncctools/tocenter.sty
%{_texmfdistdir}/tex/latex/ncctools/topsection.sty
%{_texmfdistdir}/tex/latex/ncctools/watermark.sty
%doc %{_texmfdistdir}/doc/latex/ncctools/README
%doc %{_texmfdistdir}/doc/latex/ncctools/README.source
%doc %{_texmfdistdir}/doc/latex/ncctools/afterpackage.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/changes.txt
%doc %{_texmfdistdir}/doc/latex/ncctools/dcounter.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/desclist.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/extdash.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/manifest.txt
%doc %{_texmfdistdir}/doc/latex/ncctools/manyfoot.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/mboxfill.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccbbb.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccboxes.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/ncccomma.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/ncccropbox.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/ncccropmark.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccfancyhdr.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccfloats.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccfoots.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccmath.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccparskip.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccpic.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccrules.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccsect.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccstretch.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/nccthm.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/ncctools.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/ncctools.tex
%doc %{_texmfdistdir}/doc/latex/ncctools/textarea.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/tocenter.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/topsection.pdf
%doc %{_texmfdistdir}/doc/latex/ncctools/watermark.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ncctools/afterpackage.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/dcounter.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/desclist.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/extdash.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/manyfoot.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/mboxfill.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccbbb.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccboxes.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/ncccomma.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/ncccropbox.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/ncccropmark.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccfancyhdr.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccfloats.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccfoots.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccmath.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccparskip.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccpic.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccrules.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccsect.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccstretch.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/nccthm.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/ncctools.ins
%doc %{_texmfdistdir}/source/latex/ncctools/textarea.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/tocenter.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/topsection.dtx
%doc %{_texmfdistdir}/source/latex/ncctools/watermark.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.5-2
+ Revision: 754252
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.5-1
+ Revision: 719105
- texlive-ncctools
- texlive-ncctools
- texlive-ncctools
- texlive-ncctools

