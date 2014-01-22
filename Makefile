DOCUMENT = murakami_final_report
TEX = $(DOCUMENT).tex
DVI = $(DOCUMENT).dvi
LOG = $(DOCUMENT).log
AUX = $(DOCUMENT).aux
TOC = $(DOCUMENT).toc
PDF = $(DOCUMENT).pdf

all:
	ebb image/*.jpg
	ebb image*.png
	make dvi
	dvipdfmx $(DVI)
	open $(PDF)
dvi:
	platex $(TEX)
clean:
	rm $(DVI)
	rm $(LOG)
	rm $(AUX)
	rm $(TOC)
