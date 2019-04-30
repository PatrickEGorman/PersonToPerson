function login() {
    FB.login(function (response) {
        if (response.authResponse) {
            console.log('Welcome!  Fetching your information.... ');
        } else {
            console.log('User cancelled login or did not fully authorize.');
        }
    });
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected'){
        document.cookie = "facebook_access_token="+response.authResponse.facebook_access_token;
        console.log('test');
    }
    else{
        console.log('do something here');
    }
  });
}
