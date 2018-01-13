$(document).ready(function() {
    $("#circle_1").click(function() {
        $(this).attr("src", "image/light_circle.png");
        $("#circle_2").attr("src", "image/blue_circle.png");
        $("#circle_3").attr("src", "image/blue_circle.png");
        $(".background").stop();
        $(".background").animate({left:"0px"}, 1000);
    });
    $("#circle_2").click(function() {
        $(this).attr("src", "image/light_circle.png");
        $("#circle_1").attr("src", "image/blue_circle.png");
        $("#circle_3").attr("src", "image/blue_circle.png");
        $(".background").stop();
        $(".background").animate({left:"-1352px"}, 1000);
    });
    $("#circle_3").click(function() {
        $(this).attr("src", "image/light_circle.png");
        $("#circle_1").attr("src", "image/blue_circle.png");
        $("#circle_2").attr("src", "image/blue_circle.png");
        $(".background").stop();
        $(".background").animate({left:"-2704px"}, 1000);
    });

    $("#zuoyebuluo").mouseover(function() {
        $("#zuoyebuluo_front").stop();
        $("#zuoyebuluo_front").animate({top:"0px"}, 200);
    });
    $("#zuoyebuluo").mouseleave(function() {
        $("#zuoyebuluo_front").stop();
        $("#zuoyebuluo_front").animate({top:"108px"}, 200);
    });

    $("#csdn").mouseover(function() {
        $("#csdn_front").stop();
        $("#csdn_front").animate({top:"0px"}, 200);
    });
    $("#csdn").mouseleave(function() {
        $("#csdn_front").stop();
        $("#csdn_front").animate({top:"108px"}, 200);
    });

    $("#vjudge").mouseover(function() {
        $("#vjudge_front").stop();
        $("#vjudge_front").animate({top:"0px"}, 200);
    });
    $("#vjudge").mouseleave(function() {
        $("#vjudge_front").stop();
        $("#vjudge_front").animate({top:"108px"}, 200);
    });

    $("#codeforces").mouseover(function() {
        $("#codeforces_front").stop();
        $("#codeforces_front").animate({top:"0px"}, 200);
    });
    $("#codeforces").mouseleave(function() {
        $("#codeforces_front").stop();
        $("#codeforces_front").animate({top:"108px"}, 200);
    });
});