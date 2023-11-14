const typeselector = document.getElementById('type')
const openedelement = document.getElementById('openedselection')
const closedelements = document.getElementById('closedelements')
    
    typeselector.addEventListener('change', function () {
        if (typeselector.value === 'open') {
            openedelement.style.display = 'block';
            closedelements.style.display = 'none';
        } else if (typeselector.value === 'close') {
            openedelement.style.display = 'none';
            closedelements.style.display = 'block';
        }
    });