
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
