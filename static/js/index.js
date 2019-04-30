import React from '../lib/node_modules/react'
import ReactDOM from '../lib/node_modules/react-dom'


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
