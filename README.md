https://www.udemy.com/learning-ai/learn/v4/t/lecture/6061052?start=0

- matplotlibrcの38行目の
- backend : macosx
- これを
- backend : TkAgg
- と変更させると解決できた！
- matplotlibrcの場所は，
- $python -c "import matplotlib;print(matplotlib.matplotlib_fname())"
