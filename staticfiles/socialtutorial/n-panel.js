document.addEventListener("keydown", keyDown, false);

var nopen = false;
var topen = false;
//-----------------------Get keypresses-----------------------
function keyDown(e) {
    var keyCode = e.keyCode;
    clog(document.activeElement.tagName);
    if (
        document.activeElement.tagName != "TEXTAREA" && document.activeElement.tagName != "INPUT" && document.activeElement.tagName != "IFRAME" && document.activeElement.tagName != "EMBED"
        ) {
        if (keyCode == 78) {
            try {
                togglePanel("n");
            } catch {
                clog("No n-panel");
            }
        } else if (keyCode == 84) {
            try {
                togglePanel("t");
            } catch {
                clog("No t-panel");
            }
        } else if (keyCode == 76) {
            if (topen === true) {
                lightMode();
            }
        } else if (keyCode == 68) {
            if (topen === true) {
                darkMode();
            }
        } else if (keyCode == 72) {
            if (topen === true) {
                noTooltips();
            }
        } else if (keyCode == 65) {
            if (topen === true) {
                randomArticle();
            }
        } else if (keyCode == 89) {
            if (topen === true) {
                youtube();
            }
        } else if (keyCode == 69) {
            if (topen === true) {
                messageMe(window.location.href);
            }
        } else if (keyCode == 87) {
            if (topen === true) {
                navigationMenu(window.location.href);
            }
        }
    }
}

//-----------------------console messages hinting at panels-----------------------
function secretPanel(i) {
    if (i == 0) {
        if (nopen === false) {
            clog("You've found the secret Properties panel- press N to open it");
        }
    } else if (i == 1) {
        if (topen === false) {
            clog("You've found the secret Tools panel- press T to open it");
        }
    }
}
//-----------------------Toggle panels-----------------------
function togglePanel(p) {
    if (p == "n") {
        if (nopen === true) { //hide panel
            document.getElementById("n-panel-arrow").innerHTML = '<p>&blacktriangleleft;</p>'; //change arrow direction
            document.getElementById("n-panel-arrow").classList.toggle('panel-open');
            document.getElementById("n-panel").style.opacity = "0";
            document.getElementById("n-panel").style.right = "-450px"; //with the N panel, it needs to move to the right to avoid text squish
            nopen = false;
        } else { //show panel
            document.getElementById("n-panel-arrow").innerHTML = '<p>&blacktriangleright;</p>';
            document.getElementById("n-panel-arrow").classList.toggle('panel-open');
            document.getElementById("n-panel").style.opacity = "1";
            document.getElementById("n-panel").style.right = "24px";
            nopen = true;
        }
    } else if (p == "t") {
        if (topen === true) {
            document.getElementById("t-panel").style.opacity = "0";
            document.getElementById("t-panel-arrow").classList.toggle('panel-open');
            document.getElementById("t-panel-arrow").innerHTML = '<p>&blacktriangleright;</p>';
            document.getElementById("t-panel").style.width = "0px"; //this one can just adjust the width
            document.querySelectorAll('.t-icon-box').forEach(function (s) { //font-awesome sizing needs to change as well
                s.style.fontSize = "0px";
            })
            topen = false;
        } else {
            document.querySelectorAll('.t-icon-box').forEach(function (s) {
                s.style.fontSize = "1.9rem";
            })
            document.getElementById("t-panel").style.opacity = "1";
            document.getElementById("t-panel-arrow").classList.toggle('panel-open');
            document.getElementById("t-panel-arrow").innerHTML = '<p>&blacktriangleleft;</p>';
            document.getElementById("t-panel").style.width = "52px";
            topen = true;
        }
    }
}

function lightMode() {
    document.getElementsByTagName("body")[0].id = "lightbody";
    document.getElementsByTagName("footer")[0].id = "lightfooter";
    document.getElementsByClassName("topnav")[0].id = "lightnav";
    window.localStorage.setItem('color', 'light'); //add color mode to local and session storage
    window.sessionStorage.setItem('color', 'light');
}

function darkMode() {
    document.getElementsByTagName("body")[0].id = "darkbody";
    document.getElementsByTagName("footer")[0].id = "darkfooter";
    document.getElementsByClassName("topnav")[0].id = "darknav";
    window.localStorage.setItem('color', 'dark');
    window.sessionStorage.setItem('color', 'dark');
}

function randomArticle() {
    window.location.href = window.location.origin + "/random";

}

function youtube() {
    window.location.href = "https://www.youtube.com/channel/UCimP8dIVhBrCDpJhDqZg1UQ";
}

function messageMe(source) {
    window.location.href = window.location.origin + "/contact";
}

function navigationMenu(current) {
    clog("navigation menu starting at " + current);
}

function noTooltips() { //toggle tooltip display
    document.querySelectorAll('.t-panel').forEach(function (s) {
        s.classList.toggle("no-tooltips");
    });
    document.getElementById('n-panel-arrow').classList.toggle("no-tooltips");
    document.getElementById('t-panel-arrow').classList.toggle("no-tooltips");
}
