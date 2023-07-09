let userList = [];
let users = null;
let sort = null;
let sortTitle = null;

document.addEventListener('DOMContentLoaded', function() {
    users = document.querySelector('#users');
    sort = document.querySelector('#sort');
    sort.addEventListener('change', () => showUsers())
    sortTitle = document.querySelector('#sortBy');

    fetch('getUsers')
    .then(response => response.json())
    .then(users => {
        users.forEach(user => {
            userList.push([user.id, user.name, user.averageScore, user.correctAnswers, user.quizzesCompleted, user.quizzesCreated])
        });
        showUsers();
    });
})

function showUsers(){
    const sortBy = parseInt(sort.value.slice(0,1))
    userList.sort(
        (first, second) => { return second[sortBy] - first[sortBy] }
    );
    console.log(sortBy)
    sortTitle.innerHTML = sort.value.slice(2);
    users.innerHTML = '';
    for (let i = 0; i < userList.length; i++) {
        const element = document.createElement('tr');
        element.innerHTML = `<th scope="row" colspan="1">#${i+1}</th>
                             <td colspan="1"><a class="underline-link" href="profile/${userList[i][0]}"><b>${userList[i][1]}</b></a></td>
                             <td colspan="1">${userList[i][sortBy]}</td>`;
        users.append(element);
    }
    return false;
}