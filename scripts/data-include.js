//Script som inkluderar html-filer i andra html-filer

document.addEventListener("DOMContentLoaded", function() { //väntar på att hela sidan laddas in innan scriptet körs
    var includes = document.querySelectorAll('[data-include]');
    includes.forEach(function(include) { //hämtar filnamn från 'data-include' attributet och lägger till .html
        var file = include.getAttribute('data-include') + '.html';
        fetch(file) //hämtar html-filen
            .then(response => response.text())
            .then(data => {
                include.innerHTML = data; //lägger in html-koden i elementet
            })
            .catch(error => console.error('Error loading file:', error));
    });
});