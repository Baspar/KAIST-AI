all: doc move pack pseudo-clean

graph:
	plantuml *.uml

doc: graph
	pdflatex  --shell-escape "Homework3Solution.tex" && pdflatex --shell-escape "Homework3Solution.tex"

clean: pseudo-clean
	rm -f "20156441_bastien.pdf" "Homework3Solution.pdf" "20156441_bastien.zip"

pseudo-clean:
	rm -rf "Homework3Solution.aux" "Homework3Solution.log" "Homework3Solution.toc" "_minted-Homework3Solution" *.png

move:
	mv "Homework3Solution.pdf" "20156441_bastien.pdf"

pack:
	zip 20156441_bastien.zip "20156441_bastien.pdf"
