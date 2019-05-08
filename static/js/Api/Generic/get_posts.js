
let Nightmare = require('nightmare');
const nightmare = Nightmare({ show: true });

function search_all_posts(url) {
    return nightmare
        .goto(url)
    }

module.exports = {
    search_all_posts: search_all_posts
};
