var modal_seen = false;

function closeModal() {
    document.querySelectorAll('.modal').forEach(function (s) {
        s.classList.remove('is-active');
        modal_seen = true;
    })
}
window.addEventListener("scroll", function () {
    console.log(this.scrollY);
    if (this.scrollY > 200 && !modal_seen) {
        document.querySelectorAll('.modal').forEach(function (s) {
            s.classList.add('is-active');
        })
    }
})