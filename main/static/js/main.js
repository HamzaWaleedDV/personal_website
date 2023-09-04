function mail() {
    const message = document.getElementById("body").value;
    window.open('mailto:learncodeeasily.contact@gmail.com?subject=i want a service&body='+message);
}