all: doc pack pseudo-clean

doc:
	pdflatex  --shell-escape "Homework4Solution.tex" && pdflatex --shell-escape "Homework4Solution.tex"

clean: pseudo-clean
	rm -f "Homework4Solution.pdf" "20156441_bastien.zip"

pseudo-clean:
	rm -rf "Homework4Solution.aux" "Homework4Solution.log" "Homework4Solution.toc" "_minted-Homework4Solution"

pack:
	zip 20156441_bastien.zip "Homework4Solution.pdf"
