
const searchForm = document.querySelector('.search-area > form');
const searchButton = searchForm.querySelector('button');
const searchBar = searchForm.querySelector('input');
let valid = false;


searchForm.addEventListener('submit', (e) => {
    e.preventDefault();

    searchBar.addEventListener('keyup', (e) => {
        if (e.target.value.trim().length > 0) {
            e.target.value = e.target.value.trim();
            valid = true;
        }
        if (e.which == 13 && valid == true) {
            searchForm.submit();
        }
        searchButton.disabled = !valid;
    });

    searchButton.addEventListener('click', () => {
        if (valid == true) {
            searchForm.submit();
        }
    });

});



