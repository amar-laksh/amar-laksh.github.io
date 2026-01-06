# Experimental!

┌─╴Strings
  SplitAt     ← ⊜□ ⊸(¬⦷)
  ReplaceWith ← ⍜(⊜∘|≡⋅∘) ⊓⊸⦷¤
  Filter      ← /$"__" Strings~SplitAt
└─╴

┌─╴HTML
  GetImgSrc ← °□⊢Strings~SplitAt "\"" °□⊣ Strings~SplitAt "<img src="
└─╴

┌─╴FS
  Cmd           ← &runc Strings~SplitAt " "
  CmdOutput     ← °$"_\n"◌:◌Cmd
  CmdExitCode   ← ◌:⊙◌Cmd
  IndexFileName ← "./content/_index.md"
  MkTempDir     ← CmdOutput "mktemp -d"
  GetHostName   ← CmdOutput "whoami"
└─╴

┌─╴Time
  CurrentYear ← $"_"⊢datetime now
  CurrentYear ← "2025"
└─╴

┌─╴TOML
  GetValue‼ ← °□⊢Strings~SplitAt "\n" °□⊣⊜□ ⊸(¬⦷ $"_ = " ^0) (&fras ^1)
└─╴

┌─╴test
  ⍤⤙≍ {} Strings~SplitAt "hello" ""
  ⍤⤙≍ {"hello" "world"} Strings~SplitAt " " "hello world"
  ⍤⤙≍ {"hell" " w" "rld"} Strings~SplitAt "o" "hello world"
  ⍤⤙≍ {"hello worl"} Strings~SplitAt "d" "hello world"
  ⍤⤙≍ {"hello world"} Strings~SplitAt "non-existent" "hello world"

  ⍤⤙≍ "jello world" Strings~ReplaceWith "hello" "hello world" "jello"
  ⍤⤙≍ "hello world" Strings~ReplaceWith "non-existent" "hello world" "jello"
  ⍤⤙≍ 1 type FS~MkTempDir # The return type from the function should be string

  ⍤⤙≍ $"\"amar-laksh\"" TOML~GetValue‼"github" "./config.toml"
  ⍤⤙≍ $"[\"rss.xml\"]" TOML~GetValue‼"feed_filenames" "./config.toml"
  # If GetValue is passed a non existent key it returns the first line in the config file.
  ⍤⤙≍ °□ ⊢Strings~SplitAt "\n" &fras "./config.toml" TOML~GetValue‼"non-existent" "./config.toml"

  # ⍤⤙≍ (°$"_\n" ◌:◌FS~Cmd "date +%Y") Time~CurrentYear
  ⍤⤙≍ 0 FS~CmdExitCode "whoami"
└─╴
