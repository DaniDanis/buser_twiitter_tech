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

//funcao que faz fecth-post (geral)
function faz_fetch(url, data) {
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify(data),
    });
  }

  // funcao que pega o csrf'token
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // muda de curtido para não curtido e vice-versa
  function muda_cor_de_curtido(obj) {
    let get_obj_id = obj.id.split('_')[1]
    let curtidas = document.getElementById('likes_id'+(get_obj_id))

    // if else verifica se o post tem a classe curtido
    if (obj.classList.contains("curtido")) {
      obj.src = "../../static/images/posts/icones/curtir_icone.svg";
      obj.classList.remove("curtido");
      curtidas.innerText = parseInt(curtidas.innerText)-1
  

    } else {
      obj.src = "../../static/images/posts/icones/ja_curtido.svg";
      obj.classList.add("curtido");
      curtidas.innerText = parseInt(curtidas.innerText)+1
    }
    // dados enviado pelo fetch
    let data = {
      post_id: obj.id.split("_")[1],
    };
    //parte que faz a requisição fetch
    faz_fetch("/curtir-action/", data);
  }

  //funcao para caixa de comentario
  function abre_caixa_comentario(obj) {
    // pega o id do post a partir do id do comentário,
    // já que a diferença é só, por exemplo, 89 e comment_89
    let id_post = obj.id.split("_")[1];
    //pega o elemento caixa de comentário
    let cx_comment = document.querySelector("#cx_comment");
    //pega a div que contera o post:
    let div_post_de_referencia = document.querySelector('#cx_comment > .div-post-de-referencia ');
    if (div_post_de_referencia.children.length){
      div_post_de_referencia.children[0].remove();
    }
    // clona o post real, pra não correr risco de eu mexer no post em si
    let post = document.getElementById(id_post).cloneNode(true);
    // insere uma nova classe no post
    post.classList.add("post_caixa_comment");
    // inisiro o post na div, para estilizar
    div_post_de_referencia.appendChild(post);

    // sequencia de remocao de imagens e aside do post
    document.querySelector(".post_caixa_comment .post_content_image").remove();
    document
      .querySelector(".post_caixa_comment .post_icones_de_interacao")
      .remove();

    // Comando que adiciona valor ao input que repassa o id do post
    let input_id_post = document.createElement('input');


    input_id_post.value = id_post;
    input_id_post.name = 'input-post-id';
    document.querySelector('.form-comment-post').appendChild(input_id_post);
    input_id_post.type = 'hidden';
    //rederiza a caixa na tela através da troca de display
    cx_comment.style.display = "flex";
    document.querySelector('#text-input-comment').focus();
    cx_comment.addEventListener('blur', reset_comment)
 
  }



 function reset_comment(){
  console.log ("reset rodando ...")
  let div_post_de_referencia = document.querySelector("#div-post-de-referencia").firstChild;
  div_post_de_referencia.remove();
 }

 function cx_comment_display_none(){
  let cx_comment = document.querySelector("#cx_comment");
  cx_comment.style.display  = "none"  ;
  let input_cx_comment = document.querySelector("#cx_comment .main-text-input");
  input_cx_comment.value = '';
 }

 // abre e fecha o menu do usuario
 function cx_menubar_display_none(){
  let cx_menubar = document.getElementById('menubar-profile-dropup-menuitens')

  if (cx_menubar.classList.contains("esconder")){
    cx_menubar.classList.remove("esconder");
  } else{
    cx_menubar.classList.add("esconder");
  }
 }
