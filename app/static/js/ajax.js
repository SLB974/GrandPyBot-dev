

const $form = $("#message");
const $box = $("#chatbox");
const $question = $("#user_query");
const $map = $("#map");
const $spinner = $(".spinner");
const $origin = $("#chatbox .dialogue_left:first-child");

function createDialogue(dialogue, direction) {

    console.log(direction);

    if (direction == true) {
        direction = "dialogue_left";
    } else {
        direction = "dialogue_right";
    };


    console.log(dialogue, direction);
    let $target = $origin.clone()
    $target.removeClass('dialogue_left');
    $target.addClass(direction);
    $target.children('.bubble').text(dialogue);
    $target.appendTo($box);
    $box.animate({ scrollTop: 1000 }, "slow");

}

function createMap(mapLink) {
    createDialogue('Voici une carte pour te repérer...',true)
    var img = $('<img id="map">');
    img.attr('src', mapLink);
    $box.append(img);
    $box.animate({ scrollTop: 1000 }, "slow");

};

function createLink(wikiLink) {
    link = $("<a target='_blank' id='wikilink' href=" + wikiLink + ">Plus d'informations sur Wikipedia</a>");
    $box.append(link);
    $box.animate({ scrollTop: 1000 }, "slow");

};

function manageEmpty(response) {
    createDialogue(response["empty"], true);
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
            createDialogue("Je n'ai pas trouvé d'informations supplémentaires sur cet endroit", true)
        }
    };
};



$(document).ready(() => {

    $form.submit(function (e) {
        e.preventDefault();
        $spinner.show();
        var user_query = $question.val();
        console.log(user_query.length);
        $question.val("");
        
        if (user_query.length == 0) {
            $.ajax({
                url: '/empty'
            }).done(function (response) {
                console.log(response);
                manageEmpty(response);
            });
        } else {
            
            createDialogue(user_query, false);
            $box.animate({ scrollTop: 1000 }, "slow");
            $.ajax({
                url: '/ajax',
                type: 'POST',
                data: JSON.stringify(user_query),
                success: function (response) {
                    console.log(response);
                    manageResponse(response);
                },
                error: function (error) {
                    console.log(error);
                }
            });
        };
        
        $box.animate({ scrollTop: 1000 }, "slow");

        $spinner.hide();
    });

});