
let generic_get_posts = require('../../bundles/generic_get_posts');
let Nightmare = require('nightmare');
const nightmare = Nightmare({ show: true });

function get_posts(category) {
    if(category === "view_all"){
        return generic_get_posts.search_all_posts('https://www.facebook.com/marketplace/')
            .evaluate(() => document.querySelector('#links ._7yc _3ogd').href)
            .end();
    }
}

console.log(get_posts('view_all'));
