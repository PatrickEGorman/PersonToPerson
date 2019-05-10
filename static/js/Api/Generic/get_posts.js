
// import Nightmare from 'nightmare'
// const nightmare = Nightmare({ show: true });
import $ from 'jquery'

export default {
    // search_all_posts: function search_all_posts(url)
    // {
    //     return nightmare
    //         .goto(url)
    // },

    getAndFilter: function getAndFilter(url, className) {
        let data = $.get(url);
        return data.getElementsByClassName(className);
    }
}
