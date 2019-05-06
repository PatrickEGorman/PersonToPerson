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

function logout(){

}

class LogoutFacebookOption extends Component{
   render(){
      return(
         <a className="nav-link" id="logout_facebook" onClick={logout()} href="#">Log Out</a>
      );
   }
}

class LoginFacebookOption extends Component{
   render(){
      return(
          <a className="nav-link" id="login_facebook" onClick={login()} href="#">Sign In With
              Facebook</a>
      );
   }
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected'){
        document.cookie = "facebook_access_token="+response.authResponse.facebook_access_token;
        ReactDOM.render(<LogoutFacebookOption />, document.getElementById('facebookLogoutLogin'));
    }
    else{
        ReactDOM.render(<LoginFacebookOption />, document.getElementById('facebookLogoutLogin'));
    }
  });
}

document.addEventListener('facebookLoaded', function (e) {checkLoginState();});
