function auto_height(elem) {  /* javascript */
    elem.style.height = "1px";
    elem.style.height = (elem.scrollHeight)+"px";
}

function tweet_input_popup() {
    var display = document.getElementsByClassName('main-textbox-column');
    if(display[0].style.display == "none")
        display[0].style.display = 'block';
    else
    display[0].style.display = 'none';
}