all: zip

zip: pack pseudo-clean

graph: graph1 graph2

graph1:
	cd problem1; plantuml graph.uml; cd ..

graph2:
	cd problem2; ./genTree.sh; plantuml graph.uml; cd ..

mv:
	mv "Homework5Solution.pdf" "20156441_bastien.pdf"

doc: graph
	pdflatex  --shell-escape "Homework5Solution.tex" && pdflatex --shell-escape "Homework5Solution.tex"

clean: pseudo-clean
	rm -f "20156441_bastien.zip" "20156441_bastien.pdf" problem2/graph.* problem1/graph.png

pseudo-clean:
	rm -rf "Homework5Solution.aux" "Homework5Solution.log" "Homework5Solution.toc" "_minted-Homework5Solution"

pack: doc mv
	zip -r 20156441_bastien.zip "20156441_bastien.pdf" problem*
