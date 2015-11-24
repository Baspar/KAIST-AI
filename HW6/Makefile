all: zip

zip: pack pseudo-clean

graph: graph1

graph1:
	cd problem1; plantuml graph1.uml graph2.uml; cd ..

mv:
	mv "Homework6Solution.pdf" "20156441_bastien.pdf"

doc: graph
	pdflatex  --shell-escape "Homework6Solution.tex" && pdflatex --shell-escape "Homework6Solution.tex"

clean: pseudo-clean
	rm -f "20156441_bastien.zip" "20156441_bastien.pdf" problem1/graph1.png problem1/graph2.png

pseudo-clean:
	rm -rf "Homework6Solution.aux" "Homework6Solution.log" "Homework6Solution.toc" "_minted-Homework6Solution"

pack: doc mv
	zip -r 20156441_bastien.zip "20156441_bastien.pdf" problem*
