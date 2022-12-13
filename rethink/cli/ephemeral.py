#!/usr/bin/env python3

#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import sys; sys.dont_write_bytecode = True;

import rethink


def main():
    pdf_path = "data/Elasticsearch - The Definitive Guide.pdf"
    text = rethink.preprocessors.pdf2txt.PDF(pdf_path).result()
    print(text)


if __name__ == "__main__":
    main()