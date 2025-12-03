# Experimental!

JugglingFileName ← "./content/_index.md"

IndexFileString     ← &fras JugglingFileName
SaveJugglingGif     ← $"https://jugglinglab.org/anim?_"
MkPatternHyperLink  ← $"[![thumbnail of siteswap pattern: _](images/juggling/_.gif)](https://jugglinglab.org/anim?_)\n"..
AddJugglingPattern! ← ⊃(SaveJugglingGif ^0|&fwa JugglingFileName (⍜regex≡($"<juggling>\n_\n</juggling>" ˜⊂MkPatternHyperLink ^0°□⊏ 1) "(?m)^<juggling>\n((.|\n)*)\n</juggling>$" IndexFileString))

AddJugglingPattern!("4")
