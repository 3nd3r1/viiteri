# Viljamin Vaatismusmäärittely

## Yleistä

-   Nimi: Viiteri
-   Koodi: Python
-   Package manager: poetry
-   Dokumentaatio: Suomeksi
-   Koodin kieli: englanniksi
-   Checkstyle: pylint

## Rakenne

![Folder Structure](./folder_structure.png)

Inspiraatio: [github.com/tehtavat/viikko3/web-login](https://github.com/ohjelmistotuotanto-hy/tehtavat/blob/main/viikko3/web-login)

### Huomioita

-   Kaikki viittaukset muodossa:

    `import Reference from viiteri.entities.reference`

-   Kaikki nimet snake_case

## Testaus

-   Yksikkötestaus: unittest
-   Integraatiotestaus: robot
-   Tulevaisuudessa kaikkien user storyjen hyväksymiskriteerit kirjoitetaan robot formaatissa

## Devaus ohjeita

-   Jokaiselle taskille tai spikelle oma branch, joka myöhemmin mergetään trunkkiin pull requestillä
-   Taskeissä täytyy olla estimoitu työmäärä ja aktuaalinen työmäärä
-   Muistakaa tehdä pull requestit, jotka on linkitetty taskien issueihin
-   Muistakaa merkata itsenne task-issuen assigneeksi
