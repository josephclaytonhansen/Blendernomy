//-----------------------Set dark or light mode to be persistent-----------------------
window.addEventListener("DOMContentLoaded", (event) => {
    localStorage;
    sessionStorage;
    if (localStorage.getItem("color") == "dark") {
        darkModeNoFlash();
    };
    if (sessionStorage.getItem("color" == "dark")) {
        darkModeNoFlash();
    };
    if (localStorage.getItem("color") == "light") {
        lightModeNoFlash();
    };
    if (sessionStorage.getItem("color" == "light")) {
        lightModeNoFlash();
    };

});

function home() {
    window.location.href = window.location.origin;
}

//These two functions are for page loads with a persistent color mode; instead of the usual transitions, we assign a no-flash style
function darkModeNoFlash() {
    document.getElementsByTagName("body")[0].id = "darkbody-noflash";
    document.getElementsByTagName("footer")[0].id = "darkfooter";
    document.getElementsByClassName("topnav")[0].id = "darknav";
    window.localStorage.setItem('color', 'dark');
    window.sessionStorage.setItem('color', 'dark');
}

function lightModeNoFlash() {
    document.getElementsByTagName("body")[0].id = "lightbody-noflash";
    document.getElementsByTagName("footer")[0].id = "lightfooter";
    document.getElementsByClassName("topnav")[0].id = "lightnav";
    window.localStorage.setItem('color', 'light');
    window.sessionStorage.setItem('color', 'light');
}

window.addEventListener("scroll", function () {
    if (this.scrollY > 20) {
        document.getElementsByClassName("topnav")[0].style.height = 50 + "px";
        document.getElementById("n-panel").style.top = 60 + "px";
        document.querySelectorAll('.topnav-link').forEach(function (s) {
            s.style.opacity = 1;
            s.style.fontSize = "1rem";
        });
    } else if (this.scrollY < 20) {
        document.getElementsByClassName("topnav")[0].style.height = 4 + "px";
        document.getElementById("n-panel").style.top = 20 + "px";
        document.querySelectorAll('.topnav-link').forEach(function (s) {
            s.style.opacity = 0;
            s.style.fontSize = "0px";
        });
    }
})

function hoverTopNav() {
    if (document.getElementsByClassName("topnav")[0].style.height == "4px") {
        document.getElementsByClassName("topnav")[0].style.height = 10 + "px";
    }
}

function noHoverTopNav() {
    if (document.getElementsByClassName("topnav")[0].style.height == "10px") {
        document.getElementsByClassName("topnav")[0].style.height = 4 + "px";
    }
}

function showTopNav() {
    if (document.getElementsByClassName("topnav")[0].style.height == "10px") {
        document.getElementsByClassName("topnav")[0].style.height = 50 + "px";
        document.getElementById("n-panel").style.top = 60 + "px";
        document.querySelectorAll('.topnav-link').forEach(function (s) {
            s.style.opacity = 1;
            s.style.fontSize = "1rem";
        });
    } else {
        document.getElementsByClassName("topnav")[0].style.height = 4 + "px";
        document.getElementById("n-panel").style.top = 20 + "px";
        document.querySelectorAll('.topnav-link').forEach(function (s) {
            s.style.opacity = 0;
            s.style.fontSize = "0px";
        });
    }
}