all: doc move pack pseudo-clean

doc:
	pdflatex "Homework1Solution.tex" && pdflatex "Homework1Solution.tex"

clean: pseudo-clean
	rm -f "Homework1Solution.pdf"

pseudo-clean:
	rm -f "Homework1Solution.aux" "Homework1Solution.log" "Homework1Solution.toc"

move:
	mv "Homework1Solution.pdf" "20156441_bastien.pdf"

pack:
	zip -r 20156441_bastien.zip "20156441_bastien.pdf" problem*
