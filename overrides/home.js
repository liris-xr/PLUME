function updateHeaderClass() {
    if (window.scrollY > document.querySelector('.teaser').offsetHeight) {
        document.querySelector('.md-header').classList.remove('md-header--transparent');
    } else {
        document.querySelector('.md-header').classList.add('md-header--transparent');
    }
}

window.onload = updateHeaderClass;
window.onscroll = updateHeaderClass;