let questionsAnswered = new Set();
let progressBar = undefined;
let questionNumber = 0;

document.addEventListener('DOMContentLoaded', function() {
    progressBar = document.querySelector('.progress-bar');
    questionNumber = document.querySelectorAll('.jumbotron').length;
    Array.from(document.querySelectorAll('[type=radio]')).forEach((button) => {
        button.addEventListener('change', () => updateProgressBar(button));
    });
});

function updateProgressBar(button){
    if (!(questionsAnswered.has(button.id.slice(0,-2)))){
        questionsAnswered.add(button.id.slice(0,-2));
        percentage = (questionsAnswered.size / questionNumber) * 100;
        progressBar.innerHTML = `${Math.round(percentage * 10) / 10}%`;
        progressBar.style.width = `${percentage}%`;
        if (percentage >= 100){
            document.querySelector('#submit-answers').removeAttribute('disabled');
        }
    }
    return false;
}