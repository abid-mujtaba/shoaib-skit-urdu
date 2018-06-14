LATEX=xelatex
LATEXOPT=--shell-escape --halt-on-error
NONSTOP=--interaction=nonstopmode

LATEXMK=latexmk
LATEXMKOPT=-pdf
#CONTINUOUS=-pvc		# Used to update pdf in viewer
CONTINUOUS=


MAIN=skit
SOURCES=$(MAIN).tex urdu-prose.sty Makefile


all: show

show: $(MAIN).pdf
	vupdf $(MAIN).pdf


$(MAIN).pdf: $(MAIN).tex $(SOURCES)
		$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) -pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)

$(MAIN).tex: $(MAIN)-en.tex
		./en2urdu.py $(MAIN)-en.tex -l > $(MAIN).tex


clean:
		$(LATEXMK) -C $(MAIN)
		rm -f $(MAIN).pdfsync
		rm -rf *~ *.tmp
		rm -f *.fmt *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk
		rm -f $(MAIN).tex


.PHONY: clean all show 
# Source: https://drewsilcock.co.uk/using-make-and-latexmk
