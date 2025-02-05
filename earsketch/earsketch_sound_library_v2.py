<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Sound Clips</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }
            .clip {
                margin-bottom: 10px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                cursor: pointer;
            }
            .clip h3 {
                margin: 0;
                font-size: 18px;
            }
            .clip p {
                display: none;
                font-size: 14px;
            }
            .expanded p {
                display: block;
            }
            button {
                padding: 8px 12px;
                font-size: 14px;
                cursor: pointer;
                display: block;
                margin: 10px auto;
            }
            select {
                display: block;
                margin: 10px auto;
                padding: 5px;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <h1>Sound Clips</h1>
        <label for="genreFilter">Filter by Genre:</label>
        <select id="genreFilter">
            <option value="all">All</option>
        </select>
        <label for="instrumentFilter">Filter by Instrument:</label>
        <select id="instrumentFilter">
            <option value="all">All</option>
        </select>
        <label for="artistFilter">Filter by Artist:</label>
        <select id="artistFilter">
            <option value="all">All</option>
        </select>
        <div id="soundClips"></div>
        <button id="loadMore">Load More</button>

        <script>
            let soundClips = [];
            let filteredClips = [];
            let currentIndex = 0;
            const batchSize = 50;
            const baseUrl = "https://earsketch.gatech.edu/backend-static";
            const soundClipsContainer = document.getElementById("soundClips");
            const loadMoreBtn = document.getElementById("loadMore");
            const genreFilter = document.getElementById("genreFilter");
            const instrumentFilter =
                document.getElementById("instrumentFilter");
            const artistFilter = document.getElementById("artistFilter");

            async function loadSoundData() {
                try {
                    const response = await fetch(
                        "earsketch_sound_library.json",
                    );
                    if (!response.ok) {
                        throw new Error(
                            `HTTP error! Status: ${response.status}`,
                        );
                    }
                    soundClips = await response.json();
                    populateFilters();
                    filterSoundClips();
                } catch (error) {
                    console.error("Failed to load sound data:", error);
                }
            }

            function populateFilters() {
                const genres = [
                    ...new Set(soundClips.map((clip) => clip.genre)),
                ];
                populateFilter(genreFilter, genres);

                const instruments = [
                    ...new Set(soundClips.map((clip) => clip.instrument)),
                ];
                populateFilter(instrumentFilter, instruments);

                const artists = [
                    ...new Set(soundClips.map((clip) => clip.artist)),
                ];
                populateFilter(artistFilter, artists);
            }

            function populateFilter(filterElement, options) {
                options.forEach((optionValue) => {
                    const option = document.createElement("option");
                    option.value = optionValue;
                    option.textContent = optionValue;
                    filterElement.appendChild(option);
                });
            }

            function filterSoundClips() {
                const selectedGenre = genreFilter.value;
                const selectedInstrument = instrumentFilter.value;
                const selectedArtist = artistFilter.value;

                filteredClips = soundClips.filter(
                    (clip) =>
                        (selectedGenre === "all" ||
                            clip.genre === selectedGenre) &&
                        (selectedInstrument === "all" ||
                            clip.instrument === selectedInstrument) &&
                        (selectedArtist === "all" ||
                            clip.artist === selectedArtist),
                );

                currentIndex = 0;
                soundClipsContainer.innerHTML = "";
                renderSoundClips();
            }

            function renderSoundClips() {
                let fragment = document.createDocumentFragment();
                for (
                    let i = currentIndex;
                    i <
                    Math.min(currentIndex + batchSize, filteredClips.length);
                    i++
                ) {
                    const clip = filteredClips[i];
                    const clipDiv = document.createElement("div");
                    clipDiv.className = "clip";

                    const title = document.createElement("h3");
                    title.textContent = clip.name;

                    const details = document.createElement("div");
                    details.innerHTML = `
                        <p>Artist: ${clip.artist}</p>
                        <p>Genre: ${clip.genre}</p>
                        <p>Instrument: ${clip.instrument}</p>
                        <p>Key Signature: ${clip.keySignature}</p>
                        <p>Tempo: ${clip.tempo}</p>
                        <p>Year: ${clip.year}</p>
                    `;

                    const playButton = document.createElement("audio");
                    playButton.controls = true;
                    playButton.preload = "metadata";
                    playButton.src = `${baseUrl}/${clip.path}`;

                    clipDiv.appendChild(title);
                    clipDiv.appendChild(playButton);
                    clipDiv.appendChild(details);

                    clipDiv.addEventListener("click", () => {
                        clipDiv.classList.toggle("expanded");
                    });

                    fragment.appendChild(clipDiv);
                }
                soundClipsContainer.appendChild(fragment);
                currentIndex += batchSize;

                if (currentIndex >= filteredClips.length) {
                    loadMoreBtn.style.display = "none";
                } else {
                    loadMoreBtn.style.display = "block";
                }
            }

            genreFilter.addEventListener("change", filterSoundClips);
            instrumentFilter.addEventListener("change", filterSoundClips);
            artistFilter.addEventListener("change", filterSoundClips);
            loadMoreBtn.addEventListener("click", renderSoundClips);
            loadSoundData();
        </script>
    </body>
</html>
