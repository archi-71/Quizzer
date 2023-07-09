document.addEventListener('DOMContentLoaded', function() {
    score = document.querySelector('#average-score');
    if (score.innerHTML !== '-'){
        percentage = parseFloat(score.innerHTML)
        score.style.color = `rgb(${300-3*percentage}, ${3*percentage}, 0)`
    } 
});
