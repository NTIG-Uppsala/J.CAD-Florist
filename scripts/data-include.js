document.addEventListener("DOMContentLoaded", function() {
    var includes = document.querySelectorAll('[data-include]');
    includes.forEach(function(include) {
        var file = include.getAttribute('data-include') + '.html';
        fetch(file)
            .then(response => response.text())
            .then(data => {
                include.innerHTML = data;
                const fragment = document.createDocumentFragment();
                include.appendChild(fragment);
            })
            .catch(error => console.error('Error loading file:', error));
    });
});