function login() {
    FB.login(function (response) {
        if (response.authResponse) {
            console.log('Welcome!  Fetching your information.... ');
            FB.api('/me', function (response) {
                console.log('Good to see you, ' + response.name + '.');
            });
        } else {
            console.log('User cancelled login or did not fully authorize.');
        }
    });
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    if(response.status === 'connected'){
        document.cookie = "facebook_access_token="+response.authResponse.facebook_access_token;
        $.post('/set_facebook_access_token', data={'facebook_access_token': response.authResponse.accessToken})
    }
    else{
        console.log('do something here');
    }
  });
}
