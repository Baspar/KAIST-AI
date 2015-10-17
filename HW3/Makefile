all: graph doc move pseudo-clean

graph: Backward.uml

doc:
	pdflatex  --shell-escape "Homework3Solution.tex" && pdflatex --shell-escape "Homework3Solution.tex"

%.uml:
	plantuml $@

clean: pseudo-clean
	rm -f "20156441_bastien.pdf" "Homework3Solution.pdf"

pseudo-clean:
	rm -rf "Homework3Solution.aux" "Homework3Solution.log" "Homework3Solution.toc" "_minted-Homework3Solution" *.png

move:
	mv "Homework3Solution.pdf" "20156441_bastien.pdf"
