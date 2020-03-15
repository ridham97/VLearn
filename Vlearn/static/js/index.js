function LanguageColors() {
    var colors = ["#AD1457", "#1565C0", "#CDDC39", "#263238", "#1B5E20", "#311B92", "#26A69A", "#9E9D24"],
        len = colors.length;
    $(".v-color").css(
        "background-color",
        (index, style) => colors[index % len]
    );
}
LanguageColors();


$(document).ready(function () {
    var trigger = $('#navbarText ul li a'),
        container = $('#card-1');

    $("#card-1").load("v-module.html");
    trigger.on('click', function () {
        var $this = $(this),
            target = $this.data('target');

        container.load(target + '.html');


        return false;
    });
});


$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});



window.onscroll = function () { myFunction() };

var header = document.getElementById("v-myHeader");



var sticky = header.offsetTop;


function myFunction() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

var btns = document.getElementsByClassName("v-active");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("active");
        current[0].className = current[0].className.replace(" active", "");
        this.className += " active";
    });
}