all: doc move pseudo-clean

graph:
	plantuml *.uml

doc: graph
	pdflatex  --shell-escape "Homework3Solution.tex" && pdflatex --shell-escape "Homework3Solution.tex"

clean: pseudo-clean
	rm -f "20156441_bastien.pdf" "Homework3Solution.pdf"

pseudo-clean:
	rm -rf "Homework3Solution.aux" "Homework3Solution.log" "Homework3Solution.toc" "_minted-Homework3Solution" *.png

move:
	mv "Homework3Solution.pdf" "20156441_bastien.pdf"
