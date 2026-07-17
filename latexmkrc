# latexmk configuration for the One Biology Book series
$pdf_mode = 1;              # pdflatex
$out_dir = 'build';
# One entry file per book; each PDF is named after its entry file
# (build/one_biology_book_<N>_<slug>.pdf).
@default_files = (
    'one_biology_book_1_primary_middle_school.tex',
    'one_biology_book_2_high_school.tex',
    'one_biology_book_3_university_year_1.tex',
    'one_biology_book_4_university_year_2.tex',
    'one_biology_book_5_university_year_3.tex',
);
# The books' many TikZ/pgfplots figures exceed pdfTeX's default main
# memory (5M words); raise the runtime limits.
$pdflatex = 'pdflatex -cnf-line=main_memory=12000000 -cnf-line=extra_mem_top=6000000 -cnf-line=extra_mem_bot=6000000 -interaction=nonstopmode -halt-on-error %O %S';
$makeindex = 'makeindex %O -o %D %S';
