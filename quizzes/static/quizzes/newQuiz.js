let questionNum = 0;
const alphabet = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}

document.addEventListener('DOMContentLoaded', function() {
    const questions =  document.querySelector('#questions');
    document.querySelector('#add-question').addEventListener('click', () => addQuestion())
    addQuestion();
})

document.addEventListener('click', event => {
    const element = event.target;
    if (element.className === 'delete float-right') {
        questionNum--;

        const following = document.querySelectorAll(`#${element.parentElement.parentElement.id} ~ div`);
        Array.from(following).forEach(elem => {
            questionNum = parseInt(elem.id.slice(1)) - 1;
            elem.id = `q${questionNum}`;
            elem.querySelector('h4').innerHTML = `Question ${questionNum}`;
            Array.from(elem.querySelectorAll('label')).forEach(label => {label.htmlFor = label.htmlFor.slice(0,label.htmlFor.length-String(questionNum).length) + questionNum});
            Array.from(elem.querySelectorAll('button')).forEach(button => {button.id = button.id.slice(0,button.id.length-String(questionNum).length) + questionNum});
            Array.from(elem.querySelectorAll('input')).forEach(input => {
                input.id = input.id.slice(0,input.id.length-String(questionNum).length) + questionNum;
                input.name = input.name.slice(0,input.name.length-String(questionNum).length) + questionNum;
            })
        })

        element.parentElement.className = ''
        void element.offsetWidth;
        element.parentElement.className = 'content'
        element.parentElement.style.animationDirection = 'reverse';
        element.parentElement.style.animationPlayState = 'running';

        element.parentElement.parentElement.className = ''
        void element.offsetWidth;
        element.parentElement.parentElement.className = 'jumbotron question'
        element.parentElement.parentElement.style.animationPlayState = 'running';
        element.parentElement.parentElement.style.animationDirection = 'reverse';

        element.parentElement.parentElement.addEventListener('animationend', () => {
            element.parentElement.parentElement.remove();
        })

        if (questionNum === 1){
            Array.from(document.querySelectorAll('.delete')).forEach(button =>{button.setAttribute('disabled','')})
        }
    }
    return false;
})

function addQuestion(){
    if (questionNum === 1){
        document.querySelector('.delete').removeAttribute('disabled');
    }

    questionNum++;
    const question = document.createElement('div')
    question.className = 'jumbotron question'
    question.id = `q${questionNum}`
    question.innerHTML =   `<div class="content">
                                <button class="delete float-right" type="button"><i class="fa-solid fa-xmark fa-2x"></i></button>
                                <h4>Question ${questionNum}</h4>
                                <br>
                                <div class="form-group">
                                    <label for="question-${questionNum}"><h6>Question:</h6></label>
                                    <input id="question-${questionNum}" class="form-control" type="text" name="question-${questionNum}" placeholder="Question" required>
                                </div>
                                <br>
                                <div class="row row-cols-1 row-cols-xl-2 row-cols-lg-2 row-cols-md-1 row-cols-sm-1 g-4"></div>
                                <br>
                                <button id="add-option-${questionNum}" class="btn btn-primary" type="button">Add Option</button>
                                <button id="remove-option-${questionNum}" class="btn btn-primary" type="button">Remove Option</button>
                            </div>`;

    questions.append(question);

    for (let i=0; i < 4; i++){
        addOption(question)
    }

    question.querySelector(`#add-option-${questionNum}`).addEventListener('click', () => addOption(question));
    question.querySelector(`#remove-option-${questionNum}`).addEventListener('click', () => removeOption(question));

    question.style.animationPlayState = 'running';
    question.querySelector('.content').style.animationPlayState = 'running';

    if (questionNum === 1){
        document.querySelector('.delete').setAttribute('disabled','');
    }

    return false;
}

function addOption(question){
    const optionNum = question.querySelectorAll(`.form-group.col`).length
    const newOption = document.createElement('div')
    newOption.className = 'form-group col'
    newOption.innerHTML =  `<label for="answer-${optionNum + 1}-${question.id.slice(1)}"><h6>Option ${alphabet[optionNum + 1]}:</h6></label>
                            <input id="answer-${optionNum + 1}-${question.id.slice(1)}" class="form-control" type="text" name="answer-${optionNum + 1}-${question.id.slice(1)}" placeholder="Option ${alphabet[optionNum + 1]}" required>
                            <label for="correct-${question.id.slice(1)}"><h6>Correct?</h6></label>
                            <input id="correct-${question.id.slice(1)}" class="form-check-input" name="correct-${question.id.slice(1)}" type="radio" value="" required>`
    question.querySelector('.row').append(newOption)

    disableButtons(question);
    return false;
}

function removeOption(question){
    question.querySelector(`.form-group.col:last-child`).remove();
    disableButtons(question);
    return false;
}

function disableButtons(question){
    const optionNum = question.querySelectorAll(`.form-group.col`).length
    if (optionNum <= 2){
        question.querySelector(`#remove-option-${question.id.slice(1)}`).setAttribute('disabled', '')
    }
    else {
        question.querySelector(`#remove-option-${question.id.slice(1)}`).removeAttribute('disabled')
    }
    
    if (optionNum >= Object.keys(alphabet).length){
        question.querySelector(`#add-option-${question.id.slice(1)}`).setAttribute('disabled', '')
    }
    else {
        question.querySelector(`#add-option-${question.id.slice(1)}`).removeAttribute('disabled')
    }
}
