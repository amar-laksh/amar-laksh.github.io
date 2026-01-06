# Experimental!

~ "lib/lib.ua" ~ FS HTML Strings TOML Time

┌─╴Books
  IdIdx       ← 9
  ISBNIdx     ← 10
  DateReadIdx ← 17
  StatusIdx   ← 18
  TitleIdx    ← 21
  ┌─╴Backup
    CopyBookThumbnails ← ◌◌◌FS~Cmd $"cp _/_.jpg ./static/images/books/_.jpg" ::⊙(.⊏ 1)
    UnzippedDir        ← ⟜(◌FS~CmdExitCode $"unzip -d _ _/Openreads-*.backup.zip") FS~MkTempDir (°json TOML~GetValue‼"feeds_directory" "./config.toml")
    PathWithJson       ← □⟜(°json $"[_]" (Strings~ReplaceWith "@@@@@" (:", " &fras $"_/books.backup"))) UnzippedDir
  └─╴
  ToBookMarkdown   ← $"[![thumbnail of _](images/books/_.jpg)](https://isbnsearch.org/isbn/_)" °⊟₃
  CurrentYearMask  ← =(□$"|_"Time~CurrentYear) □⍣(↙5)∘ °□⊢
  CurrentYearBooks ← ▽=1 ≡(⊃(CurrentYearMask|↘ 1)°□) ⍚(⊏ [DateReadIdx TitleIdx IdIdx ISBNIdx])
  IndexFileContent ← &fras FS~IndexFileName
  DoesBookExists   ← /≠˜⌕ IndexFileContent⊸ToBookMarkdown
  AddNewBook       ← ⊃(|Backup~CopyBookThumbnails)
  AddNewBooks      ← ⍚(⨬(&p $"> Book added:\t\t\"_\"" ⊢⊸AddNewBook|&p $"> Book already exists:\t\"_\""⊢◌) :⊙DoesBookExists) ⊙CurrentYearBooks Backup~PathWithJson
└─╴

Books~AddNewBooks
