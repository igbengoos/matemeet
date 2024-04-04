function CommentReplyToggle(parent_id) {
    const row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }     
}

function showNotifications() {
    const container = document.getElementById('notification-container');
        if (container.classList.contains('d-none')) {
            container.classList.remove('d-none');
        } else {
            container.classList.add('d-none');
        }
    }

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i = cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does This Cookie string begin with the none we want
            if (cookie.substring(0, name.length) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    } return cookieValue;
} 

function remveNotification(remveNotificationURL, redirectURL) {
    const csrftoken = getCookie('csrftoken');
    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState = XMLHttpRequest.DONE) {
            if (xmlhttp.status == 200) {
                window.location.replace(redirectURL);
            } else {
                alert('There was an error with the code');
            }
        }
    };
    xmlhttp.open("DELETE", remveNotificationURL, true);
    xmlhttp.setRequestHeader("X-CRSFToken", csrftoken)
    xmlhttp.send();
}