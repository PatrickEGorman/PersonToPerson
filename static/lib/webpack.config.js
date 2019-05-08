var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
    index: '../js/index',
    facebook_login: '../js/Api/Facebook/login',
    generic_get_posts: '../js/Api/Generic/get_posts',
    facebook_get_posts: '../js/Api/Facebook/get_posts'
  },
  mode:'development',

  output: {
      path: path.resolve('../js/bundles/'),
      filename: "[name].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env',
              '@babel/preset-react'],

          }
        }
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx'],
    alias: {
      react: path.resolve(__dirname, 'node_modules/react'),
      react_dom: path.resolve(__dirname, 'node_modules/react-dom'),
      nightmare: path.resolve(__dirname, 'node_modules/nightmare')
    }
  },
  node: {
    fs: 'empty',
    child_process: 'empty'
  }

};
