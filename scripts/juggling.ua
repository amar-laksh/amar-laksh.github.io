# Experimental!

┌─╴Juggling
  ┌─╴Gif
    GrepGifURL         ← □$"_&_" °$"_&amp;_" ⊂°$"_/download_"°□⊣⊢ regex ".*img src=.(.*=media)"
    FetchAnimationPage ← GrepGifURL ⊏ 1 □₃&runc⊂{"curl" "-s"} □$"https://jugglinglab.org/anim?_"
    Save               ← |1.0 ◌◌◌&runc ⊂{"curl" "-s" "--output"} ⇌⊂⊓(∘|□$"./static/images/juggling/_.gif") FetchAnimationPage.
  └─╴
  IndexFileName          ← "./content/_index.md"
  ToPatternMarkdown      ← $"[![thumbnail of siteswap pattern: _](images/juggling/_.gif)](https://jugglinglab.org/anim?_)"..
  AppendToJugglingBlock  ← $"<juggling>\n\n_\n_\n\n</juggling>"
  SearchAndAppendPattern ← ⍜regex≡(AppendToJugglingBlock ⊓(°□⊏1|°□)) "(?m)^<juggling>\n\n((.*|\n)*)\n\n</juggling>$"
  UpdatePattern          ← ⍜&fras(SearchAndAppendPattern) IndexFileName
  PatternExists          ← /↥˜⌕ &fras IndexFileName⊸ToPatternMarkdown
  AddNewPatterns         ← |1.0 ⍚(⨬(&p $"Pattern _ updated"⊸⊃(UpdatePattern□ToPatternMarkdown|Gif~Save)|&p $"Pattern _ already exists") PatternExists)
└─╴

# Add new known patterns here
Juggling~AddNewPatterns {"3" "40" "(2x,2x)*" "4"}
