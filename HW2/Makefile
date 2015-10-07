all: doc pack pseudo-clean

doc:
	pdflatex  --shell-escape "Homework2Solution.tex" && pdflatex --shell-escape "Homework2Solution.tex"

clean: pseudo-clean
	rm -f "Homework2Solution.pdf" "20156441_bastien.zip"

pseudo-clean:
	rm -rf "Homework2Solution.aux" "Homework2Solution.log" "Homework2Solution.toc" "_minted-Homework2Solution"

pack:
	zip 20156441_bastien.zip "Homework2Solution.pdf" "square.py"
