

const $form = $("#message");
const $box = $("#chatbox");
const $question = $("#user_query");
const $map = $("#map");
const $spinner = $(".spinner");
const $origin = $("#chatbox .dialogue_left:first-child");

function scrollToLast() {
    var $element = $box.children().last()
    $box.animate({
        scrollTop: $element.offset().top
    }, 'fast');
};

function createDialogue(dialogue, direction) {

    if (direction == true) {
        direction = "dialogue_left";
    } else {
        direction = "dialogue_right";
    };

    let $target = $origin.clone()
    $target.removeClass('dialogue_left');
    $target.addClass(direction);
    $target.children('.bubble').text(dialogue);
    $target.appendTo($box);
    scrollToLast();

}

function createMap(mapLink) {
    createDialogue('Voici une carte pour te repérer...',true)
    var img = $('<img id="map">');
    img.attr('src', mapLink);
    $box.append(img);
    scrollToLast();

};

function createLink(wikiLink) {
    link = $("<a target='_blank' id='wikilink' href=" + wikiLink + ">Plus d'informations sur Wikipedia</a>");
    $box.append(link);
    scrollToLast();

};

function manageEmpty(response) {
    createDialogue(response["empty"], true);
    scrollToLast();
}
function manageResponse(response) {
    if (response.grandpy_none) {
        createDialogue(response.grandpy_none, true);
    } else {
        createDialogue(response.grandpy_response, true);
        createDialogue(response.address, true);
        createMap(response.map_link);
        if (response.wiki_response) {
            createDialogue(response.grandpy_catch_wiki, true);
            createDialogue(response.wiki_response, true);
            createLink(response.wiki_link);
            createDialogue(response.grandpy_next_query, true);
        } else {
            createDialogue("Je n'ai pas trouvé d'informations supplémentaires sur cet endroit", true);
        }
    };
};



$(document).ready(() => {

    $("#user_query").focus()
    $form.submit(function (e) {
        e.preventDefault();
        $spinner.toggle();
        var user_query = $question.val();
        $question.val("");
        
        if (user_query.length == 0) {
            $.ajax({
                url: '/empty'
            }).done(function (response) {
                manageEmpty(response);
                $spinner.toggle();
            });
        } else {
            
            $box.children().not(':last').remove();
            createDialogue(user_query, false);
            $.ajax({
                url: '/ajax',
                type: 'POST',
                data: JSON.stringify(user_query),
                success: function (response) {
                    console.log(response);
                    manageResponse(response);
                    $spinner.toggle();
                },
                error: function (error) {
                    console.log(error);
                }
            });
        };
        
    });

});