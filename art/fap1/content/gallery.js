// Modernized Gallery Code (based on NaniMoose's original)

(function(window) {
    let ArtDB = [];
    let totalwidth = 0;
    let ArtDirectory = "";
    let ZoomedIn = 1;
    let ImgShown = -1;

    const PrevOn = "img/prev.png";
    const PrevOff = "img/prevoff.png";
    const NextOn = "img/next.png";
    const NextOff = "img/nextoff.png";
    const ZoomFull = "img/full.png";

    window.SetArtDirectory = function(n) {
        ArtDirectory = n;
    };

    window.AddArt = function(t, d, f, e) {
        const a = {
            Title: t,
            Desc: d,
            File: f,
            Ext: e,
            Thumb: f.replace(/ /g, "-").substring(0, 27),
            num: ArtDB.length,
            img: null,
            imgw: 0,
            imgh: 0
        };
        ArtDB.push(a);
    };

    window.Init = function() {
        const thumbsContainer = document.getElementById("iconrow");
        if (!thumbsContainer) {
            console.error("Thumbs container not found");
            return;
        }

        let c = '<table border="0" cellspacing="2" cellpadding="0"><tr>';
        ArtDB.forEach((a, n) => {
            c += `<td><a href="#" onclick="ShowImg(${n}); return false;" title="${a.Title}"><img src="thumb/${a.Thumb}.jpg" class="Thumb" width="64" height="96"></a></td>`;
            totalwidth += 70;
        });
        c += '</tr></table>';

        thumbsContainer.innerHTML = c;

        setTimeout(() => ShowImg(0), 100);
    };

    window.ShowImg = function(n) {
        const thumbs = document.querySelectorAll("#iconrow img");
        if (ImgShown > -1) {
            thumbs[ImgShown].className = "Thumb";
        }
        thumbs[n].className = "ThumbSel";

        updateNavButtons(n);

        const a = ArtDB[n];
        let c = `<big>${a.Title}</big><br><br>`;
        
        const displayContainer = document.getElementById("disp");
        
        if (a.Ext === "swf") {
            const sc = ScaleImage(4000, 3000);
            c += `
                <div id="flash-container" style="width:${sc.w}px;height:${sc.h}px;"></div>
                <script>
                    window.RufflePlayer = window.RufflePlayer || {};
                    window.addEventListener("load", (event) => {
                        const ruffle = window.RufflePlayer.newest();
                        const player = ruffle.createPlayer();
                        const container = document.getElementById("flash-container");
                        container.appendChild(player);
                        player.load("${ArtDirectory}${a.File}.swf");
                    });
                </script>
            `;
        } else {
            const imgSrc = `${ArtDirectory}${a.File}.${a.Ext}`;
            if (a.imgw > 0 && ZoomedIn !== 1) {
                const sc = ScaleImage(a.imgw, a.imgh);
                c += `<img src="${imgSrc}" width="${sc.w}" height="${sc.h}" border="2">`;
            } else {
                c += `<img src="${imgSrc}" onload="ResizeImg(${n})" border="2">`;
            }
        }
        
        c += `<br>${a.Desc}<br><br>`;
        displayContainer.innerHTML = c;
        ImgShown = n;

        PrebufferImg(n + 1);
        PrebufferImg(n - 1);
    };

    function updateNavButtons(n) {
        const prevButton = document.getElementById("prevButton");
        const nextButton = document.getElementById("nextButton");
        const zoomButton = document.getElementById("zoomButton");

        prevButton.src = n > 0 ? PrevOn : PrevOff;
        nextButton.src = n < ArtDB.length - 1 ? NextOn : NextOff;
        zoomButton.src = ZoomFull;
        zoomButton.onclick = () => openFullImage(n);
    }

    window.DoNext = function() {
        if (ImgShown + 1 < ArtDB.length) {
            ShowImg(ImgShown + 1);
            CenterThumbs();
        }
    };

    window.DoPrev = function() {
        if (ImgShown - 1 > -1) {
            ShowImg(ImgShown - 1);
            CenterThumbs();
        }
    };

    function openFullImage(n) {
        const a = ArtDB[n];
        const imgSrc = `${ArtDirectory}${a.File}.${a.Ext}`;
        window.open(imgSrc, '_blank');
    }

    function PrebufferImg(n) {
        if (n < 0 || n >= ArtDB.length) return;
        const a = ArtDB[n];
        if (a.imgw > 0) return;
        const img = new Image();
        img.src = `${ArtDirectory}${a.File}.${a.Ext}`;
        img.onload = () => {
            a.imgw = img.naturalWidth;
            a.imgh = img.naturalHeight;
        };
    }

    function CenterThumbs() {
        const thumbsContainer = document.getElementById("iconrow");
        const w = thumbsContainer.offsetWidth;
        const x = Math.floor((totalwidth * ImgShown / ArtDB.length) - (w / 2));
        thumbsContainer.scrollLeft = Math.max(0, x);
    }

    // Initialize the gallery when the DOM is fully loaded
    document.addEventListener("DOMContentLoaded", window.Init);

})(window);