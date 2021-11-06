

var myLink = document.getElementById('mylink');

myLink.onclick = function(){

    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "Public/Scripts/filename.js."; 
    document.getElementsByTagName("head")[0].appendChild(script);
    return false;

}


