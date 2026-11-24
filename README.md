# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/framicks/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/framicks/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Tuesday, 24 November 2026, packed into a single broadsheet page. The front page leads with South Korea scrambling fighter jets after Russian military aircraft entered its air-defence zone near Ulleung island on Tuesday morning — and a false emergency text that wrongly told islanders Russian planes had violated the country's airspace. The rest of the page carries five more stories from the same day's news cycle: the World Chess Championship opening in Geneva, with defending champion Gukesh facing challenger Sindarov in Game 1; President Trump pardoning turkeys Freedom and Feathers at the White House; Jensen Huang back at Nvidia headquarters to cheering staff as the Senate Banking Committee sets a December 3 hearing; Ukraine's drone strike on the Lukoil refinery at Perm, more than 1,500 km from the border; and Armenia publishing a draft new constitution as a step towards peace with Azerbaijan. Six stories, one crowded news day, set out as a classic newspaper front page in `front-page.png`.

## Stories

1. False air-raid alert as Russian jets near Korean island (24 Nov)
2. Chess crown battle begins in Geneva (24 Nov, Game 1)
3. Trump pardons turkeys Freedom and Feathers (24 Nov)
4. Huang back at Nvidia as Senate sets hearing (board acted Monday 23 Nov; hearing set for Dec 3)
5. Ukraine hits Lukoil refinery deep in Russia (strikes overnight into Monday 23 Nov)
6. Armenia unveils new charter in peace push (draft published Monday 23 Nov)

## Run it

```sh
python3 main.py
```

This copies `front-page.png` (a real PNG, 1024×1024, under 1 MiB) to `/output/entry.png`. Set `MAKEFUN_OUTPUT_DIR` to pick a different destination. Running it twice produces byte-identical output, since the image is shipped in the repository and only copied, never redrawn. The script also re-reads the file it wrote and checks its sha256 against the shipped image before reporting success.

## Verification

You can check the output yourself in a minute. Run `python3 main.py` twice with `MAKEFUN_OUTPUT_DIR` pointed at two different folders, then compare the two `entry.png` files with `sha256sum` — both hashes should match each other and the shipped `front-page.png`, since the script only copies the image and never redraws it. The PNG itself should stay 1024×1024 pixels and under 1 MiB, which you can confirm with `file` or `identify`. If either run prints an error instead, the source image is missing, its first eight bytes are not a PNG signature, or its dimensions are not 1024×1024, and the script exits with code 1.

## Sources

Headlines were checked against reporting dated 24 November 2026: Aju Press and Reuters on the Russian aircraft entering South Korea's air-defence zone and the mistaken shelter alert; Chess.com and FIDE on Game 1 of the Gukesh–Sindarov title match in Geneva; the White House on the 2 p.m. turkey-pardon ceremony for Freedom and Feathers; Reuters, the Wall Street Journal and the Senate Banking Committee on Nvidia's reinstatement of Jensen Huang and the December 3 hearing; Ukraine's General Staff and Reuters on the Lukoil-Permnefteorgsintez refinery strike; and Reuters/AP on Armenia's draft constitution. Where an event itself fell on Monday 23 November, the story list above says so; nothing is presented as happening on a day it did not.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jjs4n5n8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
