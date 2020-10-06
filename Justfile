build-and_sync: build sync
    echo "Done."

build:
    rm metadata.tex
    cat metadata.json | python3 json2tex.py metadata > metadata.tex
    latexmk -e '$pdflatex=q/pdflatex %O -shell-escape %S/' -pdf thesis.tex

sync:
    cp thesis.pdf ~/Dropbox/Thesis

clean:
    latexmk -C
