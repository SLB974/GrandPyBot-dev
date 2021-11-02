function manageIntro(response) {
    $(".bubble").text(response["intro"])
}

$(window).on('load', function () {
    $.ajax({
        url: '/intro'
    }).done(function (response) {
        manageIntro(response);
        });
});
    