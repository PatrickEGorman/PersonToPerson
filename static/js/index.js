import React from 'react'
import ReactDOM from 'react-dom'


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

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected'){
        document.cookie = "facebook_access_token="+response.authResponse.facebook_access_token;
    }
    else{
        console.log('do something here');
    }
  });
}

window.fbAsyncInit = function() {
    FB.init({
      appId            : '298536934407119',
      autoLogAppEvents : true,
      xfbml            : true,
      version          : 'v3.2'
    });
    document.getElementById('login_facebook').style.visibility = "visible";
    FB.api('/me', function(response) {
        console.log(JSON.stringify(response));
    });
    checkLoginState();
  };

getLocation();
