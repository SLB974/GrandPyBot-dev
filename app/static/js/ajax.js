

const $form = $("#message");
const $box = $("#chatbox");
const $question = $("#user_query");
const $spinner = $("#spinner");
const $map = $("#map");

function createParagraph(paragraphContent, classe) {
    let paragraph = document.createElement("p");
    paragraph.innerHTML = paragraphContent;
    paragraph.className = classe;
    $box.append(paragraph);
};

function createMap(mapLink) {

    var img = $('<img id="map">');
    img.attr('src', mapLink);
    $box.append(img);
};


function createLink(wikiLink) {
    link = $("<a target='_blank' href=" + wikiLink + ">Plus d'informations sur Wikipedia</a>");
    $box.append(link);
};

function updateScroll() {
    $box.scrollTop = $box.scrollHeight;
};



function manageResponse(response) {
    if (response.grandpy_none) {
        createParagraph(response.grandpy_none, "grand_py");
    } else {
        createParagraph(response.grandpy_response, "grand_py");
        createParagraph(response.address, "grand_py");
        createMap(response.map_link);
        createParagraph(response.grandpy_catch_wiki, "grand_py");
        createParagraph(response.wiki_response, "grand_py");
        createLink(response.wiki_link);
        updateScroll();
        $spinner.toggleClass("spinner_on spinner_off")
    };
};


$(document).ready(() => {

    // $('#mop').attr('src', "https://maps.googleapis.com/maps/api/staticmap?center=Berkeley,CA&zoom=14&size=400x400&key=AIzaSyDkeF5Xu-WxkLQWfA4TBXdcupRDi6KSeRY");

    $form.submit(function (e) {
        e.preventDefault();
        $box.empty();
        var user_query = $question.val();
        createParagraph(user_query, "user");
        $question.val("");
        $spinner.toggleClass("spinner_off spinner_on");
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
    });

});