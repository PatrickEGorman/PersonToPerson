import React, { Component } from 'react';
import ReactDOM from 'react_dom';

function login() {
    FB.login(function (response) {
        if (response.authResponse) {
            console.log('Welcome!  Fetching your information.... ');
        } else {
            console.log('User cancelled login or did not fully authorize.');
        }
    });
    checkLoginState();
}

class LoginFacebookOption extends Component{
   render(){
      return(
          <a className="nav-link" id="login_facebook" onClick={login} href="#">Sign In With
              Facebook</a>
      );
   }
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected'){
        document.cookie = "facebook_access_token="+response.authResponse.facebook_access_token;
        document.cookie = "is_logged_in_facebook=true";
    }
    else{
        ReactDOM.render(<LoginFacebookOption />, document.getElementById('facebookLogoutLogin'));
        document.cookie = "is_logged_in_facebook=false";
    }
  });
}

document.addEventListener('facebookLoaded', function (e) {checkLoginState();});
