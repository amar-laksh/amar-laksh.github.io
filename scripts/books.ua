# Experimental!

┌─╴BooksFS
  MkTempDir        ← °$"_\n" °⊸∘◌&runc {"mktemp" "-d"}
  ReadBooksFile    ← &fras $"_/books.backup"
  UnzipBackup      ← ◌◌◌&runc⊂{"unzip" "/home/amar/Downloads/Openreads-*.backup.zip" "-d"}□
  BooksFileContent ← ReadBooksFile⊸UnzipBackup MkTempDir
└─╴

┌─╴BooksJSON
  StatusIdx       ← 18
  ISBNIdx         ← 10
  TitleIdx        ← 21
  YearReadIdx     ← 4
  Replace         ← ⍜(⊜∘|≡⋅∘) ⊓⊸⦷¤
  BooksJson       ← °json $"[_]" Replace "@@@@@" BooksFS~BooksFileContent ", "
  FilterReadBooks ← ⍚(⨬("" ◌|°□⊏ [YearReadIdx TitleIdx ISBNIdx]) ⊸(=0 °□⊏ StatusIdx)) BooksJson
└─╴

≡(&p$"This is: _") ↘ 1 ◴ BooksJSON~FilterReadBooks
# &fwa "Testing.md" json FilterReadBooks
# &fwa "Testing.md" json BooksJson
