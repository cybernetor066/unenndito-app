/* eslint-disable no-unused-vars */

document.addEventListener("DOMContentLoaded", init, false); // Initialise the DOM Environment
	
function init() {
    document.getElementsByClassName("showHideToolTip").forEach(element => {
        element.addEventListener("mouseover", showTip, false);
    });  
    document.getElementsByClassName("showHideToolTip").forEach(element => {
        element.addEventListener("mouseout", hideTip, false);
    });
    document.getElementsByClassName("showHideToolTip").forEach(element => {
        element.addEventListener("click", copyText, false);
    });  
}




function showTip() {
    // document.getElementById("myTooltip").innerHTML = alert("Hello");
    document.getElementById("myTooltip").style.visibility = "visible";
    document.getElementById("myTooltip").style.opacity = 1;

    setTimeout(() => {
        document.getElementById("myTooltip").style.visibility = "hidden";
        document.getElementById("myTooltip").style.opacity = 0;
    }, 1500);
}

function hideTip() {
    // document.getElementById("myTooltip").innerHTML = alert("Hello");
    document.getElementById("myTooltip").style.visibility = "hidden";
    document.getElementById("myTooltip").style.opacity = 0;
}


function copyText(text){
    // First of all hide the first tooltip
    // document.getElementById("myTooltip").style.visibility = "hidden";
    // document.getElementById("myTooltip").style.opacity = 0;

    var dummy = document.createElement("input");
    // dummy.style.display = 'none';
    document.body.appendChild(dummy);

    dummy.setAttribute("id", "dummy_id");
    document.getElementById("dummy_id").value=text;
    dummy.select();
    dummy.setSelectionRange(0, 99999);
    document.execCommand("copy");
    document.body.removeChild(dummy);

    document.getElementById("copiedTooltip").style.visibility = "visible";
    document.getElementById("copiedTooltip").style.opacity = 1;

    setTimeout(() => {
        document.getElementById("copiedTooltip").style.visibility = "hidden";
        document.getElementById("copiedTooltip").style.opacity = 0;
    }, 1500);
}