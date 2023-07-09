let quizzesElem = undefined;
let category = 'none';


document.addEventListener('DOMContentLoaded', function() {
    quizzesElem = document.querySelector('#quizzes');
    category = document.querySelector('#filterCategory').dataset.category_id;
    document.querySelector('#search-box').addEventListener('input', () => searchQuizzes(document.querySelector('#search-box').value))
    loadQuizzes();
});

function loadQuizzes(){
    quizzesElem.innerHTML = '';
    if (category === "none"){
        ext = ''
    }
    else {
        ext = `/${category}`
    }
    fetch(`../../getQuizzes${ext}`)
    .then(response => response.json())
    .then(quizzes => {
        quizzes.forEach(quiz => {
            const element = document.createElement('div');
            element.className = 'col';
            element.innerHTML = `<div class="card quiz-card">
                                    <h4 id="quiz-name" class="card-title">${quiz.name}</h4>
                                    <h6>In <b id="quiz-category" class="card-link link-primary underline-link">${quiz.category}</b></h6>
                                    <p id="quiz-description" class="card-text">${quiz.description}</p>
                                    <p class="card-text">${quiz.questionNumber} questions</p>
                                    <p class="card-text">Created by <b id="quiz-creator" class="card-link link-primary underline-link">${quiz.creator}</b> on <i>${quiz.timestamp}</i></p>
                                </div>`;
            
            element.querySelector('#quiz-category').addEventListener('click', (e) => {window.location.href = `../../quizzes/${quiz.category_id}`; e.stopPropagation();});
            element.querySelector('#quiz-creator').addEventListener('click', (e) => {window.location.href = `../../profile/${quiz.creator_id}`; e.stopPropagation();});
            element.addEventListener('click', () => window.location.href = `../../quiz/${quiz.id}`);
            quizzesElem.append(element);

        });

        if (quizzes.length === 0){
            document.querySelector('#no-results').className = '';
        }

    });
    return false;
}

function searchQuizzes(query){
    Array.from(quizzesElem.querySelectorAll('div.col')).forEach(quiz => {
        const contentString = `${quiz.querySelector('#quiz-name').innerHTML} ${quiz.querySelector('#quiz-category').innerHTML} ${quiz.querySelector('#quiz-description').innerHTML}`
        if (contentString.toLowerCase().includes(query.toLowerCase())){
            quiz.className = 'col'
        } 
        else {
            quiz.className = 'col hidden'
        }
    })

    if (quizzesElem.querySelectorAll('div.col:not(.hidden)').length === 0){
        document.querySelector('#no-results').className = '';
    }
    else {
        document.querySelector('#no-results').className = 'hidden';
    }
}