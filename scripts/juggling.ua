# Experimental!

~ "lib/lib.ua" ~ FS HTML Strings TOML

┌─╴Juggling
  ┌─╴Gif
    FixImgUrl          ← ∧(Strings~Filter°□) {"amp;" "/download"}
    FetchAnimationPage ← ◌⨬(:|&ep "Failed to fetch animation image") FS~Cmd $"curl -s https://jugglinglab.org/anim?_"
    Save               ← ◌◌◌FS~Cmd $"curl -s --output ./static/images/juggling/_.gif _" :⊸(FixImgUrl HTML~GetImgSrc FetchAnimationPage)
  └─╴
  IndexFileName          ← "./content/_index.md"
  ToPatternMarkdown      ← $"[![thumbnail of siteswap pattern: _](images/juggling/_.gif)](https://jugglinglab.org/anim?_)"..
  AppendToJugglingBlock  ← $"<juggling>\n\n_\n_\n\n</juggling>"
  SearchAndAppendPattern ← ⍜regex≡(AppendToJugglingBlock ⊓(°□⊏1|°□)) "(?m)^<juggling>\n\n((.*|\n)*)\n\n</juggling>$"
  UpdatePattern          ← ⍜&fras(SearchAndAppendPattern) IndexFileName□ToPatternMarkdown
  DoesPatternExists      ← /≠˜⌕ &fras IndexFileName⊸ToPatternMarkdown
  AddNewPatterns         ← |1.0 ⍚(⨬(&p $"> Pattern _ updated"⊸⊃(UpdatePattern|Gif~Save)|&p $"> Pattern _ already exists") DoesPatternExists)
└─╴

Juggling~AddNewPatterns (°json TOML~GetValue‼"known_site_swaps" "./config.toml")

┌─╴test
  ⍤⤙≍ {0 "42"} □₂Juggling~DoesPatternExists "42"
  ⍤⤙≍ {1 "3"} □₂Juggling~DoesPatternExists "3"
└─╴
