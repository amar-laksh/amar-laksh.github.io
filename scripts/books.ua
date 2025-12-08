# Experimental!

MkTempDir     ← °$"_\n" °⊸∘◌&runc {"mktemp" "-d"}
ExtractBooks  ← &fras $"_/books.backup"
ExtractBackup ← ◌◌◌&runc⊂{"unzip" "/home/amar/Downloads/Openreads-2025_12_11-0_56_13.backup.zip" "-d"}□
GetBooks      ← ExtractBooks⊸ExtractBackup MkTempDir

# °json GetBooks
