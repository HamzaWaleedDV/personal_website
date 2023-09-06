function mail() {
    const message = document.getElementById("body").value;
    const subject = document.getElementById("subject").value;
    window.open('mailto:learncodeeasily.contact@gmail.com?subject=' + subject + '&body=' + message);
}