all: doc move pack pseudo-clean

doc:
	pdflatex  --shell-escape "Homework2Solution.tex" && pdflatex --shell-escape "Homework2Solution.tex"

clean: pseudo-clean
	rm -f "20156441_bastien.pdf" "20156441_bastien.zip"

pseudo-clean:
	rm -rf "Homework2Solution.aux" "Homework2Solution.log" "Homework2Solution.toc" "_minted-Homework2Solution"

move:
	mv "Homework2Solution.pdf" "20156441_bastien.pdf"

pack:
	zip 20156441_bastien.zip "20156441_bastien.pdf" "square.py"
