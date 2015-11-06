all: doc mv pack pseudo-clean

mv: 
	mv "Homework4Solution.pdf" "20156441_bastien.pdf"

doc:
	pdflatex  --shell-escape "Homework4Solution.tex" && pdflatex --shell-escape "Homework4Solution.tex"

clean: pseudo-clean
	rm -f "20156441_bastien.zip" "20156441_bastien.pdf"

pseudo-clean:
	rm -rf "Homework4Solution.aux" "Homework4Solution.log" "Homework4Solution.toc" "_minted-Homework4Solution"

pack:
	zip 20156441_bastien.zip "20156441_bastien.pdf" *.pl
