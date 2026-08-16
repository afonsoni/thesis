# This project builds with XeLaTeX only: dissertation.sty loads fontspec and
# the bundled NewsGotT .ttf fonts, which pdflatex cannot use.
#
# pdf_mode 5 = build the PDF with xelatex.
$pdf_mode = 5;

# glossaries/acronyms: let latexmk run makeglossaries when the .acn changes.
add_cus_dep('acn', 'acr', 0, 'makeglossaries');
add_cus_dep('glo', 'gls', 0, 'makeglossaries');
sub makeglossaries {
    my ($base, $path) = fileparse($_[0]);
    my $cwd = $path eq './' ? '' : "-d $path";
    return system("makeglossaries $cwd $base");
}

# Build artifacts to clean alongside latexmk's defaults.
$clean_ext .= ' acn acr alg glg glo gls glsdefs ist synctex.gz xdv';
