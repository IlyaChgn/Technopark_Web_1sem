function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const likesQuestionsList = document.getElementsByClassName('like-questions-list');
const likesAnswerList = document.getElementsByClassName('like-answer-list');
const correctAnswersList = document.getElementsByClassName('correct-answer-list')

for (let item of likesQuestionsList) {
    const DislikeBtn = item.children[0].children[0];
    const Counter = item.children[1];
    const LikeBtn = item.children[2].children[0];

    DislikeBtn.addEventListener('click', () => {
        const formData = new FormData();
        formData.append('item_id', item.dataset.id);
        formData.append('rate_type', 'dislike');
        formData.append('item_type', 'question');
        const request = new Request('/rate/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                Counter.innerHTML = data.count;
                if (data.count < 0)
                    Counter.style.color = "red";
                else
                    Counter.style.color = "green";

                if (data.action == 'add') {
                    DislikeBtn.classList.remove('btn-outline-danger');
                    DislikeBtn.classList.add('btn-danger');
                } else {
                    DislikeBtn.classList.remove('btn-danger');
                    DislikeBtn.classList.add('btn-outline-danger');
                }

                LikeBtn.classList.remove('btn-success');
                LikeBtn.classList.add('btn-outline-success');
            })
    });

    LikeBtn.addEventListener('click', () => {
        const formData = new FormData();
        formData.append('item_id', item.dataset.id);
        formData.append('rate_type', 'like');
        formData.append('item_type', 'question');
        const request = new Request('/rate/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                Counter.innerHTML = data.count;
                if (data.count >= 0)
                    Counter.style.color = "green";
                else
                    Counter.style.color = "red";

                if (data.action == 'add') {
                    LikeBtn.classList.remove('btn-outline-success');
                    LikeBtn.classList.add('btn-success');
                } else {
                    LikeBtn.classList.remove('btn-success');
                    LikeBtn.classList.add('btn-outline-success');
                }

                DislikeBtn.classList.remove('btn-danger');
                DislikeBtn.classList.add('btn-outline-danger');
            })
    });
}

for (let item of likesAnswerList) {
    const DislikeBtn = item.children[0].children[0];
    const Counter = item.children[1];
    const LikeBtn = item.children[2].children[0];

    DislikeBtn.addEventListener('click', () => {
        const formData = new FormData();
        formData.append('item_id', item.dataset.id);
        formData.append('rate_type', 'dislike');
        formData.append('item_type', 'answer');
        const request = new Request('/rate/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                Counter.innerHTML = data.count;
                if (data.count < 0)
                    Counter.style.color = "red";
                else
                    Counter.style.color = "green";

                if (data.action == 'add') {
                    DislikeBtn.classList.remove('btn-outline-danger');
                    DislikeBtn.classList.add('btn-danger');
                } else {
                    DislikeBtn.classList.remove('btn-danger');
                    DislikeBtn.classList.add('btn-outline-danger');
                }

                LikeBtn.classList.remove('btn-success');
                LikeBtn.classList.add('btn-outline-success');
            })
    });

    LikeBtn.addEventListener('click', () => {
        const formData = new FormData();
        formData.append('item_id', item.dataset.id);
        formData.append('rate_type', 'like');
        formData.append('item_type', 'answer');
        const request = new Request('/rate/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                Counter.innerHTML = data.count;
                if (data.count >= 0)
                    Counter.style.color = "green";
                else
                    Counter.style.color = "red";

                if (data.action == 'add') {
                    LikeBtn.classList.remove('btn-outline-success');
                    LikeBtn.classList.add('btn-success');
                } else {
                    LikeBtn.classList.remove('btn-success');
                    LikeBtn.classList.add('btn-outline-success');
                }

                DislikeBtn.classList.remove('btn-danger');
                DislikeBtn.classList.add('btn-outline-danger');
            })
    });
}

for (let item of correctAnswersList) {
    const IsCorrectBtn = item.children[0].children[0];
    const IsUncorrectBtn = item.children[1].children[0];

    IsCorrectBtn.addEventListener('click', () => {
        const formData = new FormData();
        formData.append('item_id', item.dataset.id);
        formData.append('correctness', 'true');

        const request = new Request('/correct/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                if (data.is_correct == 'true') {
                    IsCorrectBtn.checked = true;
                    IsUncorrectBtn.checked = false;
                } else if (data.is_correct == 'false') {
                    IsCorrectBtn.checked = false;
                    IsUncorrectBtn.checked = true;
                } else {
                    IsCorrectBtn.checked = false;
                    IsUncorrectBtn.checked = false;
                }
            })
    });

    IsUncorrectBtn.addEventListener('click', () => {
        const formData = new FormData();
        formData.append('item_id', item.dataset.id);
        formData.append('correctness', 'false');

        const request = new Request('/correct/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            }
        })
        fetch(request)
            .then((response) => response.json())
            .then((data) => {
                if (data.is_correct == 'false') {
                    IsCorrectBtn.checked = false;
                    IsUncorrectBtn.checked = true;
                } else if (data.is_correct == 'true') {
                    IsCorrectBtn.checked = true;
                    IsUncorrectBtn.checked = false;
                } else {
                    IsCorrectBtn.checked = false;
                    IsUncorrectBtn.checked = false;
                }
            })
    });
}