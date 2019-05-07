import React, { Component } from '../lib/node_modules/react';
import ReactDOM from '../lib/node_modules/react-dom';


function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
  }
}

function showPosition(position) {
  $(document).ready(function() {
      document.cookie = "lat="+position.coords.latitude;
      document.cookie = "long="+position.coords.longitude;
  })
}

function login() {
    FB.login(function (response) {
        if (response.authResponse) {
            console.log('Welcome!  Fetching your information.... ');
        } else {
            console.log('User cancelled login or did not fully authorize.');
        }
    });
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
    }
    else{
        ReactDOM.render(<LoginFacebookOption />, document.getElementById('facebookLogoutLogin'));
    }
  });
}

document.addEventListener('facebookLoaded', function (e) {checkLoginState();});


