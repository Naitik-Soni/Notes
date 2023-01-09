function shownotes(){
    document.getElementById("form").style.display = "inline";
    document.body.style.overflow = 'hidden';
}

function closenote(){
    document.getElementById("form").style.display = "none";
    document.getElementById("title").value = "";
    document.getElementById("inputnote").innerHTML = "";
    document.getElementsByClassName("noteform")[0].action = "addnotes/";
    document.getElementById("abc").setAttribute("href", "");
    document.getElementById("abc").style.display = "none";
    document.body.style.overflow = 'visible';
}

function showmynote(ids){
    document.getElementById("form").style.display = "inline";
    var id = String(ids);
    var title = document.getElementById(id+"headers").innerHTML;
    var paragraph = document.getElementById(id+"paragraph").innerHTML;

    document.getElementsByClassName("noteform")[0].action = "updatenote/"+id;
    document.getElementById("abc").setAttribute("href", "delete/" + id);
    document.getElementById("abc").style.display = "inline";
    
    document.getElementById("title").value = title;
    document.getElementById("inputnote").innerHTML = paragraph;
    document.body.style.overflow = 'hidden';

}