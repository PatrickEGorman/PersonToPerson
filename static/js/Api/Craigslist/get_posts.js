import GenericGetPosts from '../Generic/get_posts'


let results = GenericGetPosts.getAndFilter('https://charlottesville.craigslist.org/d/musical-instruments/search/msa', "result-row");

console.log(results[0]);
