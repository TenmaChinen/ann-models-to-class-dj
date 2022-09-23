

function sendFormRequest(form, callback, url) {
  const request = new XMLHttpRequest();
  request.open("POST", url, true);
  if (callback != null) {
    request.onreadystatechange = function () {
      if (request.readyState == 4 && request.status == 200) {
        callback(JSON.parse(request.responseText));
      }
    };
  }
  // request.setRequestHeader("X-CSRFToken", csrftoken);
  // request.setRequestHeader("Content-Type", "application/json");
  // request.send(JSON.stringify(data));
  const formData = new FormData(form);
  request.send(formData);
}