function auto_height(elem) {  /* javascript */
    elem.style.height = "1px";
    elem.style.height = (elem.scrollHeight)+"px";
}

function tweet_input_popup() {
    var textbox = document.getElementById('main-textbox-column');

    var postlist = document.getElementsByClassName('main-postlist');
    

    if(textbox.style.display === 'none' || textbox.style.display === ''){

        textbox.style.display = 'block';
        postlist[0].style.margin = '0 auto auto auto';
    } else{
        textbox.style.display = 'none';
        postlist[0].style.margin = '6vh auto auto auto';
    }
}