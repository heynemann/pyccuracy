$(function(){
    var left = $("#main_title").position().left + $("#main_title").width() - $("#toc").width() - 10;
    $("#toc").css("left", left + "px");
});
