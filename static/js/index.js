
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
