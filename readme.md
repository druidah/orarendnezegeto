# Projekt célja
Egy ASP.NET alkalmazás elkészítése, ami képes útvonaltervezésre, valamint adott megállók járatsűrűségéről statisztikát készíteni.

## Fejlesztéshez
1. A SCRUM csoportok a saját águkon fejlesztenek, abból állnak ki, abba merge-elnek vissza.
2. A merge-eléshez pull requestet hozunk létre, és a SCRUM csoport minden tagját jelöljük reviewerként. A house rule-ra bízzuk, hogy mennyit vár el. A Jeskoattack csoportban úgy döntöttünk, hogy ha lehet, mindenki nézze át és approve-olja, vagy ha sürgős a fejlesztés, minimum 3 approve szükséges.
3. Új ág létrehozásánál:
   - Ha user story, akkor `story/fejlesztés-neve`, pl. `story/User-Autentikáció-implementálása`.
   - Ha altask vagy a story-n kívüli, de szükséges alapfejlesztés, akkor `task/fejlesztés-neve`, pl. `task/Solution-Létrehozása`.
   - Beszédes ágneveket használjunk, így egyszerűbb lesz átlátni. Új taskhoz vagy storyhoz új ág legyen, ne csak csoportnév-fejlesztő név.
4. A commit message legyen átlátható és beszédes, hogy később is vissza lehessen nézni, mi történt.
5. Hetente vagy ha több fejlesztés is készen van, akkor a SCRUM ágakat egyszerre összegezzük. A team leaderek indítanak pull requestet egy `nextupdate` branch-re, amit minden leader átnéz és approve-ol. Csak így kerülhet bele. A `nextupdate` azért kell, hogy a main branch-be csak tiszta, működő kód kerüljön.
6. Igyekezzünk beszédes metódus-, osztály- és változóneveket használni, ha nem dobjuk el pár sor után. Ha bármeddig megmarad egy elem (pl. class vagy metódusnév), mindenképp legyen beszédes neve. A Visual Studio segít kitölteni, csak egyszer kell begépelni.
7. Tartsuk átláthatóan a kódot, külön `.cs` fájlokba darabolva a releváns részeket. Az "egyfájlos" megoldás helyett jobb a Separation of Concerns elve szerint működni. Így például külön fájlokban kezeljük a heatmap-et, az adatbázis kezelését stb.
Egy angol fórumról egy ide vágó rész:

Here's a relevant excerpt from an English forum:
> It's pretty easy once you get the hang of it. One class per file/one file per class.  
> 
> Is there a reason they use multiple files over just one big file?  
> 
> There's absolutely tons of answers to this but the most common ones would be:
> 
> -- Easier to maintain: No one wants to look through a file that is several thousand lines long.
> 
> -- Source control for team environments: Having everyone work on one or two big files and then everyone checking in is going to be merge hell. You'd be figuring out for ages which changes should go in or not.
> 
> -- Something called the "Separation of concerns" [Wikipedia link](https://en.wikipedia.org/wiki/Separation_of_concerns). It's far easier to understand what's going on if you have files like `GameRules.cs`, `GamePlayer.cs`, `Enemy.cs`, `Board.cs` instead of one massive `Game.cs`.
> 
> -- Organizing files into folders is a good way to group functionality by purpose. For example, you could have a folder named `Database` and another named `UserInterface.WPF`, etc.

## Git segítség, ha kellene
- `git fetch`: Behúzza a repo origin-ből az ágakat, hogy lokálisan is meglegyenek.
- `git pull`: Ez originből behúzza a legfrissebb állapotot. Ha rápulloltok a változtatásaitokra, azok elvesznek... 
- GitHub-on is lehet ágat létrehozni, ami egyszerűbb.
   1. `git checkout solution-létrehozása`
   2. GitHub oldalán pull request, és kész.
- Ha egy másik SCRUM ágban van, amire szükségem van, akkor: 
   1. `git checkout solution-létrehozása`
   2. `git merge csapatnév`
   3. Kevesebb szerencsével conflict kezelés jön.
- Git config fájlba lehet írni, hogy automatikusan hozzon létre upstream branchet, ha lokálisan nincs meg.
   1. `git checkout -b task/solution-létrehozás`
   2. Kóddal végezve:
      - `git add .`
      - `git commit -m "Kész a solution, mehet a fejlesztés"`
      - `git push`
      - Ha nincs upstream: `git push --set-upstream origin task/solution-létrehozás`
